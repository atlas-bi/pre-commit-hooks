"""Pre-commit hook to remove connection string from Atlas scaffolded model context."""
import argparse
import fnmatch
import re
from typing import Optional, Sequence


def find_context_connection_string(filenames: Sequence[str]) -> int:
    """Check files for connection string."""
    retcode = 0

    for filename in filenames:
        if fnmatch.fnmatch(filename, "*/Atlas_WebContext.cs"):
            # search for match in file.
            with open(filename, encoding="UTF-8", newline="") as this_file:
                old_contents = this_file.read()

            new_contents = re.sub(
                r"optionsBuilder\.UseSqlServer\(.*?\);", "", old_contents, re.IGNORECASE
            )

            if new_contents != old_contents:
                retcode = 1
                print(f"Removing connection string in {filename}")  # noqa: T001
                with open(filename, "w", encoding="UTF-8", newline="") as this_file:
                    this_file.write(new_contents)

    return retcode


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Set up pre-commit hook."""
    parser = argparse.ArgumentParser(
        "Remove the scaffold connection string from Atlas_WebContext.cs",
    )

    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )

    args = parser.parse_args(argv)

    return find_context_connection_string(args.filenames)


if __name__ == "__main__":
    raise SystemExit(main())
