# ⚡ Quick Start Guide

Get your AI workforce running in **5 minutes**.

## Prerequisites

- Python 3.8+
- Telegram account
- 5 minutes

## Step 1: Install (1 minute)

```bash
git clone https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce.git
cd multiple-personality-telegram-workforce

# Or use the setup script
chmod +x scripts/setup.sh
./scripts/setup.sh
```

## Step 2: Create Bots (2 minutes)

1. Open Telegram, search for **@BotFather**
2. Send `/newbot` 6 times:

```
Name: Monica - Chief of Staff
Username: monica_[yourname]_bot

Name: Dwight - Research
Username: dwight_[yourname]_bot

Name: Kelly - Social Media
Username: kelly_[yourname]_bot

Name: Ross - Engineer
Username: ross_[yourname]_bot

Name: Pam - Creative
Username: pam_[yourname]_bot

Name: Rachel - LinkedIn
Username: rachel_[yourname]_bot
```

**Save all 6 tokens!**

## Step 3: Configure (1 minute)

```bash
# Edit config
cp config/agents.yaml.example config/agents.yaml
nano config/agents.yaml
```

Paste your tokens:
```yaml
agents:
  monica:
    enabled: true
    token: "123456789:ABC..."  # Your token
  # ... repeat for all 6
```

## Step 4: Run (1 minute)

```bash
python src/main.py
```

Done! 🎉 Your agents are now online.

## Test It

Message any bot:
```
→ @monica_yourname_bot: "What can you do?"
→ @dwight_yourname_bot: "Research AI trends"
→ @kelly_yourname_bot: "What's trending?"
```

## Deploy (Optional)

For 24/7 operation:

```bash
# Railway (Free)
railway login
railway init
railway up

# Or Docker
docker-compose -f deploy/docker-compose.yml up -d
```

## Next Steps

- [Full Setup Guide](docs/GITHUB_SETUP.md)
- [Architecture Docs](docs/ARCHITECTURE.md)
- [Personality Guide](docs/PERSONALITIES.md)

---

**Problems?** Open an issue on GitHub! 🎭
