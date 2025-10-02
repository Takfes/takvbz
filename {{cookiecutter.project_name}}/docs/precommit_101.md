# Pre-Commit 101: Crash Course

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. Here's a quick guide:

## Installation
Install pre-commit:
```bash
pip install pre-commit
```

## Key Commands

### 1. **Install Hooks**
Install hooks defined in `.pre-commit-config.yaml`:
```bash
pre-commit install
```

### 2. **Run Hooks**
Run all hooks on all files:
```bash
pre-commit run -a
```
Run hooks only on staged files:
```bash
pre-commit run
```

### 3. **Update Hooks**
Update all hooks to their latest versions:
```bash
pre-commit autoupdate
```

### 4. **Uninstall Hooks**
Remove pre-commit hooks:
```bash
pre-commit uninstall
```

### 5. **Check Config**
Validate the `.pre-commit-config.yaml` file:
```bash
pre-commit validate-config
```

### 6. **List Installed Hooks**
List all installed hooks:
```bash
pre-commit list-hooks
```

### 7. **Run Hooks on a Specific File**
Run pre-commit hooks on a specific file:
```bash
pre-commit run --files <file_path>
```
Example:
```bash
pre-commit run --files example.py
```

### 8. **Skip Pre-Commit Hooks**
To skip pre-commit hooks when committing:
```bash
git commit --no-verify
```

### 9. **Manually Reinstall Hooks**
If hooks are not working as expected, reinstall them:
```bash
pre-commit install --install-hooks
```

### 10. **Debugging Hooks**
Run hooks with verbose output for debugging:
```bash
pre-commit run -a --verbose
```

## Practical Workflow
1. Install hooks: `pre-commit install`
2. Run hooks on staged files: `pre-commit run`
3. Run hooks on all files: `pre-commit run -a`
4. Update hooks periodically: `pre-commit autoupdate`

## Tips
- Use `pre-commit run -a` before committing to ensure all files are checked.
- Add `pre-commit autoupdate` to your workflow to keep hooks up-to-date.

For more details, visit the [Pre-Commit Documentation](https://pre-commit.com/).