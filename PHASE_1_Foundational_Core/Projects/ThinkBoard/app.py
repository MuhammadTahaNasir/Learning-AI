#!/usr/bin/env python3
"""
ThinkBoard - Data Analytics Dashboard
A Flask application for data analysis and visualization
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import os
import logging
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'csv'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_csv(file_path):
    """Validate CSV file content"""
    try:
        df = pd.read_csv(file_path)
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
    return send_from_directory('static', 'index.html')

@app.route('/Uploads/<filename>')
def serve_sample_data(filename):
    """Serve sample data files"""
    return send_from_directory('Uploads', filename)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "ThinkBoard is running",
        "version": "1.0.0"
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload and process CSV file"""
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
        
        # Secure filename and save
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        # Validate CSV content
        is_valid, message = validate_csv(file_path)
        if not is_valid:
            os.remove(file_path)  # Clean up invalid file
            return jsonify({"error": message}), 400
        
        # Process the data
        df = pd.read_csv(file_path)
        logger.info(f"File uploaded successfully: {filename} with {len(df)} rows and {len(df.columns)} columns")
        
        # Return file info
        return jsonify({
            "message": "File uploaded successfully",
            "filename": filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "preview": df.head(5).to_dict('records')
        })
        
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return jsonify({"error": f"Error uploading file: {str(e)}"}), 500

@app.route('/sort', methods=['POST'])
def sort_data():
    """Sort data by specified column"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column = data.get('column')
        ascending = data.get('ascending', True)
        
        if not column:
            return jsonify({"error": "Column name is required"}), 400
        
        # Get the latest uploaded file
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
        if not files:
            return jsonify({"error": "No CSV files found"}), 404
        
        latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(UPLOAD_FOLDER, x)))
        file_path = os.path.join(UPLOAD_FOLDER, latest_file)
        
        df = pd.read_csv(file_path)
        
        if column not in df.columns:
            available_columns = df.columns.tolist()
            return jsonify({"error": f"Column '{column}' not found. Available columns: {available_columns}"}), 400
        
        # Sort the data
        df_sorted = df.sort_values(by=column, ascending=ascending)
        
        logger.info(f"Data sorted by column '{column}' in {'ascending' if ascending else 'descending'} order")
        
        return jsonify({
            "message": "Data sorted successfully",
            "column": column,
            "ascending": ascending,
            "sorted_data": df_sorted.head(10).to_dict('records')
        })
        
    except Exception as e:
        logger.error(f"Error sorting data: {str(e)}")
        return jsonify({"error": f"Error sorting data: {str(e)}"}), 500

@app.route('/search', methods=['POST'])
def search_data():
    """Search data in specified column"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column = data.get('column')
        search_term = data.get('search_term', '')
        
        if not column:
            return jsonify({"error": "Column name is required"}), 400
        
        # Get the latest uploaded file
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
        if not files:
            return jsonify({"error": "No CSV files found"}), 404
        
        latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(UPLOAD_FOLDER, x)))
        file_path = os.path.join(UPLOAD_FOLDER, latest_file)
        
        df = pd.read_csv(file_path)
        
        if column not in df.columns:
            available_columns = df.columns.tolist()
            return jsonify({"error": f"Column '{column}' not found. Available columns: {available_columns}"}), 400
        
        # Search in the column
        if search_term:
            # Convert to string for searching
            df[column] = df[column].astype(str)
            mask = df[column].str.contains(search_term, case=False, na=False)
            df_filtered = df[mask]
        else:
            df_filtered = df
        
        logger.info(f"Search completed for '{search_term}' in column '{column}'. Found {len(df_filtered)} results")
        
        return jsonify({
            "message": "Search completed",
            "column": column,
            "search_term": search_term,
            "results_count": len(df_filtered),
            "search_results": df_filtered.head(10).to_dict('records')
        })
        
    except Exception as e:
        logger.error(f"Error searching data: {str(e)}")
        return jsonify({"error": f"Error searching data: {str(e)}"}), 500

@app.route('/gradient', methods=['POST'])
def compute_gradient():
    """Compute gradient for numeric column"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column = data.get('column')
        if not column:
            return jsonify({"error": "Column name is required"}), 400
        
        # Get the latest uploaded file
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
        if not files:
            return jsonify({"error": "No CSV files found"}), 404
        
        latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(UPLOAD_FOLDER, x)))
        file_path = os.path.join(UPLOAD_FOLDER, latest_file)
        
        df = pd.read_csv(file_path)
        
        if column not in df.columns:
            available_columns = df.columns.tolist()
            return jsonify({"error": f"Column '{column}' not found. Available columns: {available_columns}"}), 400
        
        # Check if column is numeric
        if not np.issubdtype(df[column].dtype, np.number):
            return jsonify({"error": f"Column '{column}' is not numeric"}), 400
        
        # Check if we have enough data for gradient
        if len(df) < 2:
            return jsonify({"error": "Need at least 2 data points for gradient calculation"}), 400
        
        # Compute gradient
        values = df[column].values
        gradients = np.gradient(values)
        
        logger.info(f"Gradient computed for column '{column}'")
        
        return jsonify({
            "column": column,
            "gradients": gradients.tolist()
        })
        
    except Exception as e:
        logger.error(f"Error computing gradient: {str(e)}")
        return jsonify({"error": f"Error computing gradient: {str(e)}"}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    """Get basic statistics about uploaded files"""
    try:
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
        if not files:
            return jsonify({"message": "No CSV files found"}), 404
        
        stats = []
        for filename in files:
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            df = pd.read_csv(file_path)
            stats.append({
                "filename": filename,
                "rows": len(df),
                "columns": len(df.columns),
                "numeric_columns": len(df.select_dtypes(include=[np.number]).columns)
            })
        
        return jsonify({
            "total_files": len(files),
            "files": stats
        })
        
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return jsonify({"error": f"Error getting stats: {str(e)}"}), 500

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

if __name__ == '__main__':
    # Get port from environment variable (for Railway deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)