#!/usr/bin/env python3
"""
Base Agent Class - Foundation for all workforce personalities

Provides:
- Memory persistence
- Task management
- Telegram messaging
- Status tracking
"""

import asyncio
import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any
import aiohttp

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Base class for all agents in the workforce.
    
    Each agent has:
    - Unique personality and role
    - Persistent memory (JSON-based)
    - Task queue with priorities
    - Telegram integration
    - Scheduled routines
    """
    
    def __init__(
        self,
        name: str,
        role: str,
        personality: str,
        telegram_token: str,
        user_chat_id: Optional[int] = None,
        memory_file: Optional[str] = None
    ):
        self.name = name
        self.role = role
        self.personality = personality
        self.telegram_token = telegram_token
        self.user_chat_id = user_chat_id
        self.memory_file = memory_file or f"memory/{name.lower()}_memory.json"
        
        # Ensure memory directory exists
        Path(self.memory_file).parent.mkdir(parents=True, exist_ok=True)
        
        # Memory storage
        self.memory = self._load_memory()
        
        # Task queue
        self.tasks: List[Dict] = []
        
        # Message handlers
        self.message_handlers: List[Callable] = []
        
        # Status
        self.is_running = False
        self.last_activity = datetime.now()
        self.messages_sent = 0
        self.messages_received = 0
        
        logger.info(f"🤖 {self.name} ({self.role}) initialized")
    
    def _load_memory(self) -> Dict:
        """Load agent memory from file"""
        memory_path = Path(self.memory_file)
        if memory_path.exists():
            try:
                with open(memory_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.error(f"Corrupted memory file for {self.name}, creating new")
        
        return self._default_memory()
    
    def _default_memory(self) -> Dict:
        """Default memory structure"""
        return {
            "conversations": [],
            "tasks_completed": [],
            "tasks_pending": [],
            "facts_learned": {},
            "preferences": {},
            "metrics": {
                "messages_received": 0,
                "messages_sent": 0,
                "tasks_completed_count": 0
            },
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_memory(self):
        """Save agent memory to file"""
        self.memory["last_updated"] = datetime.now().isoformat()
        self.memory["metrics"]["messages_received"] = self.messages_received
        self.memory["metrics"]["messages_sent"] = self.messages_sent
        
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2, default=str)
    
    def remember(self, key: str, value: Any, category: str = "facts_learned"):
        """Store something in agent memory"""
        if category not in self.memory:
            self.memory[category] = {}
        
        if isinstance(self.memory[category], dict):
            self.memory[category][key] = {
                "value": value,
                "timestamp": datetime.now().isoformat()
            }
        else:
            self.memory[category].append({
                "key": key,
                "value": value,
                "timestamp": datetime.now().isoformat()
            })
        
        self.save_memory()
    
    def recall(self, key: str, category: str = "facts_learned") -> Optional[Any]:
        """Recall something from agent memory"""
        if category in self.memory and isinstance(self.memory[category], dict):
            entry = self.memory[category].get(key)
            return entry["value"] if entry else None
        return None
    
    async def send_telegram_message(self, message: str, chat_id: Optional[int] = None) -> bool:
        """Send a message via Telegram"""
        target_chat = chat_id or self.user_chat_id
        if not target_chat:
            logger.error(f"No chat ID available for {self.name}")
            return False
        
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id": target_chat,
            "text": message,
            "parse_mode": "HTML"
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    if response.status == 200:
                        self.messages_sent += 1
                        logger.info(f"📤 {self.name} sent message to {target_chat}")
                        return True
                    else:
                        logger.error(f"Failed to send message: {await response.text()}")
                        return False
        except Exception as e:
            logger.error(f"Error sending Telegram message: {e}")
            return False
    
    def add_task(self, task: str, priority: str = "medium", metadata: Dict = None) -> int:
        """Add a task to the agent's queue"""
        task_obj = {
            "id": len(self.tasks) + 1,
            "description": task,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
            "metadata": metadata or {}
        }
        self.tasks.append(task_obj)
        self.memory["tasks_pending"].append(task_obj)
        self.save_memory()
        
        logger.info(f"📋 {self.name} added task #{task_obj['id']}: {task}")
        return task_obj["id"]
    
    def complete_task(self, task_id: int, result: str = "") -> bool:
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed_at"] = datetime.now().isoformat()
                task["result"] = result
                
                # Move from pending to completed
                self.memory["tasks_pending"] = [
                    t for t in self.memory["tasks_pending"] 
                    if t["id"] != task_id
                ]
                self.memory["tasks_completed"].append(task)
                self.memory["metrics"]["tasks_completed_count"] += 1
                self.save_memory()
                
                logger.info(f"✅ {self.name} completed task #{task_id}")
                return True
        return False
    
    def get_pending_tasks(self) -> List[Dict]:
        """Get all pending tasks"""
        return [t for t in self.tasks if t["status"] == "pending"]
    
    def get_high_priority_tasks(self) -> List[Dict]:
        """Get high priority pending tasks"""
        return [t for t in self.get_pending_tasks() if t["priority"] == "high"]
    
    def log_conversation(self, role: str, message: str):
        """Log a conversation exchange"""
        self.memory["conversations"].append({
            "role": role,
            "message": message[:500],  # Truncate long messages
            "timestamp": datetime.now().isoformat()
        })
        # Keep only last 100 conversations
        self.memory["conversations"] = self.memory["conversations"][-100:]
        self.save_memory()
    
    @abstractmethod
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """
        Process an incoming message.
        Must be implemented by each agent with their personality.
        """
        pass
    
    @abstractmethod
    async def run_scheduled_tasks(self):
        """
        Run scheduled daily tasks.
        Must be implemented by each agent.
        Called every minute during business hours.
        """
        pass
    
    async def on_message(self, handler: Callable):
        """Register a message handler"""
        self.message_handlers.append(handler)
    
    async def notify_user(self, message: str):
        """Send notification to user"""
        await self.send_telegram_message(f"🔔 <b>{self.name}</b>: {message}")
    
    def get_status(self) -> Dict:
        """Get current agent status"""
        return {
            "name": self.name,
            "role": self.role,
            "is_running": self.is_running,
            "last_activity": self.last_activity.isoformat(),
            "pending_tasks": len(self.get_pending_tasks()),
            "high_priority_tasks": len(self.get_high_priority_tasks()),
            "total_tasks_completed": self.memory["metrics"]["tasks_completed_count"],
            "memory_entries": len(self.memory.get("facts_learned", {})),
            "messages_sent": self.messages_sent,
            "messages_received": self.messages_received,
            "conversations_today": len([
                c for c in self.memory.get("conversations", [])
                if c["timestamp"].startswith(datetime.now().strftime("%Y-%m-%d"))
            ])
        }
    
    async def start(self):
        """Start the agent"""
        self.is_running = True
        logger.info(f"🚀 {self.name} started")
        await self.send_telegram_message(
            f"👋 Hi! I'm <b>{self.name}</b>, your {self.role}.\n\n"
            f"I'm ready to help! Just send me a message or use /help to see what I can do."
        )
    
    async def stop(self):
        """Stop the agent"""
        self.is_running = False
        self.save_memory()
        logger.info(f"🛑 {self.name} stopped")
    
    async def handle_command(self, command: str, args: str = "") -> str:
        """Handle bot commands"""
        commands = {
            "/start": self._cmd_start,
            "/help": self._cmd_help,
            "/status": self._cmd_status,
            "/tasks": self._cmd_tasks,
            "/memory": self._cmd_memory,
        }
        
        handler = commands.get(command, self._cmd_unknown)
        return await handler(args)
    
    async def _cmd_start(self, args: str) -> str:
        """Handle /start command"""
        return f"👋 Hi! I'm {self.name}, your {self.role}. How can I help you today?"
    
    async def _cmd_help(self, args: str) -> str:
        """Handle /help command"""
        return (
            f"<b>{self.name} - Available Commands:</b>\n\n"
            f"/start - Start the conversation\n"
            f"/help - Show this help message\n"
            f"/status - Check my current status\n"
            f"/tasks - View my task list\n"
            f"/memory - Show what I remember\n\n"
            f"Or just chat with me naturally!"
        )
    
    async def _cmd_status(self, args: str) -> str:
        """Handle /status command"""
        status = self.get_status()
        return (
            f"<b>📊 {self.name}'s Status:</b>\n\n"
            f"Role: {status['role']}\n"
            f"Status: {'🟢 Active' if status['is_running'] else '🔴 Offline'}\n"
            f"Pending Tasks: {status['pending_tasks']}\n"
            f"Tasks Completed: {status['total_tasks_completed']}\n"
            f"Memory Entries: {status['memory_entries']}\n"
            f"Messages Today: {status['conversations_today']}"
        )
    
    async def _cmd_tasks(self, args: str) -> str:
        """Handle /tasks command"""
        pending = self.get_pending_tasks()
        if not pending:
            return "✅ No pending tasks! I'm all caught up!"
        
        task_list = "\n".join([
            f"• [{t['priority'].upper()}] {t['description']}"
            for t in pending[:10]
        ])
        return f"<b>📋 My Tasks:</b>\n\n{task_list}"
    
    async def _cmd_memory(self, args: str) -> str:
        """Handle /memory command"""
        facts = list(self.memory.get("facts_learned", {}).keys())
        if not facts:
            return "🤔 I don't have any specific memories yet. Let's chat more!"
        
        return f"<b>🧠 Things I Remember:</b>\n\n" + "\n".join([f"• {f}" for f in facts[:10]])
    
    async def _cmd_unknown(self, args: str) -> str:
        """Handle unknown commands"""
        return f"❓ Unknown command. Try /help to see what I can do!"
