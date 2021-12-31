"""Sort strings which contains numbers humanized way."""

import re
from typing import Union


def natural_sort(lst: list[str]) -> list[str]:
    def _convert(text: str) -> Union[int, str]:
        return int(text) if text.isdigit() else text.lower()

    def _alphanumeric(key: str) -> list[Union[int, str]]:
        return [_convert(c) for c in re.split('(\\d+)', key)]
    return sorted(lst, key=_alphanumeric)


strings = ['Elm12', 'Elm11', 'elm0', 'Elm2', 'elm1', 'elm10', 'elm13', 'elm9']
print(sorted(strings))
# -> ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
print(natural_sort(strings))
# -> ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
