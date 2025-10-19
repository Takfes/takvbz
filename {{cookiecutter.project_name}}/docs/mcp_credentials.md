There are **two alternative approaches** for handling **secrets in MCP** (Model Context Protocol) server configurations.

## The Two Approaches
### 1. Input-based approach (Interactive Prompt)

```json
"env": {
  "BRAVE_API_KEY": "${input:brave_api_key}"
}
```

This references the input defined in the inputs section:


```json
{
  "id": "brave_api_key",
  "type": "promptString", 
  "description": "Brave API key (optional, required for brave-search server)",
  "password": true
}
```

**How it works:**

When the MCP server starts, VS Code will prompt you to enter the API key
The password: true field makes the input field masked (like a password field)
The key is stored temporarily in memory for that session
You'll be prompted again each time you restart VS Code or reload the MCP servers

### 2. Environment variable approach

```json
"env": {
  "BRAVE_API_KEY": "${env:BRAVE_API_KEY}"
}
```

**How it works:**

Reads the API key from your system's environment variables
You need to set BRAVE_API_KEY in your shell profile (.zshrc, .bashrc, .env, etc.)
More persistent - no need to re-enter the key each session
More secure for production environments