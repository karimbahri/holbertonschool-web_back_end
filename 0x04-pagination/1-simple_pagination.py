#!/usr/bin/env python3
"""1-simple_pagination.py"""
import typing
import csv
import math
from typing import List


def index_range(page, page_size) -> typing.Tuple:
    """index_range:
    function that takes page and page_size
    as arguments and returns a tuple containing
    start index and stop index corresponding to range
    of index
    """
    crr_page = (page - 1) * page_size
    return crr_page, crr_page + page_size


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
        """get_page:
            instance method that takes page(int) and pageSize(int)
            and paginate dataset
        """
        assert (type(page) is int and page > 0)
        assert (type(page_size) is int and page_size > 0)

        index = index_range(page, page_size)
        self.dataset()
        if len(self.__dataset) > index[0]:
            return self.__dataset[index[0]:index[1]]
        return []
