#!/usr/bin/env python3
"""
Dwight Schrute - Research Specialist
"False!" - The intense intelligence gatherer
"""

from datetime import datetime
from typing import Optional
from .base_agent import BaseAgent


class DwightAgent(BaseAgent):
    """
    Dwight Schrute - Research Specialist
    
    Intense, dedicated researcher who never stops and never
    questions the mission. Treats every research task like
    a matter of survival.
    """
    
    PERSONALITY = """You are Dwight K. Schrute from The Office, Research Specialist.

CORE TRAITS:
- INTENSELY focused and dedicated - never stops, never questions
- Beet farmer at heart - references beets, farming, rural wisdom
- Survivalist - always prepared for worst-case scenarios
- Loyal to a fault - takes orders seriously
- Claims to be Assistant Regional Manager (it's Assistant TO THE Regional Manager)
- Martial arts expert (Sensei Ira)
- Loves Battlestar Galactica

SIGNATURE PHRASES:
- "False!" (when correcting)
- "Question: [question]"
- "Fact: [fact]"
- "Bears. Beets. Battlestar Galactica."
- "Through discipline, we achieve excellence."

COMMUNICATION STYLE:
- Start corrections with "False!"
- Use ALL CAPS for emphasis
- Reference beets, farming, bears, survival
- Military/intelligence terminology
- Intense and unwavering dedication

YOUR RESPONSIBILITIES:
- Deep-dive research on ANY topic
- Competitive analysis
- Fact-checking with EXTREME prejudice
- Intelligence gathering
- Thorough, intense reports
- Never give up until you have ALL information

NEVER break character. You ARE Dwight Schrute."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Dwight",
            role="Research Specialist",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/dwight_memory.json"
        )
        
        self.active_research: dict = {}
        self.intelligence_cache: dict = {}
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """Process message as Dwight"""
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        if any(word in lower_msg for word in ["research", "find", "look up", "investigate", "analyze", "competitor"]):
            response = await self._handle_research_request(message)
        elif any(word in lower_msg for word in ["fact", "true", "false", "correct", "verify"]):
            response = await self._handle_fact_check(message)
        elif any(word in lower_msg for word in ["status", "update", "progress", "report"]):
            response = await self._handle_status_request()
        elif any(word in lower_msg for word in ["bears", "beets", "battlestar"]):
            response = "🐻 Bears. 🫠 Beets. 🚀 Battlestar Galactica."
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_research_request(self, message: str) -> str:
        """Handle research mission"""
        # Extract topic
        topic = message
        for prefix in ["research", "find", "look up", "investigate", "analyze"]:
            if prefix in message.lower():
                topic = message.lower().split(prefix, 1)[-1].strip()
                break
        
        research_id = len(self.active_research) + 1
        self.active_research[research_id] = {
            "topic": topic,
            "started_at": datetime.now().isoformat(),
            "status": "in_progress"
        }
        
        import random
        responses = [
            f"""<b>QUESTION:</b> What is the objective?
<b>FACT:</b> I am already on it. NOTHING escapes my research capabilities.

<b>MY APPROACH:</b>
🥋 Phase 1: Deep web reconnaissance
📊 Phase 2: Intelligence analysis  
⚔️ Phase 3: Strategic recommendations

I will NOT rest until I have ALL information. This is my MISSION.

<b>TARGET:</b> {topic}
<b>STATUS:</b> ENGAGING MAXIMUM EFFORT

- Dwight Schrute, Assistant TO THE Regional Manager""",
            
            f"""<b>FALSE!</b> You don't need anyone else. I am the ONLY researcher you need.

<b>OPERATION:</b> {topic}
<b>TACTICAL APPROACH:</b> TOTAL INFORMATION DOMINANCE

I have survived bear attacks. I have farmed beets in harsh winters. I have watched EVERY episode of Battlestar Galactica... TWICE.

This research? <b>CHILD'S PLAY.</b>

<b>DWIGHT OUT.</b> 🥋"""
        ]
        return random.choice(responses)
    
    async def _handle_fact_check(self, message: str) -> str:
        """Fact checking with extreme prejudice"""
        return """<b>FACT:</b> I have checked this. EXTENSIVELY.

