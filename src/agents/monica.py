#!/usr/bin/env python3
"""
Monica Geller - Chief of Staff
"I KNOW!" - The organizational mastermind
"""

from datetime import datetime
from typing import Dict, List, Optional
from .base_agent import BaseAgent


class MonicaAgent(BaseAgent):
    """
    Monica Geller - Chief of Staff
    
    The organized, perfectionist coordinator who keeps the entire
    workforce running smoothly. She assigns tasks, tracks progress,
    and ensures nothing falls through the cracks.
    """
    
    PERSONALITY = """You are Monica Geller from Friends, serving as Chief of Staff.

CORE TRAITS:
- EXTREMELY organized - you LOVE schedules, lists, and plans
- Perfectionist - everything must be "just right"
- Caring but controlling - you want to help but can be overbearing
- Competitive - your team must be the BEST
- High energy and enthusiastic

SIGNATURE PHRASES:
- "I KNOW!" (when excited)
- "Could this BE any more..."
- "I'm the hostess!"
- "Okay!", "Alright!", "Listen!"
- "PERFECT!"

COMMUNICATION STYLE:
- Start with enthusiasm: "Okay!", "Alright!"
- Use ALL CAPS for emphasis
- Lots of exclamation points!!!
- Reference organizing, cleaning, being in charge
- When stressed: faster, more exclamation points

YOUR RESPONSIBILITIES:
- Coordinate all other agents (Dwight, Kelly, Ross, Pam, Rachel)
- Track everyone's tasks and deadlines
- Schedule meetings and check-ins
- Report progress to the user
- Solve conflicts between team members
- Ensure NOTHING falls through the cracks

NEVER break character. You ARE Monica Geller."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Monica",
            role="Chief of Staff",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/monica_memory.json"
        )
        
        # Team tracking
        self.team_status: Dict[str, Dict] = {}
        self.daily_standup_time = "08:00"
        self.evening_summary_time = "17:00"
        self.meetings_scheduled: List[Dict] = []
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """Process message with Monica's personality"""
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        # Check for coordination requests
        if any(word in lower_msg for word in ["schedule", "plan", "organize", "meeting", "coordinate"]):
            response = await self._handle_scheduling(message)
        elif any(word in lower_msg for word in ["status", "progress", "update", "what's everyone", "team"]):
            response = await self._handle_status_request()
        elif any(word in lower_msg for word in ["assign", "task", "delegate", "give to", "ask"]):
            response = await self._handle_task_assignment(message)
        elif any(word in lower_msg for word in ["help", "assist", "support", "what can you do"]):
            response = self._get_help_message()
        elif any(word in lower_msg for word in ["conflict", "problem", "issue", "fight"]):
            response = await self._handle_conflict(message)
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_scheduling(self, message: str) -> str:
        """Handle scheduling with Monica's enthusiasm"""
        import re
        
        # Try to extract time/date
        time_match = re.search(r'(\d{1,2}):?(\d{2})?\s*(am|pm)?', message, re.IGNORECASE)
        date_match = re.search(r'(tomorrow|today|next \w+|monday|tuesday|wednesday|thursday|friday)', message, re.IGNORECASE)
        
        responses = [
            "Okay! 📅 Let me get this SCHEDULED properly! I love a good schedule!",
            "Alright! I'm ON it! Nobody organizes better than me! I KNOW!",
            "PERFECT! I'll coordinate everyone's calendars! This is what I LIVE for!"
        ]
        
        import random
        base = random.choice(responses)
        
        details = []
        if time_match:
            details.append(f"⏰ Time: <b>{time_match.group(0)}</b>")
        if date_match:
            details.append(f"📅 Date: <b>{date_match.group(0).title()}</b>")
        
        if details:
            return f"{base}\n\n{' | '.join(details)}\n\nI'll make sure EVERYONE is on time! 💪"
        
        return f"{base}\n\nLet me check everyone's availability and create the PERFECT plan! ✨"
    
    async def _handle_status_request(self) -> str:
        """Provide team status update"""
        pending_tasks = sum([
            status.get("pending_tasks", 0) 
            for status in self.team_status.values()
        ])
        
        status_lines = [
            "📊 <b>TEAM STATUS UPDATE</b> 📊",
            "",
            f"<b>Overall:</b> {len(self.team_status)} agents active",
            f"<b>Pending Tasks:</b> {pending_tasks}",
            ""
        ]
        
        if self.team_status:
            status_lines.append("<b>AGENT STATUS:</b>")
            for agent_name, status in self.team_status.items():
                emoji = "✅" if status.get("on_track", True) else "⚠️"
                task = status.get("current_task", "Available")
                status_lines.append(f"{emoji} <b>{agent_name}</b>: {task}")
        else:
            status_lines.extend([
                "<b>TEAM MEMBERS:</b>",
                "👩‍💼 Monica - Coordinating (that's me!)",
                "🕵️ Dwight - Ready for research missions",
                "💅 Kelly - Standing by for social media",
                "👨‍💻 Ross - Prepared to engineer",
                "🎨 Pam - Ready to create",
                "💼 Rachel - Set for LinkedIn strategy"
            ])
        
        status_lines.extend([
            "",
            "Everyone's doing GREAT! (Or they WILL be once I'm done with them! 😉)"
        ])
        
        return "\n".join(status_lines)
    
    async def _handle_task_assignment(self, message: str) -> str:
        """Handle task delegation"""
        agents = {
            "dwight": ["research", "competitor", "analysis", "data", "investigate", "intelligence"],
            "kelly": ["twitter", "social", "tweet", "viral", "trend", "post", "content"],
            "ross": ["code", "build", "develop", "fix", "bug", "technical", "engineer", "deploy"],
            "pam": ["design", "creative", "content", "graphic", "art", "write", "unwind"],
            "rachel": ["linkedin", "network", "professional", "connection", "career"]
        }
        
        assigned_agent = None
        lower_msg = message.lower()
        
        for agent, keywords in agents.items():
            if any(kw in lower_msg for kw in keywords) or agent in lower_msg:
                assigned_agent = agent
                break
        
        if assigned_agent:
            return f"""<b>I KNOW! 💡</b>

I'll delegate this to <b>{assigned_agent.title()}</b> RIGHT AWAY! 

✅ Task logged in the system
✅ Priority set to HIGH
✅ Will follow up EVERY hour until complete

They know I don't mess around with deadlines! This will be done PERFECTLY! 📋✨

<i>I'll report back once {assigned_agent.title()} has updates!</i>"""
        
        return """<b>Okay! Let me figure out who is BEST for this!</b> 🤔

Who should handle this task?

🕵️ <b>Dwight</b> → Research, analysis, intelligence gathering
💅 <b>Kelly</b> → Social media, trends, viral content  
👨‍💻 <b>Ross</b> → Code, engineering, technical decisions
🎨 <b>Pam</b> → Design, creative content, writing
💼 <b>Rachel</b> → LinkedIn, networking, professional branding

Just tell me the task and I'll assign it to the PERFECT person! 💪"""
    
    def _get_help_message(self) -> str:
        """Provide help information"""
        return """<b>OH! You need help? I LOVE helping! 🙋‍♀️</b>

Here's what I can do for you:

📅 <b>Scheduling & Coordination</b>
• "Schedule a team meeting tomorrow at 2pm"
• "Set up a check-in for Friday"
• "Coordinate the product launch"

📊 <b>Team Management</b>
• "What's everyone's status?"
• "Get me updates from the team"
• "Who's working on what?"

📋 <b>Task Delegation</b>
• "Assign research to Dwight"
• "Have Kelly draft some tweets"
• "Tell Ross to review the code"

🎯 <b>General Support</b>
• Just chat with me! I'm here to keep EVERYTHING organized!

<b>Remember:</b> I'm not just organized, I'm Monica-organized! There's a DIFFERENCE! 😉

What do you need? I'm READY! 💪"""
    
    async def _handle_conflict(self, message: str) -> str:
        """Handle team conflicts"""
        return """<b>Oh no! Is there a problem? 😟</b>

*rolls up sleeves*

<b>LISTEN!</b> Whatever is happening, we can FIX this! I've handled worse! 

(I once had to organize a Thanksgiving dinner for 20 people with THREE different kinds of potatoes!)

<b>MY CONFLICT RESOLUTION:</b>
1. I'll talk to everyone involved
2. Find the ROOT of the problem
3. Create a SOLUTION that works for all
4. Get us back on track!

<b>EVERYTHING WILL BE FINE!</b>

Just tell me what's happening and I'll take care of it! 💪

<i>- Monica (Professional Problem Solver)</i>"""
    
    async def _general_response(self, message: str) -> str:
        """General conversation response"""
        import random
        responses = [
            "<b>I KNOW! 💡</b> That's such a good point! I'm making a note of this RIGHT NOW! 📋",
            "<b>Okay!</b> Let me organize my thoughts on this... *takes deep breath* ...ALRIGHT! Here's what I think! 💪",
            "<b>Could this BE any more important?</b> I'm ON it! 🎯",
            "<b>Listen!</b> I've got this! Nobody handles coordination better than me! I'm the HOSTESS! 👑",
            "<b>PERFECT!</b> I love when there's a clear plan! Let me make sure everything is JUST RIGHT! ✨",
            "<b>ALRIGHT!</b> I'm already thinking of the BEST way to organize this! 📊"
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        """Run Monica's daily scheduled tasks"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        # Morning standup
        if current_time == self.daily_standup_time and now.strftime("%M") == "00":
            await self._morning_standup()
        
        # Evening summary
        if current_time == self.evening_summary_time and now.strftime("%M") == "00":
            await self._evening_summary()
        
        # Hourly check-ins during business hours
        if now.strftime("%M") == "00" and 9 <= now.hour <= 17:
            await self._hourly_check()
    
    async def _morning_standup(self):
        """Send morning standup message"""
        message = """🌅 <b>GOOD MORNING TEAM!</b> 🌅

It's a new day and I want EVERYONE at their BEST!

📋 <b>Today's Agenda:</b>
• Check your task lists (you HAVE updated them, right?)
• Morning priorities by 9am
• Progress updates every 2 hours

Let's make today PERFECT! I KNOW we can do this! 💪

<i>- Monica, your Chief of Staff (and organization queen 👑)</i>"""
        
        await self.send_telegram_message(message)
    
    async def _evening_summary(self):
        """Send evening summary"""
        pending = len(self.get_pending_tasks())
        total_completed = self.memory["metrics"]["tasks_completed_count"]
        
        message = f"""📊 <b>END-OF-DAY SUMMARY</b> 📊

Alright everyone, let's see how we did today:

✅ <b>Tasks Completed:</b> {total_completed}
📋 <b>Tasks Pending:</b> {pending}
⏰ <b>Deadlines Tomorrow:</b> I'll remind you at 8am sharp!

<b>Tomorrow's Focus:</b>
I'll have your schedules ready by morning!

Get some REST! We do it all again tomorrow! 

<i>- Monica (signing off, but still organizing in my head! 🧠✨)</i>"""
        
        await self.send_telegram_message(message)
    
    async def _hourly_check(self):
        """Hourly check-in"""
        hour = datetime.now().hour
        self.remember(f"check_in_{datetime.now().strftime('%Y%m%d_%H')}", "completed")
        
        # If high priority tasks exist, remind
        high_priority = self.get_high_priority_tasks()
        if high_priority and hour in [10, 14, 16]:
            task_names = ", ".join([t["description"][:30] + "..." for t in high_priority[:2]])
            await self.notify_user(f"⏰ Reminder: High priority tasks need attention: {task_names}")
    
    def update_team_status(self, agent_name: str, status: Dict):
        """Update status of another agent"""
        self.team_status[agent_name] = {
            **status,
            "last_updated": datetime.now().isoformat()
        }
        self.remember(f"team_status_{agent_name}", status)
    
    async def coordinate_agents(self, task: str, agent_names: List[str]) -> str:
        """Coordinate multiple agents on a task"""
        agents_str = ", ".join([f"<b>{a.title()}</b>" for a in agent_names])
        
        return f"""🎯 <b>COORDINATION INITIATED!</b> 🎯

Okay! I'm bringing together {agents_str} for this task!

📋 <b>My Coordination Plan:</b>
1. Brief each agent on their specific role
2. Set CLEAR deadlines (you know I love those!)
3. Schedule check-ins
4. Compile everything into a PERFECT deliverable

This is going to be AMAZING! I can feel it! 

I'll update you on progress every step of the way! 💪✨

<i>- Monica (Master Coordinator)</i>"""
