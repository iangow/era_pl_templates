from graphviz import Digraph


def styled_dag(name: str = "dag") -> Digraph:
    g = Digraph(name)

    # Graph-level layout
    g.attr(
        rankdir="LR",
        splines="true",
        nodesep="0.6",
        ranksep="0.7",
    )

    # Node defaults
    g.attr(
        "node",
        shape="box",
        style="rounded,filled",
        fillcolor="gray85",
        color="black",
        fontname="Helvetica",
        fontsize="11",
        width="1.9",
        height="0.6",
        fixedsize="true",
    )

    # Edge defaults
    g.attr(
        "edge",
        color="black",
        penwidth="2",
        arrowsize="0.9",
    )

    return g
