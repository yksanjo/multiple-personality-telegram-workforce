# Contributing to Multiple Personality Telegram Workforce

First off, thank you for considering contributing! 🎉

## 🚀 Quick Start

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add amazing feature'`)
5. Push (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📋 Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/multiple-personality-telegram-workforce.git
cd multiple-personality-telegram-workforce

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Copy config
cp config/agents.yaml.example config/agents.yaml

# Run tests
pytest tests/
```

## 🎯 What to Contribute

### 🐛 Bug Fixes
- Fix personality inconsistencies
- Resolve memory issues
- Fix Telegram API edge cases

### ✨ New Features
- Add new agent personalities
- Integrate external APIs (GitHub, Twitter, etc.)
- Add voice/image support
- Create web dashboard

### 📚 Documentation
- Improve README
- Add more examples
- Write tutorials
- Translate to other languages

### 🧪 Testing
- Add unit tests
- Add integration tests
- Test on different platforms

## 🎭 Adding a New Agent

1. Create new file `src/agents/new_agent.py`:

```python
#!/usr/bin/env python3
"""
New Agent - Role Description
"""

from typing import Optional
from .base_agent import BaseAgent


class NewAgent(BaseAgent):
    """New agent with unique personality"""
    
    PERSONALITY = """You are [Character Name] from [Show/Movie].

CORE TRAITS:
- Trait 1
- Trait 2
- Trait 3

SIGNATURE PHRASES:
- "Phrase 1"
- "Phrase 2"

COMMUNICATION STYLE:
- How they speak
- What they emphasize

YOUR RESPONSIBILITIES:
- What they do
- How they help

NEVER break character."""

    def __init__(self, telegram_token: str, user_chat_id: Optional[int] = None):
        super().__init__(
            name="AgentName",
            role="Role Description",
            personality=self.PERSONALITY,
            telegram_token=telegram_token,
            user_chat_id=user_chat_id,
            memory_file="memory/agentname_memory.json"
        )
    
    async def process_message(self, message: str, from_user: str = "user") -> str:
        """Process message in character"""
        self.log_conversation("user", message)
        self.messages_received += 1
        
        # Add your logic here
        response = f"Your response in character to: {message}"
        
        self.log_conversation("assistant", response)
        await self.save_memory()
        return response
    
    async def run_scheduled_tasks(self):
        """Daily scheduled tasks"""
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        # Add scheduled tasks
        if current_time == "09:00":
            await self._morning_routine()
    
    async def _morning_routine(self):
        """Morning routine"""
        await self.send_telegram_message("Good morning! ☀️")
```

2. Register in `src/agents/__init__.py`:

```python
from .new_agent import NewAgent

__all__ = [
    # ... existing agents
    'NewAgent'
]
```

3. Add to coordinator in `src/coordinator/agent_coordinator.py`:

```python
from agents import NewAgent

agent_map = {
    # ... existing agents
    "newagent": NewAgent,
}
```

4. Update config example

5. Add tests

6. Update documentation

## 📝 Code Style

We use:
- **Black** for formatting
- **Flake8** for linting
- **Type hints** where possible

```bash
# Format code
black src/

# Check style
flake8 src/

# Run tests
pytest tests/
```

## 🧪 Testing

Write tests for:
- Agent responses
- Memory persistence
- Task management
- Coordinator functionality

Example test:

```python
# tests/test_agents.py
import pytest
from src.agents import MonicaAgent

@pytest.fixture
def monica():
    return MonicaAgent("fake_token", 123456)

@pytest.mark.asyncio
async def test_monica_scheduling(monica):
    response = await monica.process_message("Schedule a meeting")
    assert "schedule" in response.lower()
    assert "📅" in response
```

## 📸 Adding Screenshots

When adding features, include screenshots:

1. Take screenshot of Telegram conversation
2. Save to `docs/assets/screenshots/`
3. Reference in PR description
4. Update README if significant

## 🌟 Commit Message Convention

Use emoji prefixes:

- 🎭 `:performing_arts:` - New agent/personality
- ✨ `:sparkles:` - New feature
- 🐛 `:bug:` - Bug fix
- 📚 `:books:` - Documentation
- 💄 `:lipstick:` - UI/style changes
- ⚡ `:zap:` - Performance
- 🔒 `:lock:` - Security
- 🧪 `:test_tube:` - Tests

Examples:
```
🎭 Add Chandler Bing agent for sarcastic comments
✨ Add image generation support to Pam
🐛 Fix Monica's task tracking memory leak
📚 Add deployment guide for AWS
```

## 🏷️ Pull Request Process

1. **Title**: Clear description with emoji prefix
2. **Description**: What changed and why
3. **Screenshots**: If UI-related
4. **Tests**: Ensure they pass
5. **Documentation**: Update if needed

### PR Template

```markdown
## 🎯 What
Brief description of changes

## 📝 Why
Why these changes were made

## 📸 Screenshots
If applicable

## ✅ Checklist
- [ ] Code follows style guide
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Commit messages follow convention
```

## 🐛 Reporting Bugs

Use GitHub Issues with template:

```markdown
**Describe the bug**
Clear description

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen

**Screenshots**
If applicable

**Environment:**
- OS: [e.g. macOS]
- Python: [e.g. 3.11]
- Version: [e.g. 1.0.0]
```

## 💡 Feature Requests

Use GitHub Discussions or Issues:

```markdown
**Is your feature request related to a problem?**
Clear description

**Describe the solution you'd like**
What you want to happen

**Describe alternatives you've considered**
Other options

**Additional context**
Screenshots, examples, etc.
```

## 🎨 Personality Design Guidelines

When creating new agents:

1. **Be Consistent**: Stay in character always
2. **Be Distinct**: Clear personality differences
3. **Be Useful**: Practical role/function
4. **Be Memorable**: Catchphrases and quirks
5. **Be Respectful**: No offensive stereotypes

### Personality Template

```
Name: [Character Name]
From: [TV Show/Movie/Book]
Role: [Job function]

Traits (3-5):
- [Trait 1]
- [Trait 2]
- [Trait 3]

Catchphrases (2-3):
- "[Phrase 1]"
- "[Phrase 2]"

Communication style:
- [How they speak]
- [What words they use]
- [Tone/vibe]

Daily schedule:
- [Time]: [Activity]
```

## 🙏 Recognition

Contributors will be:
- Listed in README
- Mentioned in release notes
- Added to CONTRIBUTORS.md

## 📞 Questions?

- Open a GitHub Discussion
- Join our Discord (if available)
- Email: your-email@example.com

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

### Unacceptable Behavior

- Trolling or insulting comments
- Personal attacks
- Public or private harassment
- Publishing others' private information

## 🎉 Thank You!

Your contributions make this project better for everyone! 🎭

---

**Happy Contributing!** 🚀
