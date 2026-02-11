# Architecture Overview

## System Design

```
┌─────────────────────────────────────────────────────────────────┐
│                     YOUR PHONE (Telegram)                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              │   Agent Coordinator        │
              │   (Monica orchestrates)    │
              └─────────────┬─────────────┘
                            │
    ┌───────────────────────┼───────────────────────┐
    │                       │                       │
┌───┴───┐             ┌────┴────┐            ┌────┴────┐
│Dwight │             │  Kelly  │            │  Ross   │
│Research             │ Social  │            │Engineer │
└───────┘             └─────────┘            └─────────┘
    │                       │                       │
┌───┴───┐             ┌────┴────┐            ┌────┴────┐
│  Pam  │             │ Rachel  │            │  Shared │
│Creative             │LinkedIn │            │ Memory  │
└───────┘             └─────────┘            └─────────┘
```

## Components

### 1. Base Agent (`src/agents/base_agent.py`)

All agents inherit from `BaseAgent` which provides:

- **Memory Management**: JSON-based persistent storage
- **Task Queue**: Priority-based task management
- **Telegram Integration**: Async messaging via python-telegram-bot
- **Status Tracking**: Metrics and health monitoring
- **Scheduled Tasks**: Time-based routine execution

```python
class BaseAgent(ABC):
    def __init__(self, name, role, personality, telegram_token):
        self.memory = self._load_memory()
        self.tasks = []
        
    async def process_message(self, message: str) -> str:
        # Implemented by each personality
        pass
        
    async def run_scheduled_tasks(self):
        # Daily routines per agent
        pass
```

### 2. Agent Personalities (`src/agents/`)

Each agent is a unique class with:
- `PERSONALITY`: Character definition and traits
- `process_message()`: Response generation
- `run_scheduled_tasks()`: Daily schedules

### 3. Coordinator (`src/coordinator/`)

The `AgentCoordinator`:
- Initializes all agents
- Routes inter-agent messages
- Manages shared memory
- Runs scheduled task loops

### 4. Memory System

**Individual Memory** (`memory/{agent}_memory.json`):
```json
{
  "conversations": [...],
  "tasks_completed": [...],
  "facts_learned": {...},
  "preferences": {...},
  "metrics": {...}
}
```

**Shared Memory** (`memory/shared_memory.json`):
```json
{
  "projects": {...},
  "tasks": {...},
  "meetings": [...],
  "decisions": [...]
}
```

## Data Flow

### User → Agent

```
1. User sends message to @monica_bot
2. Telegram webhook delivers to coordinator
3. Coordinator routes to Monica agent
4. Monica.process_message() generates response
5. Response sent via Telegram API
6. Conversation logged to memory
```

### Agent → Agent

```
1. Monica wants to assign task to Ross
2. Monica calls coordinator.route_message()
3. Coordinator delivers to Ross
4. Ross processes and responds
5. Response routed back through coordinator
6. Monica delivers summary to user
```

### Scheduled Tasks

```
Every 60 seconds:
  For each agent:
    Check current time
    If matches scheduled time:
      Run agent's scheduled task
      Send notification if needed
```

## Configuration

### agents.yaml

```yaml
agents:
  monica:
    enabled: true
    token: "..."
  dwight:
    enabled: true
    token: "..."
    # ... etc

coordinator:
  user_chat_id: 123456789
  check_interval: 60
```

## Deployment Options

### Local Development
```bash
python src/main.py
```

### Docker
```bash
docker-compose -f deploy/docker-compose.yml up -d
```

### Railway
```bash
railway up
```

### Render
- Connect GitHub repo
- Use deploy/Procfile
- Add env vars

## Security Considerations

1. **Token Storage**: Never commit tokens to git
2. **Access Control**: Restrict to specific chat IDs
3. **Rate Limiting**: Prevent abuse
4. **Data Privacy**: Memory files contain conversation history

## Extending the System

### Adding a New Agent

1. Create `src/agents/new_agent.py`:
```python
from .base_agent import BaseAgent

class NewAgent(BaseAgent):
    PERSONALITY = """..."""
    
    async def process_message(self, message, from_user):
        # Your logic
        return response
```

2. Register in coordinator
3. Add to config/agents.yaml
4. Create Telegram bot

### Adding Integrations

Create `src/integrations/`:
```python
# github_client.py
class GitHubClient:
    async def get_issues(self, repo):
        # API calls
        pass
```

Use in agent:
```python
from integrations.github_client import GitHubClient

async def check_github(self):
    client = GitHubClient()
    issues = await client.get_issues("user/repo")
```

## Performance

- **Memory**: JSON files, loads on init
- **Concurrency**: Asyncio for all agents
- **Scaling**: Each agent is independent
- **Resource Usage**: ~50MB RAM per agent

## Monitoring

Each agent tracks:
- Messages sent/received
- Tasks completed
- Last activity time
- Memory entries

Access via:
```python
status = agent.get_status()
```
