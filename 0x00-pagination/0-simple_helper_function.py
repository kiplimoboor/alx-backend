#!/usr/bin/env python3

"""Simple index range module"""


def index_range(page: int, page_size: int) -> tuple:
    return (page * page_size - page_size, page * page_size)
