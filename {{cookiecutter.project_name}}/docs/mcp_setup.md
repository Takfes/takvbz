# MCP (Model Context Protocol) Setup Guide

This project includes configuration for MCP servers that enhance AI development tools like GitHub Copilot with additional capabilities.

## What is MCP?

Model Context Protocol (MCP) allows AI coding assistants to access external tools and data sources securely. The included configuration provides:

- **Time**: Current time and date information
- **Filesystem**: Safe file system operations within project boundaries
- **Sequential Thinking**: Advanced reasoning capabilities
- **Git**: Git repository operations and history
- **GitHub**: GitHub API integration for issues, PRs, and repository data
- **Context7**: Up-to-date library documentation
- **Brave Search**: Web search capabilities

## Prerequisites

### Node.js (Required for most servers)
Most MCP servers require Node.js. Install it from [nodejs.org](https://nodejs.org/) or using a package manager:

```bash
# macOS with Homebrew
brew install node

# Ubuntu/Debian
sudo apt install nodejs npm

# Windows with Chocolatey
choco install nodejs
```

Verify installation:
```bash
node --version
npm --version
```

## Setup Instructions

### 1. Environment Variables (Optional but Recommended)

Some MCP servers work better with API credentials:

1. Copy the environment template:
   ```bash
   cp .env.template .env
   ```

2. Edit `.env` with your actual credentials:
   ```bash
   # Edit with your preferred editor
   code .env  # VS Code
   nano .env  # Terminal editor
   ```

3. Fill in the credentials you want to use:

#### GitHub Personal Access Token
- Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
- Click "Generate new token (classic)"
- Select scopes: `repo`, `read:user`
- Copy the token to your `.env` file

#### Brave Search API Key
- Visit [Brave Search API](https://api.search.brave.com/app/keys)
- Sign up and get your API key
- Copy to your `.env` file

#### Context7 API Key
- Visit [Context7](https://context7.ai) for documentation access
- Follow their API key generation process
- Copy to your `.env` file

### 2. VS Code Configuration

The MCP configuration is automatically available in VS Code through the `.vscode/settings.json` file. No additional setup needed.

### 3. Verify Setup

After setup, your AI coding assistant should have access to the additional capabilities. You can test by asking questions like:

- "What's the current time?"
- "Show me the recent git commits"  
- "Search for information about Python async programming"
- "What files are in the src directory?"

## Troubleshooting

### Node.js Not Found
If you see errors about `npx` or Node.js:
1. Ensure Node.js is installed and in your PATH
2. Restart VS Code after installing Node.js
3. Try running `node --version` in your terminal

### MCP Servers Not Loading
1. Check VS Code Developer Console (Help → Toggle Developer Tools)
2. Look for MCP-related error messages
3. Verify your `.env` file has correct credentials (if using)
4. Ensure file permissions allow execution

### Credential Issues
- MCP servers work without credentials but with limited functionality
- Double-check API key format and validity
- Ensure `.env` file is in the project root
- Verify environment variable names match exactly
- For more info, refer to the [credentials guide](mcp_credentials.md).

### Performance Issues
If MCP servers are slow:
1. Check your internet connection
2. Some servers cache data - performance improves over time
3. Consider disabling unused servers by modifying `mcp.json`

## Security Notes

- The `.env` file is git-ignored to prevent credential exposure
- Never commit API keys to version control
- Use tokens with minimal required permissions
- Regularly rotate API keys for security

## Customization

You can modify `mcp.json` to:
- Disable servers you don't need
- Add additional MCP servers
- Change server configurations
- Adjust file system access paths (for security)

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-mcp)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)