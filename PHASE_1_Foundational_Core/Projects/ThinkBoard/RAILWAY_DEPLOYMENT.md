# Railway Deployment Guide for ThinkBoard

This guide will help you deploy ThinkBoard to Railway platform.

## 🚀 Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **GitHub Repository**: Your code should be on GitHub
3. **Railway CLI** (optional): Install for local testing

## 📁 Required Files

The following files are already created for Railway deployment:

### 1. `Procfile`
```
web: python app.py
```
- Tells Railway how to start the application
- Uses `web` process type for HTTP services

### 2. `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```
- Configures Railway build and deployment settings
- Uses NIXPACKS builder for automatic dependency detection

### 3. `requirements.txt`
```
Flask>=3.0.0
Flask-CORS>=4.0.0
pandas>=2.2.0
numpy>=1.26.0
Werkzeug>=3.0.0
```
- Lists all Python dependencies
- Railway automatically installs these packages

### 4. Modified `app.py`
- Updated to use environment variables for port and host
- Compatible with Railway's deployment environment

## 🚀 Deployment Steps

### Method 1: GitHub Integration (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Railway deployment files"
   git push origin main
   ```

2. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select the branch (usually `main`)

3. **Configure Deployment**
   - Railway will automatically detect it's a Python project
   - It will use the `Procfile` to start the application
   - The `railway.json` will configure build settings

4. **Deploy**
   - Railway will automatically build and deploy
   - You'll get a URL like: `https://your-app-name.railway.app`

### Method 2: Railway CLI

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Project**
   ```bash
   cd PHASE_1_Foundational_Core/Projects/ThinkBoard
   railway init
   ```

4. **Deploy**
   ```bash
   railway up
   ```

## 🔧 Environment Variables

Railway automatically sets these environment variables:

- `PORT`: The port your app should listen on
- `HOST`: The host address (usually `0.0.0.0`)

## 📊 Application Features

Once deployed, your ThinkBoard will have:

### Web Interface
- **URL**: `https://your-app-name.railway.app`
- **Features**: File upload, data visualization, analytics

### API Endpoints
- `GET /health` - Health check
- `POST /upload` - Upload CSV files
- `POST /sort` - Sort data
- `POST /search` - Search data
- `POST /gradient` - Compute gradients
- `GET /stats` - Get file statistics

## 🔍 Monitoring

### Railway Dashboard
- **Logs**: View real-time application logs
- **Metrics**: Monitor CPU, memory usage
- **Deployments**: Track deployment history

### Health Check
```bash
curl https://your-app-name.railway.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "message": "ThinkBoard is running",
  "version": "1.0.0"
}
```

## 🛠️ Troubleshooting

### Common Issues

1. **Build Fails**
   - Check `requirements.txt` has all dependencies
   - Verify Python version compatibility
   - Check Railway logs for specific errors

2. **App Won't Start**
   - Ensure `Procfile` is correct
   - Check if `app.py` runs locally
   - Verify port configuration

3. **File Upload Issues**
   - Check file size limits (now 5MB max)
   - Verify upload folder permissions
   - Test with sample CSV files
   - Use `/test-upload` endpoint to check folder status
   - Use `/health` endpoint to see upload folder status

### Debug Steps for Upload Issues

1. **Check Health Status**
   ```bash
   curl https://your-app-name.railway.app/health
   ```
   Look for `upload_status` field.

2. **Test Upload Folder**
   ```bash
   curl https://your-app-name.railway.app/test-upload
   ```
   This will test if the upload folder is writable.

3. **Check Railway Logs**
   - Go to Railway dashboard
   - Check logs for upload-related errors
   - Look for permission or file system errors

4. **Common Solutions**
   - **Permission Error**: The app now uses `/tmp` as fallback
   - **File Size**: Reduced to 5MB for Railway compatibility
   - **CORS Issues**: Added better error handling and logging

### Debug Commands

```bash
# Check Railway logs
railway logs

# View deployment status
railway status

# Restart application
railway restart
```

## 🔄 Updates

To update your deployed application:

1. **Make changes locally**
2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Update ThinkBoard"
   git push origin main
   ```
3. **Railway automatically redeploys**

## 💰 Cost Management

- **Free Tier**: Limited usage, suitable for testing
- **Paid Plans**: For production use
- **Auto-scaling**: Railway can scale based on traffic

## 🎯 Best Practices

1. **Environment Variables**: Use for configuration
2. **Logging**: Implement proper logging for debugging
3. **Error Handling**: Add comprehensive error handling
4. **Testing**: Test locally before deploying
5. **Monitoring**: Set up alerts for critical issues

## 📞 Support

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Railway Discord**: Community support
- **GitHub Issues**: For code-specific problems

## 🎉 Success!

Once deployed, your ThinkBoard will be available at:
```
https://your-app-name.railway.app
```

Share this URL with others to let them use your data analytics dashboard! 