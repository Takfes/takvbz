- doc files about copilot and tool usage could be moved to a different location
- update the smart commit prompt + add changelog generation
- enable memory mcps servers
- update readme - include basic make commands
- what's the vscode settings question in the prompt?
- enable data and exec (find a better name) folders in the repo
- make : install - activate the venv in one go?
- does not instantiate git?
- fix make install error :

```python
An error has occurred: FatalError: git failed. Is it installed, and are you in a Git repository directory?
Check the log at /Users/takis/.cache/pre-commit/pre-commit.log
make: *** [install] Error 1
```

```python
Traceback (most recent call last):
  File "/Users/takis/Documents/sckool/fun-simpy-des-modeling/.venv/lib/python3.11/site-packages/pre_commit/error_handler.py", line 73, in error_handler
    yield
  File "/Users/takis/Documents/sckool/fun-simpy-des-modeling/.venv/lib/python3.11/site-packages/pre_commit/main.py", line 373, in main
    _adjust_args_and_chdir(args)
  File "/Users/takis/Documents/sckool/fun-simpy-des-modeling/.venv/lib/python3.11/site-packages/pre_commit/main.py", line 183, in _adjust_args_and_chdir
    toplevel = git.get_root()
               ^^^^^^^^^^^^^^
  File "/Users/takis/Documents/sckool/fun-simpy-des-modeling/.venv/lib/python3.11/site-packages/pre_commit/git.py", line 64, in get_root
    raise FatalError(
pre_commit.errors.FatalError: git failed. Is it installed, and are you in a Git repository directory?
```
