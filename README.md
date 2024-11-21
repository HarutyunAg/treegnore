# 🌳TreeGnore
Tired of messy directory trees filled with `.git` and `.gitignore` junk?  
Let TreeGnore keep it clean and simple! 🧹✨

TreeGnore generates a tree of your project's directory while ignoring files and directories specified in the `.gitignore` and excluding the `.git` folder.

```bash
treegnore
│
├── treegnore
│   ├── __init__.py
│   ├── cli.py            # Handles command-line args using argparse
│   ├── parser.py         # Parse .gitignore and generating the tree
│   └── treegnore.py      # Core class for using
├── .gitignore
├── pyproject.toml
├── README.md
└── tree.py
```

## Setup

```bash
    git clone https://github.com/yourusername/treegnore.git
    cd treegnore
    poetry shell
```
### 🌳How to plant a tree?

```bash
    python tree.py path/to/project/root
```

### 💾 Save the Tree to a File  
Want to save the tree?

Use the -o or --output flag:

```bash
    python tree.py path/to/project/root -o tree.txt
```
This saves the tree structure to a file named tree.txt in the project root directory.