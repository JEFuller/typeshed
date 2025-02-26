from _typeshed import Incomplete, SupportsGetItem

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def core_number(G: Graph[_Node]): ...
@_dispatchable
def k_core(G: Graph[_Node], k: int | None = None, core_number: SupportsGetItem[Incomplete, Incomplete] | None = None): ...
@_dispatchable
def k_shell(G: Graph[_Node], k: int | None = None, core_number: SupportsGetItem[Incomplete, Incomplete] | None = None): ...
@_dispatchable
def k_crust(G: Graph[_Node], k: int | None = None, core_number: SupportsGetItem[Incomplete, Incomplete] | None = None): ...
@_dispatchable
def k_corona(G: Graph[_Node], k: int, core_number: SupportsGetItem[Incomplete, Incomplete] | None = None): ...
@_dispatchable
def k_truss(G: Graph[_Node], k: int): ...
@_dispatchable
def onion_layers(G: Graph[_Node]): ...
