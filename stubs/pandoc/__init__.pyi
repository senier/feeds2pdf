from typing import List, Union

from .types import Pandoc, Str

def write(data: Union[Pandoc, Str], file: str, format: str, options: List[str]) -> None: ...
