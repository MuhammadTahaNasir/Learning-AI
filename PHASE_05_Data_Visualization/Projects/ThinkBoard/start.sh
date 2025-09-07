#!/bin/bash

echo "🚀 Starting ThinkBoard on Railway..."
echo "📊 Environment: $RAILWAY_ENVIRONMENT"
echo "🔧 Port: $PORT"
echo "🏠 Host: $HOST"

# Create upload directory if it doesn't exist
mkdir -p Uploads
mkdir -p /tmp/uploads

# Set permissions
chmod 755 Uploads
chmod 755 /tmp/uploads

# Start the Flask application
python app.py 