# GitHub Agent Guide: Crash Course

A quick guide to understanding GitHub Copilot's instruction framework.

## The Framework

### 1. **Copilot Instructions** (`.github/copilot-instructions.md`)
**What:** Global rules that apply to all interactions with Copilot in your project.  
**When Applied:** Always loaded—Copilot reads this file at the start of every session.  
**Use Case:** Define project-wide coding standards, error handling, documentation rules, and AI behavior.

**Example:**
```markdown
- Use PEP8 standards and type hints
- Write docstrings using Google style
- Always log errors with context
```

### 2. **Instructions** (`.github/instructions/*.instructions.md`)
**What:** File-specific or pattern-specific rules that apply when working with matching files.  
**When Applied:** Automatically invoked when editing files that match the pattern defined in the instruction file.  
**Use Case:** Enforce standards for specific file types (e.g., Docker best practices for `Dockerfile`, commenting standards for `*.py`).

**Example:**
- `docker-best-practices.instructions.md` → Applies to `**/Dockerfile`, `**/docker-compose*.yml`
- `conventional-commit.instructions.md` → Applies to `**/*` (all files)

**How It Works:**
Each instruction file has a metadata table:
```markdown
| File | Applies To | Description |
| ------- | --------- | ----------- |
| 'file.instructions.md' | **/*.py | Python coding standards |
```

### 3. **Prompts** (`.github/prompts/*.md`)
**What:** Reusable, explicit prompts you can invoke manually in conversations.  
**When Applied:** Only when explicitly referenced by the user (e.g., "Use #prompt:code-review").  
**Use Case:** Standardize common tasks like code reviews, refactoring, or testing workflows.

**Example:**
```markdown
# Prompt: Code Review
Review the code for:
- PEP8 compliance
- Type hints
- Error handling
```

## How They Work Together

1. **Copilot Instructions:** Always active, set the baseline behavior.
2. **Instructions:** Auto-triggered when editing matching files.
3. **Prompts:** Manually invoked for specific tasks.

## Practical Workflow

- **Set Global Standards:** Update `copilot-instructions.md` for project-wide rules.
- **Add File-Specific Rules:** Create instruction files for specific patterns (e.g., `*.py`, `Dockerfile`).
- **Create Reusable Prompts:** Add prompts for repetitive tasks (e.g., code review, refactoring).

## Tips
- Keep instructions concise and actionable.
- Use examples to clarify expectations.
- Test changes by observing Copilot's behavior in real tasks.

For more details, refer to the [GitHub Copilot Documentation](https://docs.github.com/copilot).
Refer to this for template ideas: [Awesome Copilot](https://github.com/github/awesome-copilot/tree/main).