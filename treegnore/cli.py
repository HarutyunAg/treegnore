import argparse
from pathlib import Path


class CLIParser:
    """
    Responsible for parsing and validating command-line arguments.
    """

    def __init__(self):
        self._parser = self.__create_parser()

    def __create_parser(self) -> argparse.ArgumentParser:
        """
        Creates and configures the argument parser.
        """
        PARSER_DESC = "Generate a directory tree structure while respecting .gitignore."
        HELP_ARG_DIR = "Specify path to the project directory."
        HELP_ARG_OUT = "Specify output file name to save the tree structure to the project root dir."
        HELP_ARG_DIRS_ONLY = "Display only directories (exclude files) in the tree structure."

        parser = argparse.ArgumentParser(description=PARSER_DESC)
        parser.add_argument(
            "project_directory",
            help=HELP_ARG_DIR,
            type=str
        )

        parser.add_argument(
            "-o", "--output",
            default="",
            help=HELP_ARG_OUT,
            type=str
        )
        
        parser.add_argument(
            "-d", "--dirs-only",
            action="store_true",  # This makes it a flag that doesn't require a value
            help=HELP_ARG_DIRS_ONLY,
            default=False
        )
        return parser

    def parse_args(self) -> argparse.Namespace:
        """
        Parses and validates the command-line arguments.
        """
        args = self._parser.parse_args()
        self._validate_args(args)
        return args

    def _validate_args(self, args: argparse.Namespace):
        """
        Validates the provided command-line arguments.
        """
        project_directory = Path(args.project_directory)
        if not project_directory.is_dir():
            raise ValueError(f"Error: {project_directory} is not a valid directory.")
        args.project_directory = project_directory
