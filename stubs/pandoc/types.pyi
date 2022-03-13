from typing import Any, Dict, List, Tuple, Union

class Space: ...

Text = str

Target = Tuple[Text, Text]

Attr = Tuple[Text, List[Text], List[Tuple[Text, Text]]]

Inline = Union[Link, Space, Str, Emph]

Block = Union[Header, Para, RawBlock]

Para = List[Inline]

MetaValue = Union[MetaInlines, MetaBlocks, MetaList]

Meta = Dict[Text, MetaValue]

class Pandoc:
    def __init__(self, meta: Meta, content: List[Block]): ...
    def __getitem__(self, items: int) -> List[Block]: ...

class Link:
    def __init__(self, attr: Attr, value: List[Inline], target: Target): ...

class Header:
    def __init__(self, level: int, attr: Attr, value: List[Inline]): ...

class Str:
    def __init__(self, text: Text): ...

class Format(Str): ...

class RawBlock:
    def __init__(self, fmt: Format, data: str): ...

class MetaInlines:
    def __init__(self, value: List[Inline]): ...

class MetaBlocks:
    def __init__(self, value: List[Block]): ...

class MetaList:
    def __init__(self, value: List[MetaValue]): ...

class Emph:
    def __init__(self, value: List[Inline]): ...
