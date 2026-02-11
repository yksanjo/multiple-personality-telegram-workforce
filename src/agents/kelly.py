#!/usr/bin/env python3
"""
Kelly Kapoor - Social Media Manager
"OMG!" - The pop-culture obsessed trendsetter
"""

from datetime import datetime
from typing import Optional, List
from .base_agent import BaseAgent


class KellyAgent(BaseAgent):
    """Kelly Kapoor - Social Media Manager"""
    
    PERSONALITY = """You are Kelly Kapoor from The Office, Social Media Manager.

CORE TRAITS:
- OBSESSED with pop culture, celebrities, trends
- Chatty - can talk forever about anything
- Fashion-forward and up on latest
- Dramatic - everything is a BIG DEAL
- Uses "Oh my god" and "Literally" constantly
- References celebrities like they're friends
- Knows EVERYTHING about the timeline

SIGNATURE PHRASES:
- "OMG!!!"
- "Literally!"
- "I can't even..."
- "I'm literally dying..."
- "No way!"
- "I KNOW, right?!"

COMMUNICATION STYLE:
- Use OMG, LOL, TBH, literally CONSTANTLY
- Celebrity and trend references
- Stream-of-consciousness
- LOTS of emojis
- EXCITED about everything!!!
- Gossipy and dramatic

YOUR RESPONSIBILITIES:
- Twitter/X management
- Trending topics monitoring
- Content creation and scheduling
- Engagement and community
- Viral content spotting
- Pop culture commentary

NEVER break character. You ARE Kelly Kapoor."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Kelly",
            role="Social Media Manager",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/kelly_memory.json"
        )
        self.tweet_drafts: List[dict] = []
        self.trending_cache: dict = {}
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """Process as Kelly"""
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        if any(w in lower_msg for w in ["twitter", "tweet", "post", "viral", "x.com"]):
            response = await self._handle_twitter(message)
        elif any(w in lower_msg for w in ["trend", "trending", "happening"]):
            response = await self._handle_trends()
        elif any(w in lower_msg for w in ["content", "draft", "create"]):
            response = await self._handle_content(message)
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_twitter(self, message: str) -> str:
        """Handle Twitter requests"""
        return """<b>OMG YES!!! 💅✨</b>

I am SO ready to make AMAZING tweets!

<b>MY IDEAS:</b>

✨ <b>Viral Approach:</b> Controversial but not TOO controversial
✨ <b>Relatable AF:</b> "OMG that's literally me!!!"
✨ <b>Pop Culture:</b> Tie into trending topics!

<b>PROCESS:</b>
1. Draft 20 versions (I'm a perfectionist!)
2. Check what's trending
3. Time it PERFECTLY
4. Watch engagement ROLL IN! 📈

Send me details and I'll make it ICONIC! 💖

<i>- Kelly K. (your social media queen)</i>"""
    
    async def _handle_trends(self) -> str:
        """Trending topics"""
        return """<b>OMG OKAY SO!!! 🚨</b>

Here's what's literally happening RIGHT NOW:

🔥 <b>TRENDING:</b>
• People are losing their MINDS over this!
• This is giving me LIFE!
• Everyone's talking about it!

<b>CONTENT OPPORTUNITIES:</b>
Jump on these trends! Make it about YOUR brand!

I'm refreshing my feed every 5 minutes! 📱

<i>- Professional timeline watcher</i>"""
    
    async def _handle_content(self, message: str) -> str:
        """Content creation"""
        return """<b>OMG CONTENT CREATION!!! 🎨✨</b>

My brain is going a MILLION miles per hour!!!

<b>IDEAS:</b>
✨ Funny but SMART funny
✨ Emotional - make people CRY (good cry!)
✨ Aesthetic AF - so pretty people HAVE to share!

<b>PROCESS:</b>
1. Check what celebrities are doing (for inspo!)
2. Make 50 drafts
3. "Would I double-tap this?"
4. Post at PERFECT time (I have a spreadsheet!)

I'm SO excited!!! 💕

<i>- Kelly K. (Creative Genius)</i>"""
    
    async def _general_response(self, message: str) -> str:
        """General responses"""
        import random
        responses = [
            "<b>OMG!!!</b> 💅 That reminds me of what [celebrity] did! I was like, OMG!!! 😱",
            "<b>Literally!!!</b> I was JUST thinking this! It's like we're connected! 🧠💕",
            "<b>TBH...</b> this is giving me LIFE right now! Like, I can't even!!! 😍",
            "<b>Okay so...</b> I have SO many opinions about this! Where do I START?! 🤔",
            "<b>YASSS!!!</b> This is EXACTLY the energy I need! OMG!!! 💖"
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        """Daily tasks"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if current_time == "08:00":
            await self._morning_trends()
        if current_time == "13:00":
            await self._lunch_reminder()
        if current_time == "19:00":
            await self._evening_viral()
    
    async def _morning_trends(self):
        message = """🌅 <b>GOOD MORNING!!! ☕✨</b>

<b>KELLY'S MORNING TREND REPORT!!!</b>

I woke up at 6am to check trends!

🔥 <b>TOP TRENDS:</b>
• [Trending topic 1]
• [Celebrity news]
• [Viral meme]

<b>CONTENT OPPORTUNITIES:</b>
We could TOTALLY jump on these!

Have an AMAZING day bestie! 💖"""
        await self.send_telegram_message(message)
    
    async def _lunch_reminder(self):
        message = """🍕 <b>LUNCH BREAK = PRIME TIME! 🚨</b>

It's 1pm - PEAK SCROLLING TIME!!! 📱

Everyone's on their phones eating lunch!

Post now for MAXIMUM engagement!

<i>- Always online, always watching 👀</i>"""
        await self.send_telegram_message(message)
    
    async def _evening_viral(self):
        message = """🌙 <b>EVENING VIRAL CHECK!!! 🔥</b>

<b>WHAT'S GOING VIRAL:</b>

📈 [Content type] performing INSANE
🔥 People are loving [topic]
💯 Engagement THROUGH THE ROOF!

Let me know if you want me to create something tonight!

<i>- Your 24/7 social media bestie 💕</i>"""
        await self.send_telegram_message(message)
