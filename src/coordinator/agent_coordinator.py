#!/usr/bin/env python3
"""
Agent Coordinator - Central orchestration for the workforce
Monica serves as the primary coordinator
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Import agents
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import MonicaAgent, DwightAgent, KellyAgent, RossAgent, PamAgent, RachelAgent

logger = logging.getLogger(__name__)


class AgentCoordinator:
    """Coordinates all agents and manages inter-agent communication"""
    
    def __init__(self, config_path: str = "config/agents.yaml"):
        self.config = self._load_config(config_path)
        self.agents: Dict[str, any] = {}
        self.is_running = False
        self.message_queue: asyncio.Queue = asyncio.Queue()
        
        # Shared memory
        self.shared_memory_path = Path("memory/shared_memory.json")
        self.shared_memory_path.parent.mkdir(parents=True, exist_ok=True)
        self.shared_memory = self._load_shared_memory()
        
        logger.info("🎭 Agent Coordinator initialized")
    
    def _load_config(self, config_path: str) -> Dict:
        """Load agent configuration"""
        try:
            import yaml
            config_file = Path(config_path)
            if config_file.exists():
                with open(config_file, 'r') as f:
                    return yaml.safe_load(f)
        except ImportError:
            logger.warning("PyYAML not installed, using default config")
        except Exception as e:
            logger.error(f"Error loading config: {e}")
        
        return self._default_config()
    
    def _default_config(self) -> Dict:
        """Default configuration"""
        return {
            "agents": {
                "monica": {"enabled": True, "token": ""},
                "dwight": {"enabled": True, "token": ""},
                "kelly": {"enabled": True, "token": ""},
                "ross": {"enabled": True, "token": ""},
                "pam": {"enabled": True, "token": ""},
                "rachel": {"enabled": True, "token": ""}
            },
            "coordinator": {
                "user_chat_id": None,
                "check_interval": 60
            }
        }
    
    def _load_shared_memory(self) -> Dict:
        """Load shared memory between agents"""
        if self.shared_memory_path.exists():
            try:
                with open(self.shared_memory_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        
        return {
            "projects": {},
            "tasks": {},
            "meetings": [],
            "decisions": [],
            "user_preferences": {},
            "created_at": datetime.now().isoformat()
        }
    
    def save_shared_memory(self):
        """Save shared memory"""
        with open(self.shared_memory_path, 'w') as f:
            json.dump(self.shared_memory, f, indent=2, default=str)
    
    async def initialize_agents(self):
        """Initialize all enabled agents"""
        user_chat_id = self.config.get("coordinator", {}).get("user_chat_id")
        
        agent_map = {
            "monica": MonicaAgent,
            "dwight": DwightAgent,
            "kelly": KellyAgent,
            "ross": RossAgent,
            "pam": PamAgent,
            "rachel": RachelAgent
        }
        
        for agent_name, agent_class in agent_map.items():
            agent_config = self.config.get("agents", {}).get(agent_name, {})
            
            if not agent_config.get("enabled", True):
                logger.info(f"⏭️  {agent_name.title()} is disabled")
                continue
            
            token = agent_config.get("token", "")
            if not token:
                logger.warning(f"⚠️  No token for {agent_name}, skipping")
                continue
            
            try:
                agent = agent_class(
                    telegram_token=token,
                    user_chat_id=user_chat_id
                )
                self.agents[agent_name] = agent
                logger.info(f"✅ {agent_name.title()} initialized")
            except Exception as e:
                logger.error(f"❌ Failed to initialize {agent_name}: {e}")
    
    async def start_all(self):
        """Start all agents"""
        self.is_running = True
        
        # Start each agent
        for name, agent in self.agents.items():
            try:
                await agent.start()
                logger.info(f"🚀 {name.title()} started")
            except Exception as e:
                logger.error(f"❌ Failed to start {name}: {e}")
        
        # Send welcome message from Monica if available
        if "monica" in self.agents:
            await self.agents["monica"].send_telegram_message(
                "🎭 <b>WORKFORCE ONLINE!</b>\n\n"
                "All agents are now active and ready to work!\n\n"
                "📋 <b>Team Status:</b>\n" +
                "\n".join([f"✅ {name.title()} - Ready" for name in self.agents.keys()])
            )
        
        # Start coordination tasks
        await asyncio.gather(
            self._scheduled_tasks_loop(),
            self._message_processor_loop()
        )
    
    async def stop_all(self):
        """Stop all agents"""
        self.is_running = False
        
        for name, agent in self.agents.items():
            try:
                await agent.stop()
                logger.info(f"🛑 {name.title()} stopped")
            except Exception as e:
                logger.error(f"❌ Error stopping {name}: {e}")
        
        self.save_shared_memory()
    
    async def _scheduled_tasks_loop(self):
        """Run scheduled tasks for all agents"""
        while self.is_running:
            try:
                for name, agent in self.agents.items():
                    try:
                        await agent.run_scheduled_tasks()
                    except Exception as e:
                        logger.error(f"❌ Scheduled task error for {name}: {e}")
                
                await asyncio.sleep(self.config.get("coordinator", {}).get("check_interval", 60))
            except Exception as e:
                logger.error(f"❌ Scheduled tasks loop error: {e}")
                await asyncio.sleep(60)
    
    async def _message_processor_loop(self):
        """Process inter-agent messages"""
        while self.is_running:
            try:
                message = await asyncio.wait_for(
                    self.message_queue.get(),
                    timeout=1.0
                )
                await self._route_message(message)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logger.error(f"❌ Message processor error: {e}")
    
    async def _route_message(self, message: Dict):
        """Route message between agents"""
        from_agent = message.get("from")
        to_agent = message.get("to")
        content = message.get("content")
        
        if to_agent == "user":
            if "monica" in self.agents:
                await self.agents["monica"].send_telegram_message(content)
        elif to_agent in self.agents:
            await self.agents[to_agent].process_message(
                f"Message from {from_agent}: {content}"
            )
        elif to_agent == "all":
            for name, agent in self.agents.items():
                if name != from_agent:
                    await agent.send_telegram_message(
                        f"📢 Message from {from_agent}: {content}"
                    )
    
    def get_agent_status(self) -> Dict:
        """Get status of all agents"""
        return {
            name: agent.get_status()
            for name, agent in self.agents.items()
        }
    
    def get_team_summary(self) -> str:
        """Get formatted team summary"""
        status = self.get_agent_status()
        lines = ["📊 <b>TEAM WORKFORCE SUMMARY</b>\n"]
        
        for name, info in status.items():
            emoji = "🟢" if info["is_running"] else "🔴"
            lines.append(
                f"{emoji} <b>{name.title()}</b> - {info['role']}\n"
                f"   Tasks: {info['pending_tasks']} pending, "
                f"{info['total_tasks_completed']} completed\n"
                f"   Messages: {info['messages_received']} in, "
                f"{info['messages_sent']} out\n"
            )
        
        return "\n".join(lines)


coordinator: Optional[AgentCoordinator] = None


def get_coordinator(config_path: str = "config/agents.yaml") -> AgentCoordinator:
    """Get or create coordinator singleton"""
    global coordinator
    if coordinator is None:
        coordinator = AgentCoordinator(config_path)
    return coordinator
