# Quant Prep — Environment Setup Notes & Context Transfer

A record of everything set up on Day 1, the problems hit and how they were fixed, and a paste-ready summary for starting a fresh chat.

---

## 1. What's installed (all permanent, on the Mac + GitHub)

| Tool | Purpose | Installed via |
|------|---------|---------------|
| Homebrew | Mac package manager (installs everything else) | brew.sh install script |
| Git | Version control | `brew install git` |
| Xcode Command Line Tools | Compiler support (prevents package build errors) | `xcode-select --install` |
| uv | Python version + virtual environment manager | `brew install uv` |
| VS Code | Code editor | `brew install --cask visual-studio-code` |
| SSH key (ed25519) | Passwordless GitHub auth | `ssh-keygen` + added to GitHub |

GitHub username: **RudraYA54** (note: this is different from the Mac login name `sakshiagarwal`).

First repo live at: `https://github.com/RudraYA54/probability-helpers`

---

## 2. The project structure that works

```
probability-helpers/
├── .venv/                      # virtual environment (git-ignored)
├── src/
│   └── combinatorics.py        # the actual code
├── tests/
│   └── test_combinatorics.py   # pytest tests (functions must start with test_)
├── conftest.py                 # empty; helps pytest find the root
├── .gitignore                  # excludes .venv, __pycache__, etc.
├── pyproject.toml              # project config + pytest config
└── README.md
```

The critical part of `pyproject.toml` that made pytest work:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
```

Without `pythonpath = ["."]`, the `from src.combinatorics import ...` line fails and pytest reports "collected 0 items".

---

## 3. The daily working loop (memorize this)

**Start a work session:**
```
cd ~/projects/probability-helpers
source .venv/bin/activate        # prompt should show (probability-helpers)
```

**Run tests:**
```
pytest -v                        # run from the project ROOT folder
```

**Save work to GitHub (after each meaningful chunk):**
```
git status                       # always check first
git add .
git commit -m "clear message describing the change"
git push                         # no args needed — -u was set on first push
```

---

## 4. Problems hit on Day 1 and the lessons (these WILL recur)

1. **`command not found: brew`** → PATH problem. Homebrew was installed but the shell couldn't find it. Fix: add `eval "$(/opt/homebrew/bin/brew shellenv)"` to `~/.zprofile`, then open a new terminal.
   - *Lesson:* `command not found` ≠ "not installed." Check if the binary exists with `ls` first, then fix the PATH.

2. **pytest "collected 0 items"** → import/path issue, not a code issue. The `from src...` import couldn't resolve.
   - *Fix:* added `pythonpath = ["."]` to pyproject.toml.

3. **Empty file** → the code looked present in VS Code but was never saved to disk, so imports found nothing.
   - *Lesson:* a white dot on the VS Code tab = unsaved. Cmd+S, or turn on File → Auto Save.

4. **Stale terminal** → things behaved inconsistently with what was on disk; closing and reopening Terminal fixed it.
   - *Lesson:* a fresh terminal is a cheap first thing to try when behavior doesn't match the files.

5. **"remote origin already exists"** → can't `git remote add` twice; use `git remote set-url origin <url>` to change it.

6. **"Repository not found"** → the remote URL had the wrong username (Mac login name instead of GitHub username `RudraYA54`).
   - *Lesson:* Mac login name ≠ GitHub username. The SSH URL is `git@github.com:GITHUB_USERNAME/repo.git`.

---

## 5. The most important rule going forward

**Write the code yourself — don't copy-paste solutions.**

Setup/shell commands are fine to be given directly. But the *substance* (the math, the algorithms, the analysis) should be written by you, then reviewed. Copy-pasting working code teaches almost nothing; producing it (and debugging it) is the actual skill recruiters test for.

Self-check after building anything: close everything and try to rebuild the key piece from memory on a blank file. If you can't, you watched it — you didn't learn it.

---

## 6. Paste this into a new chat to transfer context

> I've completed my dev environment setup on Mac: Homebrew, Git, uv (Python), VS Code, an SSH key, and my first repo `probability-helpers` (GitHub username RudraYA54) with a src/tests layout and passing pytest tests, pushed to GitHub. I'm on Week 1 of an 8-week quant-researcher prep plan (I'm a Physics undergrad entering Year 2, aiming for quant research roles). Week 1 focus: Python proficiency, probability foundations (using Harvard Stat 110 + the Green Book), Git/Linux fluency, and building a tested probability-helpers library.
>
> Important: I want to WRITE THE CODE MYSELF, not copy-paste. Give me concepts, hints, and function signatures — let me implement, then review my work. Only give complete code for pure setup/shell commands.
>
> Next up: extending the probability-helpers library with functions like expected value of a discrete distribution, conditional probability, and Bayes' theorem — each written by me, with tests.

---

## 7. Immediate next steps

- [ ] Turn on VS Code auto-save (File → Auto Save)
- [ ] Write a real README.md for the probability-helpers repo
- [ ] Implement `expected_value(values, probabilities)` yourself, with a test
- [ ] Start Stat 110 lectures (conditional probability, Bayes, expectation first)
- [ ] Green Book: 5 problems/day, written by hand
