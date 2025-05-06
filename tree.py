from treegnore import Treegnore, CLIParser


def main():
    try:
        cli_parser = CLIParser()
        args = cli_parser.parse_args()

        tree_generator = Treegnore(
            project_directory=args.project_directory,
            output_fname=args.output,
            dirs_only=args.dirs_only
        )
        tree_generator.grow_project_tree()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
