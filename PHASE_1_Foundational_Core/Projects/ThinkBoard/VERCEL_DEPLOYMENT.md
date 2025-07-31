# 🚀 Vercel Deployment Guide for ThinkBoard

This guide will help you deploy the ThinkBoard application to Vercel.com

## 📋 Prerequisites

1. **GitHub Account**: Your code should be on GitHub
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Node.js**: Install Node.js for Vercel CLI (optional)

## 🔧 Step-by-Step Deployment

### Step 1: Prepare Your Repository

Ensure your repository has these files:
```
ThinkBoard/
├── app.py (main Flask application)
├── vercel.json (Vercel configuration)
├── requirements.txt (dependencies)
├── static/ (web assets)
└── Uploads/ (data files)
```

### Step 2: Vercel Account Setup

1. Go to [vercel.com](https://vercel.com)
2. **Sign up/Login** with your GitHub account
3. **Connect your GitHub repository**

### Step 3: Deploy via Vercel Dashboard

#### Method 1: Dashboard Deployment

1. **Go to Vercel Dashboard**
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Select the repository** containing ThinkBoard
5. **Configure project settings**:
   - **Framework Preset**: Other
   - **Root Directory**: `PHASE_1_Foundational_Core/Projects/ThinkBoard`
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`
6. **Click "Deploy"**

#### Method 2: Vercel CLI (Optional)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Navigate to project directory**:
   ```bash
   cd PHASE_1_Foundational_Core/Projects/ThinkBoard
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Link to existing project or create new
   - Confirm settings
   - Deploy

### Step 4: Configuration

#### vercel.json Configuration
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "functions": {
    "app.py": {
      "runtime": "python3.9"
    }
  }
}
```

#### Environment Variables (Optional)
Add these in Vercel dashboard if needed:
- `PYTHON_VERSION`: `3.9`
- `FLASK_ENV`: `production`

### Step 5: Deploy

1. **Click "Deploy"** in Vercel dashboard
2. **Wait for build** (usually 1-3 minutes)
3. **Check logs** for any errors
4. **Your app will be live** at the provided URL

## 🔍 Troubleshooting

### Common Issues:

#### 1. Build Failures
- Check `requirements.txt` has compatible versions
- Ensure all dependencies are listed
- Verify Python version compatibility (3.9 recommended)

#### 2. Runtime Errors
- Check function logs in Vercel dashboard
- Verify `vercel.json` configuration
- Ensure `app.py` has proper Flask app instance

#### 3. File Upload Issues
- Vercel has **read-only filesystem** in production
- File uploads will **not persist** between requests
- Consider using **external storage** (AWS S3, etc.)

#### 4. Static Files
- Ensure `static/` folder is included
- Check file paths are correct
- Verify HTML references

## 📊 Monitoring

### Function Logs
- **Real-time logs** in Vercel dashboard
- **Function execution** details
- **Error tracking** and debugging

### Analytics
- **Page views** and traffic
- **Function invocations**
- **Performance metrics**

## 🔄 Updates

### Automatic Deployments
- Vercel automatically deploys on GitHub pushes
- **Preview deployments** for pull requests
- **Production deployments** for main branch

### Manual Deployment
1. Go to your project in Vercel dashboard
2. Click "Redeploy"
3. Select branch/commit
4. Deploy

## 🌐 Custom Domain

1. **Add Custom Domain** in Vercel dashboard
2. **Configure DNS** with your domain provider
3. **SSL Certificate** automatically provided by Vercel

## 📈 Performance

### Vercel Free Tier
- **100GB bandwidth** per month
- **100GB storage**
- **Unlimited serverless functions**
- **Global CDN** included

### Limitations
- **10-second timeout** for serverless functions
- **50MB payload** limit
- **Read-only filesystem** in production

## 🔒 Security

### Environment Variables
- **Never commit secrets** to GitHub
- **Use Vercel environment variables** for sensitive data
- **Secure by default** with Vercel

### File Upload Security
- **File size limits** implemented
- **File type validation** active
- **Secure filename handling** enabled

## 📞 Support

### Vercel Support
- **Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Community**: Vercel Discord/Slack
- **Email Support**: Available on paid plans

### Application Issues
- Check function logs
- Verify all files are present
- Test locally before deploying

## 🎯 Success Checklist

- ✅ Repository connected to Vercel
- ✅ Build completes successfully
- ✅ Application starts without errors
- ✅ Health check endpoint responds
- ✅ Static files serve correctly
- ✅ Custom domain configured (optional)
- ✅ SSL certificate active (automatic)

## 🚀 Next Steps

After successful deployment:
1. **Test all features** thoroughly
2. **Monitor function logs** and performance
3. **Set up custom domain** if needed
4. **Configure environment variables** for production
5. **Scale up** as traffic grows

## ⚠️ Important Notes

### File Upload Limitations
- **Vercel serverless functions** have read-only filesystem
- **Uploaded files** will not persist between requests
- **Consider alternatives**:
  - AWS S3 for file storage
  - Database storage for small files
  - Client-side processing

### Static Files
- **Static files** work normally
- **CSS, JS, images** serve correctly
- **HTML templates** function properly

Your ThinkBoard application should now be live and accessible worldwide! 🌍

## 🔗 Quick Deploy

**One-click deploy** (if repository is public):
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/MuhammadTahaNasir/Learning-AI&root-directory=PHASE_1_Foundational_Core/Projects/ThinkBoard) 