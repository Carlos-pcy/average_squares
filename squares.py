"""Computation of weighted average of squares."""
import argparse
from argparse import ArgumentParser

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]

def convert_numbers_from_file(file_path):
    """Read numbers from a file and convert them to a list of floats."""
    with open(file_path, 'r') as f:
        content = f.read().strip()
    return [float(number) for number in content.split()]


if __name__ == "__main__":

    parse = ArgumentParser(description="Compute the weighted average of some numbers.")
    parse.add_argument("numbers_file", type=str,
                       help="path to the file containing the numbers to average")
    parse.add_argument("--weights_file", type=str, default=None,
                       help="path to the file containing the weights of the numbers")
    
    args = parse.parse_args()
    
    numbers = convert_numbers_from_file(args.numbers_file)

    weights = convert_numbers_from_file(args.weights_file) if args.weights_file else None
   
    result = average_of_squares(numbers, weights)
    
    print(result)