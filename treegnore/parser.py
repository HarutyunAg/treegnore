from pathlib import Path


class GitignoreParser:

    def __init__(self, project_root_path: Path):
        gitignore_path: Path = project_root_path / ".gitignore"
        self.ignored_patterns: list[str] = self.__parse_gitignore(gitignore_path)

    def is_ignored(self, path: Path) -> bool:
        return any(path.match(pattern) for pattern in self.ignored_patterns)

    def __parse_gitignore(self, gitignore_path: Path) -> list[str]:
        if not gitignore_path.exists():
            return []

        with open(gitignore_path, "r") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]


class DirectoryTree:

    def __init__(self, project_directory: Path):
        self.project_directory = project_directory
        self.gitignore_parser = GitignoreParser(project_directory)

    def grow(self):
        return self.__grow_tree(self.project_directory)

    def __grow_tree(self, directory: Path, prefix: str = "") -> str:

        entries = sorted(directory.iterdir(),
                         key=lambda e: (e.is_file(), e.name.lower()))
        tree_structure = []

        for idx, entry in enumerate(entries):
            if entry.name == ".git":
                continue
            if self.gitignore_parser.is_ignored(entry):
                continue

            is_last_idx: bool = idx == len(entries) - 1
            connector = "└── " if is_last_idx else "├── "

            tree_structure.append(f"{prefix}{connector}{entry.name}")
            if entry.is_dir():
                new_prefix = prefix + ("    " if idx == len(entries) - 1 else "│   ")
                tree_structure.append(self.__grow_tree(entry, new_prefix))

        return "\n".join(tree_structure)
