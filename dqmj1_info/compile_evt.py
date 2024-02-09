from typing import List

import argparse
import collections
import pathlib
import sys

from .evt import Event


def main(argv: List[str]):
    parser = argparse.ArgumentParser()

    parser.add_argument("--script_filepaths", required=True, nargs="+")
    parser.add_argument("--output_directory", required=True)

    args = parser.parse_args(argv)

    script_filepaths = [pathlib.Path(filepath) for filepath in args.script_filepaths]
    output_directory = pathlib.Path(args.output_directory)

    output_directory.mkdir(exist_ok=True, parents=True)

    for script_filepath in script_filepaths:
        with open(script_filepath, "r") as input_stream:
            event = Event.from_script(input_stream)

        output_filepath = output_directory / (
            script_filepath.name.replace(".dqmj1_script", "")
        )  # TODO: add .evt if needed
        with open(output_filepath, "wb") as output_stream:
            event.write_evt(output_stream)


def main_without_args() -> None:
    main(sys.argv[1:])