from typing import Any, Dict, List, Tuple, Union

class Space: ...

Text = str

Target = Tuple[Text, Text]

Attr = Tuple[Text, List[Text], List[Tuple[Text, Text]]]

Inline = Union[Link, Space, Str]

Block = Union[Header, Para]

Para = List[Inline]

MetaValue = List[None]

Meta = Dict[Text, MetaValue]

class Pandoc:
    def __init__(self, meta: Meta, content: List[Block]): ...

class Link:
    def __init__(self, attr: Attr, value: List[Inline], target: Target): ...

class Header:
    def __init__(self, level: int, attr: Attr, value: List[Inline]): ...

class Str:
    def __init__(self, text: Text): ...
