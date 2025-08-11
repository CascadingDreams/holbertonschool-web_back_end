#!/usr/bin/env python3

"""
Helper function
"""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """returns a tuple of start index adn end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method to"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_list = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(data_list):
            return []

        return data_list[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dict"""
        data_list = self.get_page(page, page_size)

        total_pages_count = math.ceil(len(self.dataset()) / page_size)

        next_page_number = page + 1 if page < total_pages_count else None

        prev_page_number = page - 1 if page > 1 else None

        actual_page_size = len(data_list)

        return {
            "page_size": actual_page_size,
            "page": page,
            "data": data_list,
            "next_page": next_page_number,
            "prev_page": prev_page_number,
            "total_pages": total_pages_count,
        }
