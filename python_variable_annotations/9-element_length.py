#!/usr/bin/env python3

'''Annotate the below function's parameters and return values'''

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns element length'''
    return [(i, len(i)) for i in lst]
