from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'Uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Store the latest uploaded file path
latest_file_path = None

# File Handling Module
@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve index.html from static folder

@app.route('/upload', methods=['POST'])
def upload_file():
    global latest_file_path
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        latest_file_path = file_path  # Store file path

        # Analysis Module
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                return jsonify({'error': 'Empty CSV file'}), 400

            # Calculate mode, taking the first mode if multiple
            mode_values = df.mode(numeric_only=True).iloc[0].to_dict()

            summary = {
                'columns': list(df.columns),
                'row_count': len(df),
                'mean_values': df.mean(numeric_only=True).to_dict(),
                'median_values': df.median(numeric_only=True).to_dict(),
                'mode_values': mode_values,
                'max_values': df.max(numeric_only=True).to_dict(),
                'min_values': df.min(numeric_only=True).to_dict()
            }
            return jsonify({'summary': summary})
        except Exception as e:
            return jsonify({'error': f'Error processing CSV: {str(e)}'}), 400

# Search/Sort Module
@app.route('/sort', methods=['POST'])
def sort_data():
    global latest_file_path
    data = request.get_json()
    column = data.get('column')
    order = data.get('order', 'asc')

    if not latest_file_path or not os.path.exists(latest_file_path):
        return jsonify({'error': 'No file uploaded or file not found'}), 400

    try:
        df = pd.read_csv(latest_file_path)
        if column not in df.columns:
            return jsonify({'error': f'Column {column} not found'}), 400
        sorted_df = df.sort_values(by=column, ascending=(order == 'asc'))
        return jsonify(sorted_df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': f'Error sorting data: {str(e)}'}), 400

@app.route('/search', methods=['POST'])
def search_data():
    global latest_file_path
    data = request.get_json()
    column = data.get('column')
    query = data.get('query')

    if not latest_file_path or not os.path.exists(latest_file_path):
        return jsonify({'error': 'No file uploaded or file not found'}), 400

    try:
        df = pd.read_csv(latest_file_path)
        if column not in df.columns:
            return jsonify({'error': f'Column {column} not found'}), 400
        result = df[df[column].astype(str).str.contains(query, case=False, na=False)]
        return jsonify(result.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': f'Error searching data: {str(e)}'}), 400

# Math Tools Module: Gradient calculation
@app.route('/gradient', methods=['POST'])
def gradient():
    global latest_file_path
    data = request.get_json()
    column = data.get('column')

    if not latest_file_path or not os.path.exists(latest_file_path):
        return jsonify({'error': 'No file uploaded or file not found'}), 400

    try:
        df = pd.read_csv(latest_file_path)
        if column not in df.columns:
            return jsonify({'error': f'Column {column} not found'}), 400
        if not pd.api.types.is_numeric_dtype(df[column]):
            return jsonify({'error': f'Column {column} must be numeric'}), 400
        gradients = np.gradient(df[column].dropna())
        return jsonify({'gradients': gradients.tolist()})
    except Exception as e:
        return jsonify({'error': f'Error computing gradient: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)