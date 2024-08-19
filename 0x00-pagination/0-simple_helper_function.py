#!/usr/bin/env python3

"""Simple index range module"""


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
