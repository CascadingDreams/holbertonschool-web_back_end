#!/usr/bin/env python3
"""
Helper function
"""


def index_range(page, page_size):
    '''returns a tuple of start index adn end index'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
