from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def efficiency(G, u: _Node, v: _Node): ...
@_dispatchable
def global_efficiency(G): ...
@_dispatchable
def local_efficiency(G): ...
