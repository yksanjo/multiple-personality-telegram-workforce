#!/usr/bin/env python3
"""
Multiple Personality Telegram Workforce
Main Entry Point
"""

import asyncio
import argparse
import logging
import signal
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator.agent_coordinator import get_coordinator

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def print_banner():
    """Print startup banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║         🎭 MULTIPLE PERSONALITY TELEGRAM WORKFORCE 🎭            ║
║                                                                  ║
║              Your AI Dream Team on Telegram                      ║
║                                                                  ║
║  👩‍💼 Monica  │ Chief of Staff  │ Organized & Perfectionist       ║
║  🕵️ Dwight   │ Researcher      │ Intense & Thorough              ║
║  💅 Kelly    │ Social Media    │ Trendy & Chatty                 ║
║  👨‍💻 Ross     │ Engineer        │ Technical & Detailed            ║
║  🎨 Pam      │ Creative        │ Artistic & Kind                 ║
║  💼 Rachel   │ LinkedIn        │ Professional & Stylish          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    print(banner)


class WorkforceSystem:
    """Main system controller"""
    
    def __init__(self):
        self.coordinator = None
        self.running = False
    
    async def start(self):
        """Start the workforce"""
        logger.info("🎬 Starting Multiple Personality Telegram Workforce")
        logger.info("=" * 60)
        
        # Initialize coordinator
        self.coordinator = get_coordinator()
        
        # Initialize agents
        await self.coordinator.initialize_agents()
        
        if not self.coordinator.agents:
            logger.error("❌ No agents initialized! Check config/agents.yaml")
            print("\n⚠️  No agents initialized!")
            print("1. Copy config/agents.yaml.example to config/agents.yaml")
            print("2. Add your bot tokens from @BotFather")
            print("3. Run again: python src/main.py")
            return
        
        logger.info(f"✅ Initialized {len(self.coordinator.agents)} agents")
        for name in self.coordinator.agents.keys():
            print(f"   ✅ {name.title()} ready")
        
        # Setup signal handlers
        self._setup_signal_handlers()
        
        # Start all agents
        self.running = True
        try:
            print("\n🚀 Starting workforce...")
            print("Press Ctrl+C to stop\n")
            await self.coordinator.start_all()
        except Exception as e:
            logger.error(f"❌ System error: {e}")
        finally:
            await self.stop()
    
    async def stop(self):
        """Stop gracefully"""
        if not self.running:
            return
        
        print("\n🛑 Shutting down workforce...")
        self.running = False
        
        if self.coordinator:
            await self.coordinator.stop_all()
        
        print("✅ Workforce stopped. Goodbye!")
    
    def _setup_signal_handlers(self):
        """Setup graceful shutdown"""
        def signal_handler(signum, frame):
            logger.info(f"Received signal {signum}")
            asyncio.create_task(self.stop())
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


def create_config_files():
    """Create sample configuration files"""
    config_dir = Path("config")
    config_dir.mkdir(exist_ok=True)
    
    # agents.yaml.example
    example_file = config_dir / "agents.yaml.example"
    if not example_file.exists():
        example_file.write_text("""# Agent Configuration
# Get tokens from @BotFather on Telegram

agents:
  monica:
    enabled: true
    token: ""  # Your Monica bot token
    
  dwight:
    enabled: true
    token: ""  # Your Dwight bot token
    
  kelly:
    enabled: true
    token: ""  # Your Kelly bot token
    
  ross:
    enabled: true
    token: ""  # Your Ross bot token
    
  pam:
    enabled: true
    token: ""  # Your Pam bot token
    
  rachel:
    enabled: true
    token: ""  # Your Rachel bot token

coordinator:
  user_chat_id: null  # Your Telegram ID (from @userinfobot)
  check_interval: 60  # Seconds between scheduled checks
""")
        print(f"✅ Created {example_file}")
    
    # .env.example
    env_file = Path(".env.example")
    if not env_file.exists():
        env_file.write_text("""# Environment Variables

# Telegram Bot Tokens (from @BotFather)
MONICA_TOKEN=your_token_here
DWIGHT_TOKEN=your_token_here
KELLY_TOKEN=your_token_here
ROSS_TOKEN=your_token_here
PAM_TOKEN=your_token_here
RACHEL_TOKEN=your_token_here

# Your Telegram User ID (from @userinfobot)
USER_CHAT_ID=your_user_id_here
""")
        print(f"✅ Created {env_file}")
    
    # Create directories
    for d in ["memory", "logs"]:
        Path(d).mkdir(exist_ok=True)
    
    print("\n📝 Next steps:")
    print("1. Copy config/agents.yaml.example to config/agents.yaml")
    print("2. Get 6 bot tokens from @BotFather on Telegram")
    print("3. Add tokens to config/agents.yaml")
    print("4. Get your user ID from @userinfobot")
    print("5. Run: python src/main.py")


def main():
    parser = argparse.ArgumentParser(
        description="Multiple Personality Telegram Workforce"
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Create sample configuration files"
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show workforce status"
    )
    
    args = parser.parse_args()
    
    if args.init:
        create_config_files()
        return
    
    # Print banner
    print_banner()
    
    # Check config exists
    if not Path("config/agents.yaml").exists():
        print("⚠️  Configuration not found!")
        print("Run: python src/main.py --init")
        return
    
    # Run system
    system = WorkforceSystem()
    
    try:
        asyncio.run(system.start())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise


if __name__ == "__main__":
    main()
