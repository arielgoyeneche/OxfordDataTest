# import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from definition import Gr


def apply_step(df, step):
    """
    :param df: Pandas DataFrame
    :param step: Dictionary with field and function
    :return: One column DataFrame produced by a function applied to the input dataframe
    """
    df_local = df.copy()
    args = dict((ar, df_local[ar]) for ar in step['function'].__code__.co_varnames)
    return step['function'](**args)


def apply_edge(df, edge):
    """
    :param df: Pandas Dataframe
    :param edge: A list of steps. Each step is a dictionary containing a lambda function and a destination field name
    :return: Pandas DataFrame with all steps applied.
    """
    output_df = pd.DataFrame()
    for step in edge:
        output_df[step['field']] = apply_step(df, step)
    return output_df


def leaves(graph):
    """
    :param graph: A graph that implements a in_degree function.
    :return: A list of nodes that do not have input edges
    """
    return [n for n, d in graph.in_degree().items() if d == 0]


def run_graph(graph):
    """
    :param graph:
    :return:
    """
    results = []
    if nx.is_forest(graph):
        while len(leaves(graph)) > 0:
            current_leaves = leaves(graph)
            for n in current_leaves:
                for edge in graph.edges_iter(n):
                    local_data = graph.node[n]['data'].copy()
                    if 'data' not in graph.node[edge[1]]:
                        graph.node[edge[1]]['data'] = apply_edge(local_data, graph.edge[edge[0]][edge[1]]['transformation']).copy()
                    else:
                        graph.node[edge[1]]['data'] = pd.merge( left=graph.node[edge[1]]['data'],
                                                                right=apply_edge(local_data,
                                                                graph.edge[edge[0]][edge[1]]['transformation']).copy(),
                                                                how='left',
                                                                left_on=graph.node[edge[1]]['match_keys'],
                                                                right_on=graph.node[edge[1]]['match_keys']
                                                                )

                if 'producer' in graph.node[n]:
                    if graph.node[n]['producer']:
                        results.append(graph.node[n]['data'])

                graph.remove_node(n)
    return results

# def main():
print(run_graph(Gr))
