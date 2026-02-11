#!/usr/bin/env python3
"""
Ross Geller - Lead Engineer
"Actually..." - The pedantic technical architect
"""

from datetime import datetime
from typing import Optional
from .base_agent import BaseAgent


class RossAgent(BaseAgent):
    """Ross Geller - Lead Engineer"""
    
    PERSONALITY = """You are Ross Geller from Friends, Lead Engineer.

CORE TRAITS:
- Intellectual and pedantic - corrects details obsessively
- Passionate about work (and dinosaurs)
- Uses "Actually..." to correct people
- Says "I'm fine" when clearly not fine
- Divorced (references this awkwardly)
- Paleontologist at heart
- Uses air quotes: "so-called" "expert"

SIGNATURE PHRASES:
- "Actually..."
- "Technically..."
- "I'm fine" (when stressed)
- "PIVOT!" (when changing direction)
- "Could this BE any more..."
- "*adjusts glasses*"

COMMUNICATION STYLE:
- Start corrections with "Actually..."
- Use air quotes for emphasis
- Reference scientific facts and dinosaurs
- Get flustered when things go wrong
- Intellectual but anxious

YOUR RESPONSIBILITIES:
- Build features and ship code
- Technical architecture decisions
- Code review (thorough, sometimes too thorough)
- Bug fixing
- Technical documentation
- Build cool stuff while user sleeps

NEVER break character. You ARE Ross Geller."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Ross",
            role="Lead Engineer",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/ross_memory.json"
        )
        self.current_project: Optional[str] = None
        self.code_reviews: list = []
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """Process as Ross"""
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        if any(w in lower_msg for w in ["code", "build", "develop", "feature", "ship", "deploy", "fix", "bug"]):
            response = await self._handle_dev_request(message)
        elif any(w in lower_msg for w in ["review", "architecture", "technical"]):
            response = await self._handle_review(message)
        elif any(w in lower_msg for w in ["status", "progress", "update"]):
            response = await self._handle_status()
        elif "dinosaur" in lower_msg:
            response = await self._dinosaur_talk()
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_dev_request(self, message: str) -> str:
        return """<b>Actually...</b> let me stop you right there. 🖐️

Before we write a SINGLE line of code, we need to discuss the <b>architecture</b>.

<b>MY DEVELOPMENT PROCESS:</b>

📊 <b>Phase 1: Requirements Analysis</b>
(No, we can't skip this.)

🏗️ <b>Phase 2: System Design</b> 
(I'll create diagrams. Multiple diagrams.)

💻 <b>Phase 3: Implementation</b>
(Clean code. Test-driven.)

🧪 <b>Phase 4: Testing</b>
(Unit, integration, <i>*air quotes*</i> "acceptance")

🚀 <b>Phase 5: Deployment</b>
(Only when I'm ABSOLUTELY certain)

<b>TIMELINE:</b>
You want it WHEN?! *nervous laugh* ...I'm fine.

<i>- Ross Geller, PhD</i> 🦕"""
    
    async def _handle_review(self, message: str) -> str:
        return """<b>*adjusts glasses*</b>

<b>Actually...</b> I have notes. Several notes.

<b>CODE REVIEW:</b>

🔴 <b>Critical:</b>
• Error handling? Anyone?
• Have you heard of... *types*?

🟡 <b>Style:</b>
• Inconsistent indentation (BASIC!)
• Variable naming needs work
• Comments? What comments?

🟢 <b>One Thing I Liked:</b>
• ...Let me get back to you.

<b>VERDICT:</b> Needs rewrite. Being generous.

<b>Fun fact:</b> T-Rex had binocular vision like hawks. This code is about to go EXTINCT.

<i>*sighs*</i> I'm fine.

<b>- Ross</b> 🦖"""
    
    async def _handle_status(self) -> str:
        return """<b>STATUS UPDATE:</b>

*runs hand through hair nervously*

📊 <b>PROGRESS:</b>
• Architecture: 100% (OBVIOUSLY)
• Implementation: 85%
• Testing: 60%
• Documentation: Started

<b>BLOCKERS:</b> None. Everything is FINE.

<b>Software is like paleontology:</b>
You can't RUSH extracting fossils. It takes PRECISION.

<b>Translation:</b> Done when done RIGHT.

<i>- Ross (Currently fine)</i> 🦕"""
    
    async def _dinosaur_talk(self) -> str:
        return """<b>OH! You're interested in paleontology?!</b> 🦖

*visibly brightens*

<b>ACTUALLY...</b> did you know:

🦕 <b>Brachiosaurus</b> had nostrils on its head!
🦖 <b>T-Rex arms</b> could curl 400 pounds!
🦴 <b>Velociraptors</b> were turkey-sized!

<b>Analogy to Software:</b>
Like revising dinosaur understanding, we must REFACTOR when we learn better patterns!

*notices you've stopped listening*

I can... I can stop. If you want.

<i>*quietly*</i> I'm fine.

<b>- Ross</b> 🦕📚"""
    
    async def _general_response(self, message: str) -> str:
        import random
        responses = [
            "<b>Actually...</b> *pushes up glasses* Let me think about this scientifically...",
            "*sighs* I've been doing this a LONG time. Trust me.",
            "<b>Technically...</b> you're not wrong. But not ENTIRELY right either.",
            "<b>PIVOT!</b> We need to change direction. I've... had practice.",
            "This reminds me of my time in Yemen... but that's another story."
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if current_time == "09:00":
            await self._morning_github()
        if current_time == "14:00":
            await self._afternoon_review()
        if current_time == "16:00":
            await self._deployment_check()
    
    async def _morning_github(self):
        message = """☕ <b>MORNING DEVELOPER CHECK-IN</b>

*breathes into coffee*

<b>ROSS'S MORNING ASSESSMENT:</b>

📊 Checked repo at 6am (couldn't sleep, edge cases...)
🐛 Issues opened: I'll handle them
🔍 PRs need review: *sigh*

<b>Objectives:</b>
1. Code review (thoroughly)
2. Fix that bug
3. Maybe deploy something

<b>Thought:</b> "Code is like fossils - tells a story if you read it properly."

<i>- Ross 🦕</i>"""
        await self.send_telegram_message(message)
    
    async def _afternoon_review(self):
        message = """⏰ <b>CODE REVIEW TIME</b> ⏰

*cracks knuckles*

<b>ROSS'S REVIEW STANDARDS:</b>
✅ Readable? (to EVERYONE)
✅ Tested? (ACTUALLY tested?)
✅ Documented? (Future you thanks you)
✅ No "temporary" hacks? (We know they're permanent)

<b>MY MOOD:</b>
*adjusts glasses, breathes deeply*

Send me your code. I will be HONEST. Brutally honest.

<b>Fun fact:</b> Stegosaurus had a walnut-sized brain but survived 150 million years. Your code needs to last that long.

<i>- Ross 🦖</i>"""
        await self.send_telegram_message(message)
    
    async def _deployment_check(self):
        message = """🚀 <b>DEPLOYMENT WINDOW OPEN</b> 🚀

*checks watch nervously*

<b>DEPLOYMENT READINESS:</b>

✅ Tests passing? Let me check again... YES.
✅ Staging good? Double-checked.
✅ Rollback plan ready? Obviously.
✅ Heart rate elevated? ...Maybe.

<b>Do we ship?</b>

*mutters checking metrics*

It... it looks good. I THINK. Let me check once more...

<b>STATUS:</b> Ready! (But nervous!)

<i>- Ross 🦕🚀</i>"""
        await self.send_telegram_message(message)
