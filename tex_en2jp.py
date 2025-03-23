import argparse
from logging import getLogger
from pathlib import Path

from dotenv import load_dotenv

from utils import set_base_log_level, set_log_level

load_dotenv()


def _retrieve_args():
    parser = argparse.ArgumentParser(
        description="transform English to Japanese of tex lualatex file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--tex_file",
        type=Path,
        required=True,
        help="input lualatex file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=1,
        help="increase output verbosity",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="count",
        default=0,
        help="decrease output verbosity",
    )
    args = parser.parse_args()

    if not args.tex_file.is_file:
        raise FileNotFoundError(f"{args.tex_file} does NOT exist.")

    args.verbose -= args.quiet
    del args.quiet
    return args


def main(tex_file: Path, verbose: int):
    logger = getLogger(__name__)
    set_base_log_level(verbose)

    set_log_level("")

    with open(tex_file, "r") as file:
        logger.debug("reading tex_file")
        tex_source = file.read()
        print(tex_source)


if __name__ == "__main__":
    main(**vars(_retrieve_args()))
