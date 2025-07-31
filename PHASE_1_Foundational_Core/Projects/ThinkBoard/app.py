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
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'Uploads')
ALLOWED_EXTENSIONS = {'csv'}
MAX_FILE_SIZE = int(os.environ.get('MAX_FILE_SIZE', 5 * 1024 * 1024))  # 5MB for Railway

# Ensure upload folder exists with proper permissions
try:
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # Set write permissions
    os.chmod(UPLOAD_FOLDER, 0o755)
except Exception as e:
    logger.error(f"Error creating upload folder: {e}")
    # Fallback to temp directory
    UPLOAD_FOLDER = '/tmp'
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

@app.route('/test-upload', methods=['GET'])
def test_upload():
    """Test upload functionality"""
    try:
        # Test if we can write to upload folder
        test_file = os.path.join(UPLOAD_FOLDER, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        
        return jsonify({
            "status": "success",
            "message": "Upload folder is writable",
            "upload_folder": UPLOAD_FOLDER,
            "permissions": oct(os.stat(UPLOAD_FOLDER).st_mode)[-3:]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Upload folder test failed: {str(e)}",
            "upload_folder": UPLOAD_FOLDER
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    # Check upload folder status
    upload_status = "OK"
    try:
        if not os.path.exists(UPLOAD_FOLDER):
            upload_status = "NOT_EXISTS"
        elif not os.access(UPLOAD_FOLDER, os.W_OK):
            upload_status = "NOT_WRITABLE"
    except Exception as e:
        upload_status = f"ERROR: {str(e)}"
    
    return jsonify({
        "status": "healthy",
        "message": "ThinkBoard is running",
        "version": "1.0.0",
        "upload_folder": UPLOAD_FOLDER,
        "upload_status": upload_status,
        "max_file_size_mb": MAX_FILE_SIZE // (1024*1024)
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload and process CSV file"""
    try:
        logger.info("Upload request received")
        
        if 'file' not in request.files:
            logger.error("No file in request")
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            logger.error("Empty filename")
            return jsonify({"error": "No file selected"}), 400
        
        logger.info(f"Processing file: {file.filename}")
        
        if not allowed_file(file.filename):
            logger.error(f"Invalid file type: {file.filename}")
            return jsonify({"error": "Invalid file type. Only CSV files are allowed"}), 400
        
        # Check file size
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset to beginning
        
        logger.info(f"File size: {file_size} bytes")
        
        if file_size > MAX_FILE_SIZE:
            logger.error(f"File too large: {file_size} > {MAX_FILE_SIZE}")
            return jsonify({"error": f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)}MB"}), 413
        
        # Secure filename and save
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        logger.info(f"Saving file to: {file_path}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save file with error handling
        try:
            file.save(file_path)
            logger.info(f"File saved successfully: {file_path}")
        except Exception as save_error:
            logger.error(f"Error saving file: {save_error}")
            return jsonify({"error": f"Error saving file: {str(save_error)}"}), 500
        
        # Validate CSV content
        is_valid, message = validate_csv(file_path)
        if not is_valid:
            os.remove(file_path)  # Clean up invalid file
            return jsonify({"error": message}), 400
        
        # Process the data
        df = pd.read_csv(file_path)
        logger.info(f"File uploaded successfully: {filename} with {len(df)} rows and {len(df.columns)} columns")
        
        # Calculate statistics
        summary = {
            "columns": df.columns.tolist(),
            "row_count": len(df),
            "mean_values": {},
            "median_values": {},
            "mode_values": {},
            "max_values": {},
            "min_values": {},
            "numeric_columns": []
        }
        
        # Process numeric columns
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        summary["numeric_columns"] = numeric_columns.tolist()
        
        for col in numeric_columns:
            summary["mean_values"][col] = float(df[col].mean())
            summary["median_values"][col] = float(df[col].median())
            summary["max_values"][col] = float(df[col].max())
            summary["min_values"][col] = float(df[col].min())
            
            # Handle mode (can be multiple values)
            mode_result = df[col].mode()
            if not mode_result.empty:
                summary["mode_values"][col] = float(mode_result.iloc[0])
            else:
                summary["mode_values"][col] = None
        
        return jsonify({
            "message": "File uploaded successfully",
            "filename": filename,
            "summary": summary
        })
        
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

@app.route('/sort', methods=['POST'])
def sort_data():
    """Sort data by specified column"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        column = data.get('column')
        order = data.get('order', 'asc')
        
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
        ascending = order.lower() == 'asc'
        sorted_df = df.sort_values(by=column, ascending=ascending)
        
        logger.info(f"Data sorted by {column} in {order} order")
        
        return jsonify(sorted_df.to_dict('records'))
        
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
        query = data.get('query')
        
        if not column or not query:
            return jsonify({"error": "Column name and query are required"}), 400
        
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
        
        # Search the data
        search_results = df[df[column].astype(str).str.contains(query, case=False, na=False)]
        
        logger.info(f"Search completed for '{query}' in column '{column}', found {len(search_results)} results")
        
        return jsonify(search_results.to_dict('records'))
        
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
    print("🚀 Starting ThinkBoard Server...")
    print("📊 Dashboard will be available at: http://127.0.0.1:5000")
    print("🔧 API endpoints:")
    print("   - POST /upload: Upload CSV file")
    print("   - POST /sort: Sort data")
    print("   - POST /search: Search data")
    print("   - POST /gradient: Compute gradient")
    print("   - GET /stats: Get file statistics")
    print("   - GET /health: Health check")
    print("=" * 50)
    
    # Railway deployment configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    # Use debug=False for production
    app.run(debug=False, host=host, port=port)