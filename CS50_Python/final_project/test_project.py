from unittest.mock import patch
import pytest
import argparse
from project import parse_args, handle_no_args


def test_handle_no_args_with_no_args():
    """Test handle_no_args with no arguments."""
    parser = argparse.ArgumentParser()
    args = parser.parse_args([])
    with pytest.raises(AttributeError):
        handle_no_args(args, parser)


def test_handle_no_args_with_args():
    """Test handle_no_args with arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cat", action="store_true", help="Get random cat facts")
    args = parser.parse_args(["-c"])
    handle_no_args(args, parser)


def test_parse_args_with_cat_arg():
    """Test parse_args with the cat argument."""
    args, parser = parse_args(["-c"])
    assert args.cat == True
    assert args.dog == False
    assert args.number == 1


def test_parse_args_with_dog_arg():
    """Test parse_args with the dog argument."""
    args, parser = parse_args(["-d"])
    assert args.cat == False
    assert args.dog == True
    assert args.number == 1
