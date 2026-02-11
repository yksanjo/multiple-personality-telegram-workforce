# 🎭 Multiple Personality Telegram Workforce

> **Your AI Dream Team on Telegram**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram)](https://core.telegram.org/bots)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

<p align="center">
  <img src="docs/assets/banner.png" alt="Multiple Personality Telegram Workforce" width="800">
</p>

Transform your productivity with a team of AI agents, each with distinct personalities inspired by beloved TV characters, working together through Telegram.

## 🎬 What Is This?

```
You: "Launch the new feature next week"

Monica (Chief of Staff): "OKAY! 📅 I'm ON it! Let me coordinate the team!"

├─ Dwight (Research): "I'll investigate competitors INTENSELY. 🕵️"
├─ Kelly (Social Media): "OMG I'm already thinking viral content! 💅"
├─ Ross (Engineer): "*adjusts glasses* I'll analyze the requirements... 👨‍💻"
├─ Pam (Creative): "I'd love to help with the designs! 🎨"
└─ Rachel (LinkedIn): "Professional announcement strategy coming! 💼"

[24 hours later]

Monica: "✅ MISSION ACCOMPLISHED! 
        • Dwight: 15-page competitor analysis
        • Kelly: 5 tweets + viral campaign ready
        • Ross: Deployment optimized, tests passing
        • Pam: Gorgeous graphics delivered
        • Rachel: LinkedIn strategy drafted
        
        Everything organized. Everything perfect. I KNOW! 💪"
```

## 🎭 Meet Your Team

| Agent | TV Character | Role | Personality | Best For |
|-------|--------------|------|-------------|----------|
| 👩‍💼 **Monica** | *Monica Geller* (Friends) | Chief of Staff | Organized, perfectionist, "I KNOW!" | Coordination, scheduling, team management |
| 🕵️ **Dwight** | *Dwight Schrute* (The Office) | Research Specialist | Intense, beet-loving, "False!" | Deep research, competitive analysis |
| 💅 **Kelly** | *Kelly Kapoor* (The Office) | Social Media Manager | Pop-culture obsessed, "OMG!" | Twitter/X, trends, viral content |
| 👨‍💻 **Ross** | *Ross Geller* (Friends) | Lead Engineer | Pedantic, dinosaur-loving, "Actually..." | Code, architecture, deployment |
| 🎨 **Pam** | *Pam Beesly* (The Office) | Creative Assistant | Sweet, artistic, diplomatic | Design, content, mediation |
| 💼 **Rachel** | *Rachel Green* (Friends) | LinkedIn Manager | Fashionable, ambitious, "No way!" | Professional networking, branding |

## ⚡ Quick Start

```bash
# 1. Clone & setup
git clone https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce.git
cd multiple-personality-telegram-workforce
./scripts/setup.sh

# 2. Create 6 bots via @BotFather (see below)

# 3. Add tokens to config/agents.yaml

# 4. Launch!
python src/main.py
```

**📖 [Detailed Setup Guide](docs/GITHUB_SETUP.md)** | **⚡ [5-Minute Quickstart](QUICKSTART.md)**

## 🚀 One-Click Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce)

## 🎯 Features

### 🧠 Persistent Memory
Each agent remembers:
- Past conversations
- Task history
- Your preferences
- Project context
- Team dynamics

```python
# Monica remembers you prefer mornings
Monica: "I scheduled it for 9am - I know you like mornings! 💪"

# Dwight recalls past research
Dwight: "As I discovered in my previous investigation..."
```

### 📅 Daily Routines

| Time | Agent | Activity |
|------|-------|----------|
| 07:00 | Dwight | Morning intelligence briefing 🕵️ |
| 08:00 | Monica | Team standup 📋 |
| 08:00 | Kelly | Trend check 📱 |
| 08:00 | Rachel | LinkedIn morning 💼 |
| 09:00 | Ross | GitHub review 💻 |
| 10:00 | Pam | Design session 🎨 |
| 17:00 | Monica | End-of-day summary ✅ |

### 🤝 Agent Coordination

Agents message each other automatically:

```
Monica → Ross: "Priority: Review new API"
Ross → Monica: "Done. Architecture is sound... I'm fine."
Monica → You: "✅ Ross approved the API!"
```

## 💬 How to Use

### Direct Messages

```
→ @monica_bot: "Schedule team sync Friday 2pm"
→ @dwight_bot: "Research AI competitors"  
→ @kelly_bot: "Draft tweets for launch"
→ @ross_bot: "Is deployment ready?"
→ @pam_bot: "Help with Unwind AI copy"
→ @rachel_bot: "Update my LinkedIn"
```

### Group Coordination

Create a Telegram group, add all bots:

```
You: @monica_bot launch next week

Monica: COORDINATION INITIATED! 🎯
Monica: @ross_bot - Technical check?
Ross: *adjusts glasses* Analyzing...
Monica: @kelly_bot - Social ready?
Kelly: OMG YES! 💅
```

## 🏗️ Architecture

```
User (Telegram)
    ↓
Agent Coordinator (Monica)
    ↓
┌─────────┬─────────┬─────────┐
│ Dwight  │  Kelly  │  Ross   │
│ Research│ Social  │ Engineer│
├─────────┼─────────┼─────────┤
│  Pam    │ Rachel  │  Shared │
│ Creative│LinkedIn │ Memory  │
└─────────┴─────────┴─────────┘
```

**[📐 Full Architecture Docs](docs/ARCHITECTURE.md)**

## 📁 Project Structure

```
multiple-personality-telegram-workforce/
├── 📂 src/
│   ├── 📂 agents/           # 6 agent personalities
│   ├── 📂 coordinator/      # Orchestration
│   └── main.py
├── 📂 deploy/               # Docker, Railway, Render
├── 📂 docs/                 # Documentation
├── 📂 config/               # Configuration
├── README.md
└── requirements.txt
```

## ☁️ Deployment Options

| Platform | Cost | Uptime | Setup |
|----------|------|--------|-------|
| **Local** | Free | While PC on | `python src/main.py` |
| **Railway** | Free tier | 24/7 | `railway up` |
| **Render** | Free tier | 24/7 | Dashboard |
| **VPS** | $5-10/mo | 24/7 | Docker |

### Railway (Recommended)

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### Docker

```bash
docker-compose -f deploy/docker-compose.yml up -d
```

**[📖 Full Deployment Guide](docs/GITHUB_SETUP.md#step-5-deploy-to-cloud)**

## 🎨 Customization

### Change Personalities

```python
# src/agents/monica.py
PERSONALITY = """You are [NEW CHARACTER]...

KEY TRAITS:
- Your custom traits

COMMUNICATION STYLE:
- How they speak
"""
```

### Add New Agents

1. Create `src/agents/new_agent.py`
2. Inherit from `BaseAgent`
3. Define personality
4. Register in coordinator

**[📋 Contributing Guide](CONTRIBUTING.md)**

## 📊 Example Workflows

### Product Launch
```
You → Monica: "Launch feature X Tuesday"
Monica coordinates:
├─ Dwight: Competitor analysis
├─ Ross: Prepare deployment  
├─ Pam: Launch graphics
├─ Kelly: Social campaign
└─ Rachel: LinkedIn strategy

Monica → You: "✅ All systems ready!"
```

### Crisis Response
```
You → Monica: "Bug in production!"
Monica → Ross: "PRIORITY BUG!"
Ross → Monica: "Fix deployed... I'm fine."
Monica → Kelly: "Draft incident comms"
Kelly → Monica: "Tweet thread ready!"
Monica → You: "🚨 RESOLVED! 12min downtime."
```

## 🧪 Testing

```bash
# Install dev dependencies
pip install pytest black flake8

# Run tests
pytest tests/

# Check style
flake8 src/
black --check src/
```

## 🤝 Contributing

We welcome contributions!

- 🐛 [Report bugs](../../issues)
- ✨ [Request features](../../discussions)
- 🎭 [Add new agents](CONTRIBUTING.md#adding-a-new-agent)
- 📚 [Improve docs](CONTRIBUTING.md)

**[📋 See Contributing Guide](CONTRIBUTING.md)**

## 🛡️ Security

- ✅ Bot tokens never committed
- ✅ Access restricted by chat ID
- ✅ No sensitive data in logs
- ✅ Memory files private

See [Security Policy](SECURITY.md)

## 📝 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Credits

- **Friends** (Monica, Ross, Rachel) - Characters
- **The Office US** (Dwight, Kelly, Pam) - Characters
- **python-telegram-bot** - Telegram library
- **Community** - Contributors like you!

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/multiple-personality-telegram-workforce&type=Date)](https://star-history.com/#YOUR_USERNAME/multiple-personality-telegram-workforce&Date)

---

<p align="center">
  <b>Built with 💙 by the community</b><br>
  <i>Your AI employees are waiting! 🎭</i><br><br>
  <a href="https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce/stargazers">⭐ Star us on GitHub</a> •
  <a href="https://twitter.com/intent/tweet?text=Check%20out%20this%20AI%20team%20on%20Telegram!">🐦 Share on Twitter</a> •
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce">💼 Share on LinkedIn</a>
</p>
