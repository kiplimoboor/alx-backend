#!/usr/bin/env python3

"""Simple pagination module"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Creates a tuple with a start and end index for a page
    Args:
        page: the page number
        page_size: the size of the pages
    Return:
        An tuple containing a start and end index for a page
    """

    last_index = page * page_size
    return (last_index - page_size, last_index)


class Server:
    """Server class to paginate a database of popular baby names.
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
