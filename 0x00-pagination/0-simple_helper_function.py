#!/usr/bin/env python3
"""Simple tuple creator module"""


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
