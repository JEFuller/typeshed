from _typeshed import Incomplete
from typing import Final

from reportlab.graphics.widgets.signsandsymbols import _Symbol
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

__version__: Final[str]
validFlag: Incomplete

class Star(_Symbol):
    size: int
    fillColor: Incomplete
    strokeColor: Incomplete
    angle: int
    def __init__(self) -> None: ...
    def demo(self): ...
    def draw(self): ...

class Flag(_Symbol):
    kind: Incomplete
    size: int
    fillColor: Incomplete
    border: int
    def __init__(self, **kw) -> None: ...
    def availableFlagNames(self): ...
    def draw(self): ...
    def clone(self): ...
    def demo(self): ...

def makeFlag(name): ...
def test() -> None: ...
