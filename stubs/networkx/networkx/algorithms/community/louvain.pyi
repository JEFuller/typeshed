from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def louvain_communities(
    G: Graph[_Node],
    weight: str | None = "weight",
    resolution: float | None = 1,
    threshold: float | None = 1e-07,
    max_level: int | None = None,
    seed: int | RandomState | None = None,
): ...
@_dispatchable
def louvain_partitions(
    G: Graph[_Node],
    weight: str | None = "weight",
    resolution: float | None = 1,
    threshold: float | None = 1e-07,
    seed: int | RandomState | None = None,
) -> Generator[Incomplete, None, None]: ...
