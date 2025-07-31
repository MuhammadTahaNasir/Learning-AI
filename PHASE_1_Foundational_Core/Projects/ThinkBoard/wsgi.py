#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app

if __name__ == "__main__":
    # Railway deployment configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"🚀 Starting ThinkBoard on Railway at {host}:{port}")
    
    # Start the application
    app.run(debug=False, host=host, port=port, threaded=True) 