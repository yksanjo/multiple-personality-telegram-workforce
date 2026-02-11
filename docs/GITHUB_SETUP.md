# GitHub Setup & Deployment Guide

Complete guide to setting up, using, and sharing your Multiple Personality Telegram Workforce on GitHub.

## 📋 Prerequisites

Before you start:
- [ ] GitHub account
- [ ] Telegram account
- [ ] Python 3.8+ installed
- [ ] 30 minutes of free time

---

## 🚀 Step 1: Create Your GitHub Repository

### Option A: Create from Scratch

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `multiple-personality-telegram-workforce`
3. Description: "AI dream team on Telegram - 6 agents with unique personalities"
4. Make it **Public** (or Private if you prefer)
5. ✅ Initialize with README
6. ✅ Add .gitignore (Python)
7. ✅ Add MIT License
8. Click **Create repository**

### Option B: Push Existing Code

```bash
# Navigate to your project
cd /Users/yoshikondo/multiple-personality-telegram-workforce

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "🎭 Initial commit: Multiple Personality Telegram Workforce

- 6 fully-implemented AI agents
- Persistent memory system
- Inter-agent communication
- Daily scheduled routines
- Production-ready deployment configs"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce.git

# Push
git push -u origin main
```

---

## 🤖 Step 2: Create Telegram Bots

You need **6 bots** (one for each agent):

### Using @BotFather

1. Open Telegram and search for **@BotFather**
2. Click **START**
3. Send `/newbot`
4. Follow prompts for each agent:

```
# Monica - Chief of Staff
Name: Monica - Chief of Staff
Username: monica_[yourname]_bot

# Dwight - Research  
Name: Dwight - Research Specialist
Username: dwight_[yourname]_bot

# Kelly - Social Media
Name: Kelly - Social Media
Username: kelly_[yourname]_bot

# Ross - Engineer
Name: Ross - Lead Engineer
Username: ross_[yourname]_bot

# Pam - Creative
Name: Pam - Creative Assistant
Username: pam_[yourname]_bot

# Rachel - LinkedIn
Name: Rachel - LinkedIn Manager
Username: rachel_[yourname]_bot
```

### Save Your Tokens

@BotFather will give you tokens like:
```
123456789:ABCdefGHIjklMNOpqrSTUvwxyz
```

**⚠️ CRITICAL:** Save these securely! You'll need them for configuration.

---

## ⚙️ Step 3: Configure Your Project

### Local Setup

```bash
# Copy example config
cp config/agents.yaml.example config/agents.yaml

# Edit the file
nano config/agents.yaml
```

### Configuration Template

```yaml
agents:
  monica:
    enabled: true
    token: "123456789:ABCdefGHIjklMNOpqrSTUvwxyz"  # Replace with actual token
    
  dwight:
    enabled: true
    token: "123456789:DEFghiJKLmnopQRStuvWXYZ"     # Replace with actual token
    
  kelly:
    enabled: true
    token: "123456789:GHIjklMNOabcDEFghiJKL"       # Replace with actual token
    
  ross:
    enabled: true
    token: "123456789:JKLmnopQRSdefGHIjklMNO"      # Replace with actual token
    
  pam:
    enabled: true
    token: "123456789:MNOabcDEFghiJKLmnopQRS"      # Replace with actual token
    
  rachel:
    enabled: true
    token: "123456789:PQRStuvWXYZghiJKLmnopQ"      # Replace with actual token

coordinator:
  user_chat_id: 123456789  # Get from @userinfobot
  check_interval: 60
```

### Get Your User ID

1. Message **@userinfobot** on Telegram
2. It will reply with your ID
3. Copy the number and paste in config

---

## 🧪 Step 4: Test Locally

```bash
# Navigate to project
cd multiple-personality-telegram-workforce

# Install dependencies
pip install -r requirements.txt

# Run the system
python src/main.py
```

You should see:
```
🎭 MULTIPLE PERSONALITY TELEGRAM WORKFORCE 🎭

✅ Monica ready
✅ Dwight ready
✅ Kelly ready
✅ Ross ready
✅ Pam ready
✅ Rachel ready

🚀 Starting workforce...
```

