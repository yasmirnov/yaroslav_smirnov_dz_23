from typing import Callable, Dict, Iterable, List, Optional

from utils import filter_query, limit_query, map_query, sort_query, unique_query


CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as f:
        for line in f:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
