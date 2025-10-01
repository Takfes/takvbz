# VS Code Settings

The template includes optional VS Code settings to optimize your Python development experience.

## Enabling VS Code Settings

When prompted during project generation:

```
include_vscode_settings [y]:
```

Select `y` to include a pre-configured `.vscode/settings.json` file in your project.

## What Gets Configured

The generated `.vscode/settings.json` includes:

### Python Configuration
- Default interpreter path detection
- Pytest as the testing framework
- Automatic test discovery

### Formatting & Linting
- **Ruff** as the default formatter
- Format on save enabled
- Ruff import organization

### Notebook Support
- Jupyter notebook rendering
- Interactive window support
- Cell execution configuration

### AI Coding Integration
- MCP (Model Context Protocol) configuration (if enabled)
- GitHub Copilot optimization
- Inline suggestions enabled

## Benefits

- ✅ **Consistency**: All team members use the same settings
- ✅ **Zero Configuration**: Works out of the box
- ✅ **Best Practices**: Optimized for Python development
- ✅ **AI-Ready**: Pre-configured for AI coding assistants

## Customization

After project generation, you can customize `.vscode/settings.json` to match your preferences. The generated file serves as a solid foundation.

## Disabling VS Code Settings

If you prefer to use your own VS Code configuration or work with a different editor, simply select `n` when prompted for `include_vscode_settings`. The `.vscode` directory will be excluded from your project.

## Related Features

- [MCP Integration](mcp.md): Enhanced AI development capabilities
- [Pre-commit Hooks](linting.md): Automated code quality checks