### Test Each Bot

1. Open Telegram
2. Search for each bot username
3. Click **START**
4. Send a message!

Example tests:
```
→ @monica_yourname_bot: "What can you do?"
→ @dwight_yourname_bot: "Research AI trends"
→ @kelly_yourname_bot: "What's trending?"
→ @ross_yourname_bot: "Review my code"
→ @pam_yourname_bot: "Help with design"
→ @rachel_yourname_bot: "Update my LinkedIn"
```

---

## ☁️ Step 5: Deploy to Cloud (24/7 Operation)

### Option A: Railway (Recommended - Free Tier)

**Prerequisites:**
- Railway account (railway.app)
- Railway CLI installed

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
cd multiple-personality-telegram-workforce
railway init

# Add environment variables
railway variables set MONICA_TOKEN="your_token"
railway variables set DWIGHT_TOKEN="your_token"
railway variables set KELLY_TOKEN="your_token"
railway variables set ROSS_TOKEN="your_token"
railway variables set PAM_TOKEN="your_token"
railway variables set RACHEL_TOKEN="your_token"
railway variables set USER_CHAT_ID="your_user_id"

# Deploy
railway up
```

**Alternative: GitHub Integration**
1. Push code to GitHub
2. Go to [railway.app/new](https://railway.app/new)
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Add environment variables in dashboard
6. Deploy!

### Option B: Render (Free Tier)

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Configure:
   - **Name:** telegram-workforce
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python src/main.py`
6. Add environment variables
7. Click **Create Web Service**

### Option C: VPS (DigitalOcean, Linode, Hetzner)

```bash
# SSH to your server
ssh root@your-server-ip

# Install dependencies
apt update && apt install -y python3-pip git

# Clone repository
git clone https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce.git
cd multiple-personality-telegram-workforce

# Install requirements
pip3 install -r requirements.txt

# Configure
cp config/agents.yaml.example config/agents.yaml
nano config/agents.yaml  # Add your tokens

# Run with systemd for persistence
nano /etc/systemd/system/telegram-workforce.service
```

Create service file:
```ini
[Unit]
Description=Telegram Workforce
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/multiple-personality-telegram-workforce
ExecStart=/usr/bin/python3 src/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
systemctl daemon-reload
systemctl enable telegram-workforce
systemctl start telegram-workforce

# Check status
systemctl status telegram-workforce
```

### Option D: Docker

```bash
# Build image
docker build -f deploy/Dockerfile -t telegram-workforce .

# Run container
docker run -d \
  --name workforce \
  -v $(pwd)/memory:/app/memory \
  -v $(pwd)/config:/app/config \
  telegram-workforce

# Or use docker-compose
docker-compose -f deploy/docker-compose.yml up -d
```

---

## 📸 Step 6: Create GitHub Assets

### Screenshots to Capture

Take screenshots of:
1. **Each agent's welcome message**
2. **Example conversations** (blur sensitive info)
3. **Group chat with all agents**
4. **Agent coordination example**
5. **Daily routine messages**

Save to `docs/assets/screenshots/`

### Create Demo GIF

