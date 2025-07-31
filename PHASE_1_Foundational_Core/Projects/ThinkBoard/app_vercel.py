#!/usr/bin/env python3
"""
ThinkBoard - Data Analytics Dashboard (Vercel Compatible)
A Flask application for data analysis and visualization
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import os
import logging
import io
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
ALLOWED_EXTENSIONS = {'csv'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_csv_data(file_data):
    """Validate CSV data content"""
    try:
        df = pd.read_csv(io.StringIO(file_data))
        if df.empty:
            return False, "CSV file is empty"
        if len(df.columns) == 0:
            return False, "CSV file has no columns"
        return True, "Valid CSV file"
    except Exception as e:
        return False, f"Invalid CSV file: {str(e)}"

@app.route('/')
def index():
    """Serve the main dashboard"""
    return send_from_directory('static', 'vercel_index.html')

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "ThinkBoard is running (Vercel Compatible)",
        "version": "1.0.0",
        "note": "File processing is client-side for Vercel compatibility"
    })

@app.route('/process-csv', methods=['POST'])
def process_csv():
    """Process CSV data immediately without saving"""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Only CSV files are allowed"}), 400
        
        # Check file size
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset to beginning
        
        if file_size > MAX_FILE_SIZE:
            return jsonify({"error": f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)}MB"}), 413
        
        # Read file data
        file_data = file.read().decode('utf-8')
        
        # Validate CSV content
        is_valid, message = validate_csv_data(file_data)
        if not is_valid:
            return jsonify({"error": message}), 400
        
        # Process the data immediately
        df = pd.read_csv(io.StringIO(file_data))
        logger.info(f"File processed successfully: {file.filename} with {len(df)} rows and {len(df.columns)} columns")
        
        # Calculate basic statistics
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        stats = {}
        
        for col in numeric_columns:
            stats[col] = {
                "mean": float(df[col].mean()),
                "median": float(df[col].median()),
                "std": float(df[col].std()),
                "min": float(df[col].min()),
                "max": float(df[col].max())
            }
        
        # Return comprehensive analysis
        return jsonify({
            "message": "File processed successfully",
            "filename": file.filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "numeric_columns": numeric_columns,
            "preview": df.head(10).to_dict('records'),
            "statistics": stats,
            "data_types": df.dtypes.to_dict()
        })
        
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

@app.route('/analyze-column', methods=['POST'])
def analyze_column():
    """Analyze specific column from uploaded data"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column_name = data.get('column')
        operation = data.get('operation', 'stats')  # stats, sort, search
        
        if not column_name:
            return jsonify({"error": "Column name is required"}), 400
        
        # Get file data from request (in real app, this would come from client)
        file_data = data.get('file_data')
        if not file_data:
            return jsonify({"error": "File data is required"}), 400
        
        # Process the data
        df = pd.read_csv(io.StringIO(file_data))
        
        if column_name not in df.columns:
            available_columns = df.columns.tolist()
            return jsonify({"error": f"Column '{column_name}' not found. Available columns: {available_columns}"}), 400
        
        # Perform analysis based on operation
        if operation == 'stats':
            if np.issubdtype(df[column_name].dtype, np.number):
                result = {
                    "column": column_name,
                    "type": "numeric",
                    "mean": float(df[column_name].mean()),
                    "median": float(df[column_name].median()),
                    "std": float(df[column_name].std()),
                    "min": float(df[column_name].min()),
                    "max": float(df[column_name].max()),
                    "count": int(df[column_name].count()),
                    "unique_values": int(df[column_name].nunique())
                }
            else:
                result = {
                    "column": column_name,
                    "type": "categorical",
                    "count": int(df[column_name].count()),
                    "unique_values": int(df[column_name].nunique()),
                    "most_common": df[column_name].value_counts().head(5).to_dict()
                }
        
        elif operation == 'sort':
            ascending = data.get('ascending', True)
            df_sorted = df.sort_values(by=column_name, ascending=ascending)
            result = {
                "column": column_name,
                "ascending": ascending,
                "sorted_data": df_sorted.head(20).to_dict('records')
            }
        
        elif operation == 'search':
            search_term = data.get('search_term', '')
            if search_term:
                df[column_name] = df[column_name].astype(str)
                mask = df[column_name].str.contains(search_term, case=False, na=False)
                df_filtered = df[mask]
            else:
                df_filtered = df
            
            result = {
                "column": column_name,
                "search_term": search_term,
                "results_count": len(df_filtered),
                "search_results": df_filtered.head(20).to_dict('records')
            }
        
        else:
            return jsonify({"error": "Invalid operation. Use 'stats', 'sort', or 'search'"}), 400
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error analyzing column: {str(e)}")
        return jsonify({"error": f"Error analyzing column: {str(e)}"}), 500

@app.route('/compute-gradient', methods=['POST'])
def compute_gradient():
    """Compute gradient for numeric column"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column_name = data.get('column')
        file_data = data.get('file_data')
        
        if not column_name or not file_data:
            return jsonify({"error": "Column name and file data are required"}), 400
        
        # Process the data
        df = pd.read_csv(io.StringIO(file_data))
        
        if column_name not in df.columns:
            available_columns = df.columns.tolist()
            return jsonify({"error": f"Column '{column_name}' not found. Available columns: {available_columns}"}), 400
        
        # Check if column is numeric
        if not np.issubdtype(df[column_name].dtype, np.number):
            return jsonify({"error": f"Column '{column_name}' is not numeric"}), 400
        
        # Check if we have enough data for gradient
        if len(df) < 2:
            return jsonify({"error": "Need at least 2 data points for gradient calculation"}), 400
        
        # Compute gradient
        values = df[column_name].values
        gradients = np.gradient(values)
        
        logger.info(f"Gradient computed for column '{column_name}'")
        
        return jsonify({
            "column": column_name,
            "gradients": gradients.tolist(),
            "original_values": values.tolist()
        })
        
    except Exception as e:
        logger.error(f"Error computing gradient: {str(e)}")
        return jsonify({"error": f"Error computing gradient: {str(e)}"}), 500

# Error handlers
@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large"}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

# For Vercel deployment - no main execution block needed
# Vercel will handle the serverless function execution 