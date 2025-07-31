# 🚀 Render Deployment Guide for ThinkBoard

This guide will help you deploy the ThinkBoard application to Render.com

## 📋 Prerequisites

1. **GitHub Account**: Your code should be on GitHub
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Python Knowledge**: Basic understanding of Flask applications

## 🔧 Step-by-Step Deployment

### Step 1: Prepare Your Repository

Ensure your repository has these files:
```
ThinkBoard/
├── app.py (main Flask application)
├── wsgi.py (for gunicorn)
├── requirements.txt (dependencies)
├── render.yaml (deployment config)
├── build.sh (build script)
├── static/ (web assets)
└── Uploads/ (data files)
```

### Step 2: Render Account Setup

1. Go to [render.com](https://render.com)
2. **Sign up/Login** with your GitHub account
3. **Connect your GitHub repository**

### Step 3: Create New Web Service

1. **Click "New +"** in your Render dashboard
2. **Select "Web Service"**
3. **Connect your GitHub repository**
4. **Select the repository** containing ThinkBoard

### Step 4: Configure Service Settings

**Service Name**: `thinkboard-app` (or your preferred name)

**Environment**: `Python 3`

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn wsgi:app
```

**Root Directory**: Leave empty (or specify if needed)

### Step 5: Environment Variables (Optional)

Add these if needed:
- `PYTHON_VERSION`: `3.9.16`
- `FLASK_ENV`: `production`

### Step 6: Deploy

1. **Click "Create Web Service"**
2. **Wait for build** (usually 2-5 minutes)
3. **Check logs** for any errors
4. **Your app will be live** at the provided URL

## 🔍 Troubleshooting

### Common Issues:

#### 1. Build Failures
- Check `requirements.txt` has correct versions
- Ensure all dependencies are listed
- Verify Python version compatibility

#### 2. Runtime Errors
- Check application logs in Render dashboard
- Verify `wsgi.py` file exists and is correct
- Ensure `app.py` has proper Flask app instance

#### 3. Port Issues
- Render automatically sets `PORT` environment variable
- App should use: `port = int(os.environ.get('PORT', 5000))`

#### 4. File Upload Issues
- Ensure `Uploads/` directory exists
- Check file permissions
- Verify CORS settings

## 📊 Monitoring

### Health Check
Your app includes a health check endpoint:
```
GET /health
```

### Logs
- **Build Logs**: Check during deployment
- **Runtime Logs**: Monitor application performance
- **Error Logs**: Debug issues

## 🔄 Updates

### Automatic Deployments
- Render automatically deploys on GitHub pushes
- Manual deployments available in dashboard
- Rollback to previous versions if needed

### Manual Deployment
1. Go to your service in Render dashboard
2. Click "Manual Deploy"
3. Select branch/commit
4. Deploy

## 🌐 Custom Domain (Optional)

1. **Add Custom Domain** in Render dashboard
2. **Configure DNS** with your domain provider
3. **SSL Certificate** automatically provided by Render

## 📈 Performance

### Free Tier Limitations
- **512 MB RAM**
- **0.1 CPU**
- **Sleep after 15 minutes** of inactivity
- **750 hours/month** free

### Upgrading
- **Paid plans** available for better performance
- **Auto-scaling** options
- **Custom domains** with SSL

## 🔒 Security

### Environment Variables
- **Never commit secrets** to GitHub
- **Use Render environment variables** for sensitive data
- **Database credentials** should be environment variables

### File Upload Security
- **File size limits** implemented
- **File type validation** active
- **Secure filename handling** enabled

## 📞 Support

### Render Support
- **Documentation**: [docs.render.com](https://docs.render.com)
- **Community**: Render Discord/Slack
- **Email Support**: Available on paid plans

### Application Issues
- Check application logs
- Verify all files are present
- Test locally before deploying

## 🎯 Success Checklist

- ✅ Repository connected to Render
- ✅ Build completes successfully
- ✅ Application starts without errors
- ✅ Health check endpoint responds
- ✅ File upload functionality works
- ✅ Custom domain configured (optional)
- ✅ SSL certificate active (automatic)

## 🚀 Next Steps

After successful deployment:
1. **Test all features** thoroughly
2. **Monitor performance** and logs
3. **Set up alerts** for downtime
4. **Configure backups** if needed
5. **Scale up** as traffic grows

Your ThinkBoard application should now be live and accessible worldwide! 🌍 