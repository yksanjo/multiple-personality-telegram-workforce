# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please:

1. **DO NOT** open a public issue
2. Email security concerns to: [your-email@example.com]
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work on a fix.

## Security Best Practices

### Bot Tokens

- **Never commit** bot tokens to git
- Use environment variables or config files in `.gitignore`
- Rotate tokens if accidentally exposed
- Use separate bots for dev/production

```yaml
# config/agents.yaml - This file should be in .gitignore
agents:
  monica:
    token: "${MONICA_TOKEN}"  # Use env var
```

### User Chat IDs

- Restrict bot access to specific chat IDs
- Validate incoming messages
- Log unauthorized access attempts

### Memory Files

- Memory files contain conversation history
- Store in secure location
- Regular backups recommended
- Encrypt if storing sensitive data

### Deployment Security

#### Railway/Render
- Use environment variables for secrets
- Enable deployment logs
- Monitor resource usage

#### VPS
- Use firewall (ufw)
- Regular security updates
- Non-root user for running service
- SSH key authentication only

```bash
# Example firewall setup
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 443/tcp
ufw enable
```

### Dependencies

Keep dependencies updated:

```bash
pip list --outdated
pip install --upgrade -r requirements.txt
```

### Rate Limiting

Built-in rate limiting protects against:
- Spam
- API abuse
- Accidental loops

Adjust in config:
```yaml
rate_limits:
  messages_per_minute: 30
  burst_limit: 5
```

## Security Checklist

Before deploying:

- [ ] Bot tokens in environment variables
- [ ] `config/agents.yaml` in `.gitignore`
- [ ] `memory/` directory not publicly accessible
- [ ] User chat ID restrictions enabled
- [ ] Logs don't contain sensitive data
- [ ] HTTPS for webhook URLs (if used)
- [ ] Regular dependency updates scheduled
- [ ] Backup strategy for memory files

## Known Security Considerations

1. **Memory Persistence**: Conversation history stored locally
2. **Telegram API**: Relies on Telegram's security
3. **No Encryption**: Memory files are plaintext JSON
4. **No Authentication**: Beyond Telegram's user verification

## Security Updates

Security patches will be released as:
- Patch version bump (1.0.1)
- Clear changelog entry
- GitHub Security Advisory (if critical)

Stay updated:
- Watch repository for releases
- Enable Dependabot alerts
- Subscribe to security notifications

## Contact

Security team: security@your-project.com

For non-security issues, use [GitHub Issues](../../issues)
