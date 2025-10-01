# MCP (Model Context Protocol) Integration

The template includes optional MCP (Model Context Protocol) integration for enhanced AI-assisted development capabilities.

## What is MCP?

Model Context Protocol allows AI coding assistants like GitHub Copilot to access external tools and data sources securely. This provides your development environment with enhanced capabilities:

- **Filesystem Operations**: Safe file system operations within project boundaries
- **Git Integration**: Git repository operations and history
- **GitHub API**: Issues, PRs, and repository data
- **Web Search**: Real-time information via Brave Search
- **Documentation**: Up-to-date library documentation via Context7
- **Advanced Reasoning**: Sequential thinking capabilities

## Enabling MCP

When prompted during project generation:

```
include_mcp_config [y]:
```

Select `y` to include MCP configuration in your project.

## What Gets Generated

When MCP is enabled, the template creates:

1. **`.vscode/mcp.json`**: MCP server configuration
2. **`.env.template`**: Template for API credentials
3. **`docs/mcp_setup.md`**: Comprehensive setup guide

## MCP Servers Included

| Server | Purpose | Node.js Required | Credentials Required |
|--------|---------|------------------|---------------------|
| time | Current time/date | ❌ | ❌ |
| filesystem | File operations | ✅ | ❌ |
| sequentialthinking | Advanced reasoning | ✅ | ❌ |
| git | Git operations | ✅ | ❌ |
| github | GitHub API | ✅ | ✅ (Personal Access Token) |
| context7 | Library docs | ❌ | ✅ (API key) |
| braveSearch | Web search | ✅ | ✅ (API key) |

## Prerequisites

- **Node.js**: Required for most MCP servers (5 out of 7)
- **API Keys**: Optional but recommended for full functionality
- **VS Code**: MCP configuration is VS Code-specific

## Post-Generation Setup

After generating your project with MCP enabled:

1. **Check Node.js availability**: The post-generation hook will warn if Node.js is not detected
2. **Copy environment template**: `cp .env.template .env`
3. **Add API credentials**: Edit `.env` with your keys (optional)
4. **Follow detailed guide**: See `docs/mcp_setup.md` in your generated project

## Security Considerations

- ✅ No credentials in template files
- ✅ Environment variables via `.env` (git-ignored)
- ✅ Clear setup instructions
- ✅ Optional credentials (servers work with degraded functionality)

## Disabling MCP

Simply select `n` when prompted for `include_mcp_config`. All MCP-related files will be excluded from your project.

## Learn More

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- Generated project includes detailed setup guide in `docs/mcp_setup.md`
