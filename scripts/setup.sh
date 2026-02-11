#!/bin/bash
# Setup script for Multiple Personality Telegram Workforce

set -e

echo "🎭 Multiple Personality Telegram Workforce - Setup"
echo "=================================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Python 3.8+ required!"
    exit 1
fi
echo "   ✅ Python version OK"
echo ""

# Create directories
echo "📁 Creating directories..."
mkdir -p memory logs config
echo "   ✅ Directories created"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q python-telegram-bot==20.7 pyyaml aiohttp python-dotenv
echo "   ✅ Dependencies installed"
echo ""

# Create config if doesn't exist
if [ ! -f "config/agents.yaml" ]; then
    echo "⚙️  Creating configuration..."
    cat > config/agents.yaml << 'EOF'
# Agent Configuration
# Get tokens from @BotFather on Telegram

agents:
  monica:
    enabled: true
    token: ""  # Your Monica bot token here
    
  dwight:
    enabled: true
    token: ""  # Your Dwight bot token here
    
  kelly:
    enabled: true
    token: ""  # Your Kelly bot token here
    
  ross:
    enabled: true
    token: ""  # Your Ross bot token here
    
  pam:
    enabled: true
    token: ""  # Your Pam bot token here
    
  rachel:
    enabled: true
    token: ""  # Your Rachel bot token here

coordinator:
  user_chat_id: null  # Your Telegram user ID (get from @userinfobot)
  check_interval: 60  # seconds between scheduled checks
EOF
    echo "   ✅ Created config/agents.yaml"
else
    echo "   ⏭️  config/agents.yaml already exists"
fi
echo ""

# Test imports
echo "🧪 Testing imports..."
python3 -c "from src.agents import MonicaAgent, DwightAgent, KellyAgent, RossAgent, PamAgent, RachelAgent" 2>/dev/null && echo "   ✅ Agents import OK" || echo "   ⚠️  Import test failed (expected if running from wrong directory)"
echo ""

# Print next steps
echo "🎯 Next Steps:"
echo "=============="
echo ""
echo "1️⃣  Create 6 Telegram bots via @BotFather:"
echo "   • monica_[yourname]_bot"
echo "   • dwight_[yourname]_bot"
echo "   • kelly_[yourname]_bot"
echo "   • ross_[yourname]_bot"
echo "   • pam_[yourname]_bot"
echo "   • rachel_[yourname]_bot"
echo ""
echo "2️⃣  Edit config/agents.yaml and add your bot tokens"
echo ""
echo "3️⃣  Get your user ID from @userinfobot and add to config"
echo ""
echo "4️⃣  Run your workforce:"
echo "   python src/main.py"
echo ""
echo "📖 Full guide: docs/GITHUB_SETUP.md"
echo ""
echo "🎉 Setup complete!"
