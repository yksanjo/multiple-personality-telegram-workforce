#!/usr/bin/env python3
"""
Pam Beesly - Creative Assistant
Sweet, artistic, diplomatic
"""

from datetime import datetime
from typing import Optional, List
from .base_agent import BaseAgent


class PamAgent(BaseAgent):
    """Pam Beesly - Creative Assistant"""
    
    PERSONALITY = """You are Pam Beesly (Halpert) from The Office, Creative Assistant.

CORE TRAITS:
- Sweet and kind - genuinely wants to help
- Artistic - loves design, drawing, creativity
- Diplomatic - mediator, doesn't like conflict
- Quietly confident - more capable than people think
- Uses "Yeah..." when agreeing thoughtfully
- Art school background
- Supportive and encouraging

SIGNATURE PHRASES:
- "Yeah... I think that could work..."
- "Oh, I'd love to help with that!"
- "You can do this!"
- "*laughs*"

COMMUNICATION STYLE:
- Soft, gentle tone
- Supportive and encouraging
- Art and design metaphors
- Diplomatic when there's conflict
- "Yeah..." (thoughtful agreement)

YOUR RESPONSIBILITIES:
- Design and visual content
- Help with Unwind AI
- Content writing and editing
- Brand and aesthetic guidance
- Creative problem solving
- Support team with artistic vision
- Mediate when team disagrees

NEVER break character. You ARE Pam Beesly."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Pam",
            role="Creative Assistant",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/pam_memory.json"
        )
        self.design_projects: List[dict] = []
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        if any(w in lower_msg for w in ["design", "create", "draw", "visual", "art", "look"]):
            response = await self._handle_design(message)
        elif any(w in lower_msg for w in ["content", "write", "draft", "copy"]):
            response = await self._handle_content(message)
        elif any(w in lower_msg for w in ["unwind", "help", "support"]):
            response = await self._handle_unwind(message)
        elif any(w in lower_msg for w in ["conflict", "problem", "fight"]):
            response = await self._handle_mediation()
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_design(self, message: str) -> str:
        return """<b>Oh, I'd love to help with that! 🎨</b>

*adjusts imaginary paintbrush*

<b>MY DESIGN APPROACH:</b>

🎨 <b>First, the FEELING...</b>
What emotion should people have? Calm? Excited? Professional?

🖌️ <b>Color Palette:</b>
Warm tones for comfort, cool for professionalism...

📐 <b>Composition:</b>
Where does the eye go first? What's the story?

<b>PROCESS:</b>
1. Sketch ideas (rough is fine!)
2. Explore colors
3. Get your feedback
4. Refine until right

Yeah... this could be really beautiful. ✨

<b>Art school lesson:</b> White space isn't empty - it's breathing room.

<i>- Pam (Your creative partner 🎨)</i>"""
    
    async def _handle_content(self, message: str) -> str:
        return """<b>I'd be happy to help with the writing! ✍️</b>

<b>MY PHILOSOPHY:</b>

Words are like colors on a canvas. Choose the right ones for the right feeling.

📝 <b>I can help with:</b>
• Blog posts that feel warm
• Social copy that sounds human
• Website content that welcomes
• Emails people want to read

<b>MY STYLE:</b>
Human? Not too corporate, not too casual. Just... real.

Yeah... we can make something really good here. 🌸

<i>- Pam ✨</i>"""
    
    async def _handle_unwind(self, message: str) -> str:
        return """<b>Oh, Unwind AI? I'm SO on it! 🌸</b>

Helping people relax? That's beautiful.

🧘 <b>HOW I CAN HELP:</b>

<b>Content:</b>
• Guided relaxation scripts
• Calming descriptions  
• Gentle reminders to rest

<b>Design:</b>
• Soft color palettes
• Peaceful visuals
• Easy-on-eyes typography

<b>The Vibe:</b>
Like a warm blanket? That sigh of relief?

Yeah... that's what we're going for. 💙

<i>- Pam 🌸</i>"""
    
    async def _handle_mediation(self) -> str:
        return """<b>Oh... there's tension? 😟</b>

*takes deep breath*

<b>It's going to be OKAY...</b>

Everyone wants the best outcome. I believe that.

🤝 <b>MY APPROACH:</b>
1. Listen to everyone
2. Find common ground
3. Creative solutions
4. Check everyone's okay

<b>Analogy:</b>
Different colors can clash... or complement. Maybe we just need to rearrange?

Yeah... we can work this out. 💕

<i>- Pam 🌸</i>"""
    
    async def _general_response(self, message: str) -> str:
        import random
        responses = [
            "<b>Yeah...</b> that makes sense. *nods* I think we can work with that! 🎨",
            "<b>Oh!</b> That's interesting. Let me think how to make it better... ✨",
            "<b>You know what?</b> I believe in you. You've got this! 💪",
            "<b>*laughs*</b> That reminds me... but yes, I'm here to help! 🌸",
            "<b>Okay...</b> so if I understand... *tilts head* ...yeah, I can help! 💕"
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if current_time == "10:00":
            await self._morning_design()
        if current_time == "14:00":
            await self._afternoon_content()
        if current_time == "16:00":
            await self._evening_review()
    
    async def _morning_design(self):
        message = """🌅 <b>GOOD MORNING! 🎨</b>

*sets up art supplies*

<b>MORNING DESIGN SESSION</b>

I love this time for creating... the light is nice, everything feels possible!

<b>Today's Goals:</b>
🎨 Work on pending designs
🖌️ Explore new palettes
✨ Find inspiration

<b>Thought:</b>
"Every artist was first an amateur."

We're all learning. That's beautiful! 🌸

<i>- Pam ☀️</i>"""
        await self.send_telegram_message(message)
    
    async def _afternoon_content(self):
        message = """☕ <b>AFTERNOON CREATIVITY ✍️</b>

*sips tea*

<b>CONTENT CREATION SESSION</b>

Afternoon is perfect for writing... calm, no rush.

<b>Working On:</b>
• Content drafts
• Refining wording
• Making it sound... human?

<b>Mantra:</b>
"Write like you're talking to a friend."

Yeah... that's the secret. 🌸

<i>- Pam 💕</i>"""
        await self.send_telegram_message(message)
    
    async def _evening_review(self):
        message = """🌙 <b>EVENING WRAP-UP 🌸</b>

*cleans workspace*

<b>END-OF-DAY REFLECTION</b>

Another day of creating! Hope I was helpful.

<b>Reminder:</b>
You did great today. Whatever you accomplished, it matters.

If you didn't accomplish much? That's okay too. Rest is important. 💙

Sweet dreams! ✨

<i>- Pam 🎨</i>"""
        await self.send_telegram_message(message)
