from pathlib import Path
from treegnore.parser import DirectoryTree


class Treegnore:

    def __init__(
            self,
            output_fname: Path,
            project_directory: Path,
            ):

        self.root = project_directory
        self.output_fname = output_fname
        self.tree = DirectoryTree(project_directory)

    def grow_project_tree(self):
        tree_structure = self.tree.grow()
        print(tree_structure)

        if self.output_fname:
            p: Path = self.root / self.output_fname
            with open(p, "w", encoding='utf-8') as f:
                f.write(tree_structure)
            print(f"Tree structure saved to {p}")
