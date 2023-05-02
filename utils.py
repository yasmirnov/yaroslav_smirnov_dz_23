from typing import Any, Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any):
    return set(data)


def limit_query(value: str, data: Iterable[str]):
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)
