#!/bin/bash
# Deploy to Railway

echo "🚂 Deploying to Railway..."
echo "=========================="
echo ""

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found!"
    echo ""
    echo "Install it:"
    echo "   npm install -g @railway/cli"
    exit 1
fi

# Check if logged in
if ! railway whoami &> /dev/null; then
    echo "🔑 Please login to Railway first:"
    railway login
fi

# Initialize project if needed
if [ ! -f "railway.json" ]; then
    echo "📦 Initializing Railway project..."
    railway init
fi

echo ""
echo "⚙️  Setting up environment variables..."
echo ""

# Prompt for tokens
echo "Enter your bot tokens (get from @BotFather):"
read -p "Monica Token: " monica_token
read -p "Dwight Token: " dwight_token
read -p "Kelly Token: " kelly_token
read -p "Ross Token: " ross_token
read -p "Pam Token: " pam_token
read -p "Rachel Token: " rachel_token
read -p "Your Telegram User ID: " user_id

echo ""
echo "📝 Setting environment variables..."
railway variables set MONICA_TOKEN="$monica_token"
railway variables set DWIGHT_TOKEN="$dwight_token"
railway variables set KELLY_TOKEN="$kelly_token"
railway variables set ROSS_TOKEN="$ross_token"
railway variables set PAM_TOKEN="$pam_token"
railway variables set RACHEL_TOKEN="$rachel_token"
railway variables set USER_CHAT_ID="$user_id"

echo ""
echo "🚀 Deploying..."
railway up

echo ""
echo "✅ Deployed!"
echo ""
echo "View logs: railway logs"
echo "Open app:  railway open"
