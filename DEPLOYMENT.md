# 🚀 Deployment Guide

## Deploy to Vercel (Recommended - Free)

### Method 1: Vercel Dashboard (Easiest)

1. **Push to GitHub** (already done ✓)

2. **Go to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub

3. **Import Project**
   - Click "Add New" → "Project"
   - Import `Anshuljain1235/Fake_Review_Monitor`
   - Click "Import"

4. **Configure Project**
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live at: `https://fake-review-monitor.vercel.app`

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name? fake-review-monitor
# - Directory? ./
# - Override settings? N

# Production deployment
vercel --prod
```

### Environment Variables (if needed)
In Vercel Dashboard → Settings → Environment Variables:
```
FLASK_ENV=production
```

---

## Deploy to Render (Alternative - Free)

1. **Go to Render**
   - Visit [render.com](https://render.com)
   - Sign up/Login with GitHub

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Connect `Anshuljain1235/Fake_Review_Monitor`

3. **Configure**
   - Name: `fake-review-monitor`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Add gunicorn to requirements.txt**
   ```
   gunicorn
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes
   - Live at: `https://fake-review-monitor.onrender.com`

---

## Deploy to Railway (Alternative - Free)

1. **Go to Railway**
   - Visit [railway.app](https://railway.app)
   - Sign up/Login with GitHub

2. **New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `Anshuljain1235/Fake_Review_Monitor`

3. **Configure**
   - Railway auto-detects Python
   - Auto-deploys on push
   - No configuration needed!

4. **Get URL**
   - Settings → Generate Domain
   - Live at: `https://fake-review-monitor.up.railway.app`

---

## Deploy to Heroku (Alternative)

1. **Install Heroku CLI**
   ```bash
   # Download from heroku.com/cli
   ```

2. **Login**
   ```bash
   heroku login
   ```

3. **Create App**
   ```bash
   heroku create fake-review-monitor
   ```

4. **Add Procfile**
   Create `Procfile`:
   ```
   web: gunicorn app:app
   ```

5. **Add gunicorn**
   Add to `requirements.txt`:
   ```
   gunicorn
   ```

6. **Deploy**
   ```bash
   git add .
   git commit -m "Add Heroku config"
   git push heroku main
   ```

7. **Open**
   ```bash
   heroku open
   ```

---

## Deploy to PythonAnywhere (Alternative)

1. **Sign up** at [pythonanywhere.com](https://pythonanywhere.com)

2. **Upload Code**
   - Go to Files
   - Upload all project files

3. **Create Web App**
   - Web → Add new web app
   - Python 3.10
   - Manual configuration

4. **Configure WSGI**
   Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:
   ```python
   import sys
   path = '/home/yourusername/Fake_Review_Monitor'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Reload** web app

---

## Troubleshooting

### Vercel Issues

**Issue: Module not found**
- Ensure `requirements.txt` is in root
- Check `vercel.json` configuration

**Issue: Static files not loading**
- Check `vercel.json` routes
- Ensure `static/` folder exists

**Issue: App crashes on startup**
- Check Vercel logs: Dashboard → Deployments → View Logs
- Verify Python version compatibility

### General Issues

**Issue: Port binding error**
```python
# Use environment port
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
```

**Issue: Large dataset timeout**
- Use smaller dataset for serverless
- Or switch to Render/Railway (not serverless)

**Issue: Memory limit exceeded**
- Reduce model complexity
- Use lighter dependencies
- Upgrade to paid tier

---

## Performance Tips

1. **Enable Caching**
   - Cache model on startup
   - Use CDN for static files

2. **Optimize Images**
   - Compress chart images
   - Use WebP format

3. **Minify Assets**
   - Minify CSS/JS
   - Remove unused code

4. **Use Production Mode**
   ```python
   app.config['DEBUG'] = False
   ```

---

## Custom Domain (Optional)

### Vercel
1. Dashboard → Settings → Domains
2. Add your domain
3. Update DNS records (provided by Vercel)

### Render
1. Settings → Custom Domain
2. Add domain
3. Update DNS CNAME

---

## Monitoring

### Vercel Analytics
- Dashboard → Analytics
- View traffic, performance, errors

### Uptime Monitoring
- [UptimeRobot](https://uptimerobot.com) (free)
- [Pingdom](https://pingdom.com)

---

## Cost Comparison

| Platform | Free Tier | Limits |
|----------|-----------|--------|
| **Vercel** | ✅ Yes | 100GB bandwidth/month |
| **Render** | ✅ Yes | 750 hours/month |
| **Railway** | ✅ Yes | $5 credit/month |
| **Heroku** | ❌ No | Paid only (was free) |
| **PythonAnywhere** | ✅ Yes | Limited CPU |

**Recommendation**: Start with **Vercel** for simplicity and speed.

---

## Next Steps After Deployment

1. ✅ Test all features on live URL
2. ✅ Update README with live demo link
3. ✅ Share on social media
4. ✅ Monitor performance
5. ✅ Collect user feedback

---

**Need help?** Open an issue on GitHub!
