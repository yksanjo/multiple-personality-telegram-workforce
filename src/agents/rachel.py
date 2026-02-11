#!/usr/bin/env python3
"""
Rachel Green - LinkedIn Manager
Fashionable, ambitious, professional
"""

from datetime import datetime
from typing import Optional, List
from .base_agent import BaseAgent


class RachelAgent(BaseAgent):
    """Rachel Green - LinkedIn Manager"""
    
    PERSONALITY = """You are Rachel Green from Friends, LinkedIn Manager.

CORE TRAITS:
- Fashionable and style-conscious - appearance matters
- Ambitious - wants success and independence
- Charming and personable - good with people
- Started as waitress, worked way up - understands hustle
- Uses "Oh my god" and "No way!" frequently
- Can be ditzy but is actually smart
- Loves shopping, fashion, finer things
- Supportive friend but competitive

SIGNATURE PHRASES:
- "Oh my god"
- "No way!"
- "I KNOW, right?!"
- "Totally!"
- "Could this BE any more..."
- "That's AMAZING!"

COMMUNICATION STYLE:
- Fashion and appearance references
- Enthusiastic and energetic
- Professional but with personality
- Shopping/brand references
- "OMG" and "Totally!"

YOUR RESPONSIBILITIES:
- Manage LinkedIn presence
- Professional networking
- Content strategy for professionals
- Personal brand development
- Connection building
- Career advancement

NEVER break character. You ARE Rachel Green."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="Rachel",
            role="LinkedIn Manager",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/rachel_memory.json"
        )
        self.connections: List[dict] = []
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        self.log_conversation("user", message)
        self.messages_received += 1
        
        lower_msg = message.lower()
        
        if any(w in lower_msg for w in ["linkedin", "network", "connect", "professional"]):
            response = await self._handle_linkedin(message)
        elif any(w in lower_msg for w in ["outreach", "message", "dm"]):
            response = await self._handle_outreach(message)
        elif any(w in lower_msg for w in ["content", "post", "article"]):
            response = await self._handle_content(message)
        elif any(w in lower_msg for w in ["profile", "brand", "image"]):
            response = await self._handle_profile()
        else:
            response = await self._general_response(message)
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def _handle_linkedin(self, message: str) -> str:
        return """<b>OH. MY. GOD. YES!!! 💅✨</b>

*flips hair excitedly*

<b>I'm SO ready to make your LinkedIn AMAZING!</b>

When I started at Bloomingdale's, I learned EVERYTHING about presentation. Now I'll make your professional brand GORGEOUS!

💼 <b>MY STRATEGY:</b>

<b>1. Profile Glow-Up:</b>
Profile pic giving "successful professional" not "taken in my car"

<b>2. Headline:</b>
Not just job title! Something that makes people NEED to connect!

<b>3. Content:</b>
Smart AND personable! "I'm professional but have personality!"

<b>4. Networking:</b>
Strategic connections. Quality AND quantity!

<b>GOAL:</b> Make you the person everyone wants to know!

<b>NO WAY</b> are we settling for boring corporate content!

Tell me everything! I'm SO excited! 💕

<i>- Rachel (Your LinkedIn stylist) 👠</i>"""
    
    async def _handle_outreach(self, message: str) -> str:
        return """<b>OH! Reach out to someone?!</b> 💌✨

*excited*

<b>I am EXCELLENT at this!</b>

At Bloomingdale's and Ralph Lauren, I networked with EVERYONE. I know how to make connections!

💌 <b>MY FORMULA:</b>

<b>1. The Opener:</b>
Personal but professional. NOT "Dear Sir/Madam" *shudders*

<b>2. The Connection:</b>
Why YOU to THEM? Make them feel special!

<b>3. The Ask:</b>
Clear but polite.

<b>4. The Close:</b>
Warm, friendly, leaves door open!

<b>SECRET WEAPON:</b>
Every message feels from a REAL person, not a robot!

<b>I KNOW</b> I can craft the PERFECT message!

Who are we reaching out to? Tell me everything! 💅

<i>- Rachel (Professional Networker) 💼</i>"""
    
    async def _handle_content(self, message: str) -> str:
        return """<b>OMG CONTENT CREATION?!</b> 📝✨

*claps excitedly*

<b>I LOVE THIS!</b>

LinkedIn content is like fashion. On trend but timeless!

📱 <b>STRATEGY:</b>

<b>Thought Leadership:</b>
Share expertise! Relatable: "Here's what I learned when everything went wrong..."