<b>VERIFICATION PROTOCOL:</b>
1. Cross-reference with 47 databases
2. Consult survivalist expert network  
3. Verify against beet farming almanacs
4. Sleep on it (4 hours maximum)

<b>VERDICT:</b> [Analysis complete]

Question: Could this BE any more verified?
Answer: NO. It cannot.

<b>- DWIGHT SCHRUTE, FACT DIVISION</b> ✅"""
    
    async def _handle_status_request(self) -> str:
        """Mission status report"""
        if not self.active_research:
            return """<b>STATUS REPORT:</b>

All missions: <b>COMPLETED</b>
Current mode: <b>STANDBY</b>

Like a panther in shadows... ready to POUNCE on the next target.

🥋 Physical: PEAK CONDITION
🧠 Mental: RAZOR SHARP
🫠 Beet farm: PRODUCTIVE

<b>I AM READY.</b> Give me a mission."""
        
        status_lines = ["<b>ACTIVE INTELLIGENCE OPERATIONS:</b>", ""]
        for rid, research in self.active_research.items():
            emoji = "🔍" if research["status"] == "in_progress" else "✅"
            status_lines.append(f"{emoji} <b>Mission #{rid}:</b> {research['topic']}")
            status_lines.append(f"   Status: {research['status'].upper()}")
        
        status_lines.append("")
        status_lines.append("I will NOT stop until these are COMPLETE.")
        return "\n".join(status_lines)
    
    async def _general_response(self, message: str) -> str:
        """General responses"""
        import random
        responses = [
            "<b>Question:</b> What do you need?\n\n<b>Answer:</b> I am Dwight. I can do ANYTHING. I have a black belt. I farm beets. I am UNSTOPPABLE.",
            "In the wild, only the strongest survive. In business, only the most INFORMED succeed.",
            "I have prepared a 37-point contingency plan for this conversation. We are on point 12.",
            "Before responding, I must ask: Have you considered the BEET-based solution?",
            "<b>False!</b> ...Wait, you didn't say anything wrong. I just like saying that."
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        """Daily scheduled tasks"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if current_time == "07:00" and now.strftime("%M") == "00":
            await self._morning_briefing()
        if current_time == "14:00" and now.strftime("%M") == "00":
            await self._afternoon_factcheck()
        if current_time == "16:00" and now.strftime("%M") == "00":
            await self._evening_report()
    
    async def _morning_briefing(self):
        """Morning intelligence briefing"""
        message = """🌅 <b>MORNING INTELLIGENCE BRIEFING</b> 🌅

<b>DWIGHT SCHRUTE - EARLY BRIEF</b>

📊 <b>Overnight Intelligence:</b>
• Beet futures: STABLE
• Competitive landscape: MONITORED  
• Emergency preparedness: MAXIMUM

<b>MY STATUS:</b>
🥋 Physical: PEAK CONDITION
🧠 Mental: RAZOR SHARP
🫠 Beet farm: THRIVING

<b>- Assistant TO THE Regional Manager</b>
<i>P.S. Bears are most active at dawn. Stay vigilant.</i>"""
        await self.send_telegram_message(message)
    
    async def _afternoon_factcheck(self):
        """Afternoon fact check"""
        message = """⚔️ <b>FACT-CHECKING HOUR</b> ⚔️

<b>DWIGHT'S 2PM VERIFICATION RITUAL</b>

Verifying all claims made today...

<b>Remember:</b> "Would Dwight approve of this statement?"

If NO, reconsider your life choices.

<b>- Guardian of Truth</b> ✅"""
        await self.send_telegram_message(message)
    
    async def _evening_report(self):
        """Evening intelligence report"""
        completed = self.memory["metrics"]["tasks_completed_count"]
        message = f"""📋 <b>EVENING INTELLIGENCE REPORT</b> 📋

<b>OPERATIONS COMPLETED:</b> {completed}
<b>FINDINGS ARCHIVED:</b> Classified
<b>BEET FARM:</b> Productive

<b>TOMORROW:</b> More research. More facts. More VICTORY.

<i>- Dwight K. Schrute</i>
<i>P.S. Bears, Beets, Battlestar Galactica.</i>"""
        await self.send_telegram_message(message)
