# Vibecoding Development Workflows

The template includes optional "vibecoding" resources to enhance AI-assisted development workflows.

## What is Vibecoding?

Vibecoding is a development approach that leverages AI coding assistants effectively through:

- **Clear Instructions**: Structured guidance for AI assistants
- **Project Standards**: Consistent coding patterns and conventions  
- **Prompt Libraries**: Reusable prompts for common tasks
- **Best Practices**: Documented development workflows

## Enabling Vibecoding

When prompted during project generation:

```
include_vibecoding [y]:
```

Select `y` to include vibecoding resources in your project.

## What Gets Generated

When vibecoding is enabled, the template creates:

```
.github/
├── copilot-instructions.md   # Project-specific AI guidance
├── instructions/             # Structured instruction library
│   └── (various .md files)
└── prompts/                  # Reusable prompt templates
    └── (various .md files)
```

### GitHub Copilot Instructions

The `.github/copilot-instructions.md` file provides context-aware guidance for AI assistants:

- Project coding standards (PEP8, type hints, Black formatting)
- Module organization principles
- Testing requirements with Pytest
- Documentation standards (Google-style docstrings)
- Error handling patterns

### Instructions Library

The `instructions/` directory contains structured guidance for:

- Code reviews
- Feature implementation
- Bug fixes
- Refactoring tasks
- Documentation updates

### Prompts Library

The `prompts/` directory includes reusable templates for:

- Creating new modules
- Writing tests
- Generating documentation
- Code optimization
- Security reviews

## Benefits

- ✅ **Consistent Code Quality**: AI follows your standards
- ✅ **Faster Development**: Pre-built prompts save time
- ✅ **Better Context**: AI understands project structure
- ✅ **Team Alignment**: Everyone uses the same patterns

## Usage

Once your project is generated with vibecoding enabled:

1. **AI Assistants**: Tools like GitHub Copilot automatically read `.github/copilot-instructions.md`
2. **Manual Reference**: Use files in `instructions/` and `prompts/` as templates
3. **Customization**: Adapt the provided resources to your specific needs

## Disabling Vibecoding

If you prefer to work without these AI workflow enhancements, simply select `n` when prompted for `include_vibecoding`. All vibecoding-related files will be excluded from your project.

## Related Features

- [MCP Integration](mcp.md): Enhanced AI tool access
- [VS Code Settings](vscode.md): Optimized development environment
