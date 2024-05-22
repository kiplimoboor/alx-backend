#!/usr/bin/env python3
"""A class implementation of paged REST APIs"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
    Creates a tuple with a start and end index for a page
    Args:
        page: the page number
        page_size: the size of the pages
    Return:
        An tuple containing a start and end index for a page
    """

    end = page_size * page
    return (end - page_size, end)


class Server:
    """
    Server class that returns paginated API responses
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets data from certain rows in a csv file
        Args:
            page: page of the data to be returned
            page_size: a specification of how many rows a page should be
        Return:
            Rows of size page_size that are found on page page.
        """
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        range = index_range(page, page_size)
        try:
            return self.dataset()[range[0]:range[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets data from certain rows in a csv file
        Args:
            page: page of the data to be returned
            page_size: a specification of how many rows a page should be
        Return:
            A dictionary with more info about the rows returned.
        """
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        range = index_range(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        try:
            rows = dataset[range[0]:range[1]]
        except IndexError:
            rows = []

        return {
            'page_size': page_size,
            'page': page,
            'data': rows,
            'next_page': None if page >= total_pages else page + 1,
            'prev_page': None if page <= 1 else page - 1,
            'total_pages': total_pages,
        }
