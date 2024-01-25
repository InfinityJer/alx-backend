#!/usr/bin/env python3
"""
Module with a simple helper function for pagination
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for a given pagination parameters.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start and end indexes for the requested page.

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

if __name__ == "__main__":
    # Example usage
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
