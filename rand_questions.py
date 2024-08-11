"""
Choong Min Um <choongmin.um@unh.edu>

This module selects a random set of questions per section of a book.
"""

import argparse
import random
from pprint import pprint

# Enter book-specific sections and numbers of questions.
sections = {
        'Adult Health 1': 86,
        'Adult Health 2': 40,
        'Child Health': 115,
        'Maternal & Newborn Health': 85,
        'Mental Health': 120,
        'Fundamentals & Management': 85
        }


def get_questions(num_questions):
    rand_questions = {}
    for key in sections:
        rand_questions[key] = sorted([
            random.randint(1, sections[key]) for num in range(num_questions)
            ]
                                     )
    return rand_questions


def get_args():
    parser = argparse.ArgumentParser(
            description=(
                'This module selects a random set of questions per '
                'section of a book.'
                )
            )
    parser.add_argument(
            'num_questions',
            type=int,
            help='number of questions you want per section'
            )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    questions = get_questions(args.num_questions)
    pprint(questions)


if __name__ == '__main__':
    main()
