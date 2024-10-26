#!/usr/bin/env python3
'''

defines index_range for task 0

'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    returns the index range based on page no and page size
    '''
    return ((page - 1) * page_size, page_size * page)