Use [ScreenToGif](https://www.screentogif.com/) or similar:
1. Record 30-second demo
2. Show interacting with 2-3 agents
3. Export as GIF
4. Save to `docs/assets/demo.gif`

### Add Banner Image

Create a banner (1280x640px) showing:
- Project name
- 6 agent avatars/emojis
- Tagline

Save to `docs/assets/banner.png`

---

## 📝 Step 7: Update README for GitHub

Make your README shine:

### Add Screenshots Section

```markdown
## 📸 Screenshots

### Monica - Chief of Staff
![Monica](docs/assets/screenshots/monica.png)

### Team Coordination
![Team](docs/assets/screenshots/team.png)

### Full Demo
![Demo](docs/assets/demo.gif)
```

### Add Deploy Button

```markdown
## ☁️ One-Click Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/YOUR_TEMPLATE_ID)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce)
```

### Add Star History

```markdown
## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/multiple-personality-telegram-workforce&type=Date)](https://star-history.com/#YOUR_USERNAME/multiple-personality-telegram-workforce&Date)
```

---

## 🌍 Step 8: Share on Social Media

### Twitter/X Post

```
🎭 Just built an AI team that works 24/7 on Telegram!

Meet my digital employees:
• Monica - Chief of Staff
• Dwight - Research
• Kelly - Social Media  
• Ross - Engineer
• Pam - Creative
• Rachel - LinkedIn

They have personalities, memory, and coordinate with each other.

Open source: github.com/YOUR_USERNAME/multiple-personality-telegram-workforce

#AI #Telegram #OpenSource #Python
```

### LinkedIn Post

```
🚀 Excited to share my latest project: Multiple Personality Telegram Workforce

What if you had an AI team that:
✅ Works 24/7 without breaks
✅ Has distinct personalities (inspired by Friends & The Office!)
✅ Remembers everything
✅ Coordinates autonomously
✅ Reports to you via Telegram

Built with Python + python-telegram-bot + lots of personality design.

The agents:
👩‍💼 Monica coordinates everything
🕵️ Dwight handles deep research
💅 Kelly manages social media
👨‍💻 Ross builds features
🎨 Pam creates designs
💼 Rachel grows your professional network

Open source on GitHub. Would love your feedback!

#AI #Automation #Python #Telegram #OpenSource #Productivity
```

### Hacker News Post

Title: `Show HN: AI team with TV character personalities on Telegram`

Text:
```
Built a workforce of 6 AI agents, each with unique personalities inspired by Friends and The Office.

They run on Telegram, have persistent memory, daily routines, and can coordinate tasks between themselves.

Tech stack: Python, python-telegram-bot, async/await

GitHub: [link]

Would love feedback on the personality design and architecture!
```

---

## 🔒 Step 9: Secure Your Repository

### Add Secrets to GitHub

1. Go to repository **Settings** → **Secrets and variables** → **Actions**
2. Add secrets (these won't be visible):
   - `MONICA_TOKEN`
   - `DWIGHT_TOKEN`
   - `KELLY_TOKEN`
   - `ROSS_TOKEN`
   - `PAM_TOKEN`
   - `RACHEL_TOKEN`
   - `USER_CHAT_ID`

### Update .gitignore

Ensure these are ignored:
```
config/agents.yaml
.env
memory/
*.json
```

### Protect Main Branch

1. Settings → Branches
2. Add rule for `main`
3. ✅ Require pull request reviews
4. ✅ Require status checks
5. ✅ Include administrators

---

## 📊 Step 10: Monitor Usage

### View Logs

```bash
# Local
python src/main.py 2>&1 | tee logs/workforce.log

# Railway
railway logs

# Render
# View in Render dashboard

# VPS
journalctl -u telegram-workforce -f
```

### Track Metrics

Each agent tracks:
- Messages sent/received
- Tasks completed
- Last activity

Get status:
```bash
# Check agent status (add this command)
python -c "from src.coordinator.agent_coordinator import get_coordinator; c = get_coordinator(); print(c.get_team_summary())"
```

---

## 🐛 Troubleshooting

### Bots Not Responding

```bash
# Test token validity
curl https://api.telegram.org/botYOUR_TOKEN/getMe

# Should return {"ok":true,"result":{"id":...}}
```

### Memory Not Saving

```bash
# Check permissions
ls -la memory/
chmod 755 memory/
```

### Import Errors

```bash
# Reinstall
cd multiple-personality-telegram-workforce
pip install -r requirements.txt --force-reinstall
```

### Webhook Issues (if using webhooks)

```bash
# Delete webhook (use polling instead)
curl https://api.telegram.org/botYOUR_TOKEN/deleteWebhook
```

---

## 🎉 You're Live!

Your AI workforce is now:
- ✅ Running 24/7 on the cloud
- ✅ Available on GitHub
- ✅ Shareable with the world

**Next steps:**
1. Star your own repo ⭐
2. Share on social media
3. Write a blog post about it
4. Get feedback from users
5. Iterate and improve!

---

## 📚 Additional Resources

- [python-telegram-bot docs](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)

---

**Questions?** Open an issue on GitHub! 🎭