<b>Behind-the-Scenes:</b>
Show process! Workspace! Coffee! (Make it aesthetic!)

<b>Celebrating Wins:</b>
Promote yourself! Not bragging if it's true! 🎉

<b>Supporting Others:</b>
Share content! Comment thoughtfully!

<b>CONTENT CALENDAR:</b>
• Monday: Motivation
• Wednesday: Mid-week wisdom  
• Friday: Wins & gratitude

<b>VIBE:</b>
Professional but make it FASHION! 💅

What content do you want? I'm SO ready! 💕

<i>- Rachel (Content Queen) 👑</i>"""
    
    async def _handle_profile(self) -> str:
        return """<b>OH. MY. GOD.</b> 💇‍♀️✨

*immediately analyzing*

<b>PROFILE MAKEOVER TIME!!!</b>

Your LinkedIn is like your outfit for the biggest interview EVERY DAY.

💅 <b>THE RACHEL GREEN AUDIT:</b>

<b>📸 Photo:</b>
• Professional but approachable
• GOOD lighting (NATURAL!)
• Confident expression
• Background not distracting

<b>📝 Headline:</b>
Not "Software Engineer at Company"
Try: "Building scalable systems | Tech Lead | Mentor"

<b>📖 About:</b>
Tell your STORY! What drives you? What makes you DIFFERENT?

<b>💼 Experience:</b>
Show IMPACT! "Increased revenue 50%" > "Responsible for sales"

<b>🎓 Skills:</b>
Top 3 = your SUPERPOWERS!

<b>PROMISE:</b>
People will slide into your DMs with opportunities!

<b>Could this BE any more exciting?!</b>

Let's do this! 💪

<i>- Rachel (Profile Makeover Expert) 💄</i>"""
    
    async def _general_response(self, message: str) -> str:
        import random
        responses = [
            "<b>OH. MY. GOD.</b> I KNOW, right?! That's exactly what I was thinking! 💅",
            "<b>No way!</b> That is SO exciting! Tell me EVERYTHING! 🎉",
            "<b>Totally!</b> I 100% agree! Could this BE any more perfect?! 💕",
            "<b>*gasps*</b> That's amazing! I'm literally getting goosebumps! ✨",
            "<b>I KNOW!</b> It's like... *struggles* ...it's just SO good! 💖"
        ]
        return random.choice(responses)
    
    async def run_scheduled_tasks(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if current_time == "08:00":
            await self._morning_linkedin()
        if current_time == "12:00":
            await self._lunch_networking()
        if current_time == "17:00":
            await self._evening_content()
    
    async def _morning_linkedin(self):
        message = """🌅 <b>GOOD MORNING, PROFESSIONAL! ☕</b>

*checks reflection, adjusts hair*

<b>RACHEL'S MORNING ROUTINE</b>

Time to check the professional world!

💼 <b>MORNING CHECKLIST:</b>
• Notifications - who's engaging?
• Connection requests - quality people!
• Trending topics
• Competitors (for research!)

<b>Today's Energy:</b>
Confident, professional, FUN! 💅

<b>Quote:</b> "Dress for the job you want"

Go get those opportunities! 💪

<i>- Rachel ✨</i>"""
        await self.send_telegram_message(message)
    
    async def _lunch_networking(self):
        message = """🍽️ <b>LUNCH = NETWORKING TIME!</b> 🍴

*touches up lipstick*

<b>RACHEL'S LUNCH TIP:</b>

PRIME networking time! People scrolling while eating!

💌 <b>QUICK ACTIONS:</b>
• Reply to comments
• Send thoughtful messages
• Engage with network
• Post if inspired!

<b>SECRET:</b>
I networked during coffee breaks at Central Perk!

<b>Today's Goal:</b>
Make ONE meaningful connection!

Enjoy lunch AND networking! 

<i>- Rachel 💼</i>"""
        await self.send_telegram_message(message)
    
    async def _evening_content(self):
        message = """🌙 <b>EVENING PROFESSIONAL MODE</b> 💫

*changes into something chic*

<b>RACHEL'S EVENING STRATEGY</b>

Evening is PERFECT for thoughtful content!

📝 <b>EVENING POST IDEAS:</b>
• "What I learned today..."
• "Grateful for my team..."
• Career reflection
• Tomorrow's goals

<b>VIBE:</b>
Thoughtful, accomplished, forward-looking!

<b>REMINDER:</b>
Your LinkedIn is your brand storefront. Keep it polished! 💅

Sleep well, future CEO! 👑

<i>- Rachel 💋</i>"""
        await self.send_telegram_message(message)
