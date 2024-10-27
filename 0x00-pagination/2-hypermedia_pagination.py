#!/usr/bin/env python3
'''

1-simple_pagination

'''
from typing import Tuple, List, Union, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    returns the index range based on page no and page size
    '''
    return ((page - 1) * page_size, page_size * page)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        '''gets the particular section of the dataset'''
        if self.__dataset:
            data = self.__dataset
        else:
            data = self.dataset()
        assert type(page_size) == int and page_size > 0
        assert type(page) == int and page > 0
        start, end = index_range(page, page_size)
        return data[start: end]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Union[int, List[List[str]], None]]:
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
