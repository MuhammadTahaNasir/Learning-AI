#!/usr/bin/env python3
"""
ThinkBoard Startup Script
Checks dependencies and starts the application
"""

import sys
import subprocess
import os

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = ['flask', 'flask_cors', 'pandas', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run: pip install -r requirements.txt")
            return False
    
    return True

def start_app():
    """Start the Flask application"""
    print("\n🚀 Starting ThinkBoard...")
    print("=" * 50)
    print("📊 ThinkBoard - Data Analytics Dashboard")
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        from app import app
        # Use debug=False to avoid watchdog issues with Python 3.13
        app.run(debug=False, host='127.0.0.1', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Thanks for using ThinkBoard!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

def main():
    """Main function"""
    print("🧪 ThinkBoard Startup Check")
    print("=" * 30)
    
    if check_dependencies():
        start_app()
    else:
        print("❌ Cannot start application due to missing dependencies")
        sys.exit(1)

if __name__ == "__main__":
    main() 