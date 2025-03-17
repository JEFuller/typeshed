from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, overload

from tensorflow import Tensor

class Constraint:
    def get_config(self) -> dict[str, Any]: ...
    def __call__(self, w: Tensor, /) -> Tensor: ...

@overload
def get(identifier: None) -> None: ...
@overload
def get(identifier: str | dict[str, Any] | Constraint) -> Constraint: ...
@overload
def get(identifier: Callable[[Tensor], Tensor]) -> Callable[[Tensor], Tensor]: ...
def __getattr__(name: str) -> Incomplete: ...
