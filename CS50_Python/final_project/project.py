"""
This file is used to run the project.

Author: saifuddin Rakib

Usage:
    python project.py

Features:
    1: Get random facts about CATS
    2: Get random facts about DOGS
    3: Get random facts about BIRDS

"""
import argparse
import sys

from rich import print, pretty
from rich.table import Table
from rich.console import Console

from models.cat_facts import CatFacts
from models.dog_facts import DogFacts


# Set rich print options
pretty.install()
console = Console()



def beautify_facts(facts: list) -> str:
    """Beautify facts.

    Args:
        facts (list): Facts to beautify.

    Returns:
        str: Beautified facts.
    """
    table = Table(
        title="Animal Facts",
        show_header=False,
        header_style="bold magenta",
        show_lines=True,
        padding=(0, 1),
    )
    table.add_column("No,", justify="center", style="cyan")
    table.add_column("Facts", justify="center", style="cyan")
    for index, fact in enumerate(facts):
        table.add_row(str(index + 1), fact)
    return table


def parse_args(args):
    """Parse command line arguments.

    Args:
        None

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Get random facts about animals",
        usage="python project.py [-h] [-c] [-d] [-n NUMBER]",
    )
    parser.add_argument("-c", "--cat", action="store_true", help="Get random cat facts")
    parser.add_argument(
        "-d",
        "--dog",
        action="store_true",
        help="Get random dog facts",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of facts to return",
        choices=range(1, 10),
    )
    args = parser.parse_args(args)
    return args, parser


def get_facts(args: argparse.Namespace) -> str:
    """Get facts.

    Args:
        args (argparse.Namespace): Parsed arguments.

    Returns:
        str: Facts.
    """
    cat_facts = CatFacts()
    dog_facts = DogFacts()
    if args.cat:
        facts = cat_facts.get_random_n_cat_fact(args.number)
    elif args.dog:
        facts = dog_facts.get_random_n_dog_fact(args.number)
    else:
        facts = None
    return facts


def handle_no_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    """Handle no arguments.

    Args:
        parser (argparse.ArgumentParser): Argument parser.

    Returns:
        None
    """
    if not args.cat and not args.dog:
        parser.print_help()
        sys.exit(1)


def print_intro():
    """Print intro.

    Args:
        None

    Returns:
        None
    """
    console.print(
        "[bold blue]Welcome to Animal Facts[/bold blue]",
        justify="center",
    )
    console.print(
        "[bold blue]Get random facts about animals[/bold blue]",
        justify="center",
    )
    console.print(
        "[bold red]Developed by Saifuddin_Rakib[/bold red]",
        justify="center",
    )
    console.print(
        "[bold red]CS50P Final Project[/bold red] 🚀",
        justify="center",
    )


def print_facts(facts: str) -> None:
    """Print facts.

    Args:
        facts (str): Facts to print.

    Returns:
        None
    """
    console.print(
        beautify_facts(facts),
        justify="center",
    )


def main():
    print_intro()
    args, parser = parse_args(sys.argv[1:])
    handle_no_args(args, parser)
    facts = get_facts(args)
    if facts:
        print_facts(facts=facts)
    else:
        print("No facts found")


if __name__ == "__main__":
    main()
