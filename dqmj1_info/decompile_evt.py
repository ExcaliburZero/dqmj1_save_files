from typing import List

import argparse
import pathlib
import sys

import evt


def main(argv: List[str]):
    parser = argparse.ArgumentParser()

    parser.add_argument("--evt_filepaths", required=True, nargs="+")
    parser.add_argument("--output_directory", required=True)
    parser.add_argument("--ignore_unknown_commands", default=False, action="store_true")

    args = parser.parse_args(argv)

    evt_filepaths = [pathlib.Path(filepath) for filepath in args.evt_filepaths]
    output_directory = pathlib.Path(args.output_directory)

    output_directory.mkdir(exist_ok=True, parents=True)

    for evt_filepath in evt_filepaths:
        with open(evt_filepath, "rb") as input_stream:
            event = evt.Event.from_evt(input_stream)

        output_filepath = output_directory / (evt_filepath.name + ".dqmj1_script")
        with open(output_filepath, "w") as output_stream:
            for command in event.commands:
                if not args.ignore_unknown_commands or not isinstance(
                    command, evt.UnknownCommand
                ):
                    print(command, file=output_stream)


if __name__ == "__main__":
    main(sys.argv[1:])