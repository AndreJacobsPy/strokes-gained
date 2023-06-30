from scipy.cluster.vq import kmeans
from scipy.spatial.distance import euclidean
from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def clustering_kmeans(df: pd.DataFrame, cols: List[str], n_clusters: int, group: int) -> np.array:
    '''A function that creates clusters'''
    # find clusters
    data = df[group][cols].values
    clusters, score = kmeans(data, n_clusters)

    return clusters, data, score


def assign_points(clusters: list, data: np.array) -> list:
    '''A function that assigns point to their closest cluster'''
    cluster_assignment = list()

    for row in data:
        distances = list()

        for i in clusters:
            distances.append(euclidean(row, i))

        cluster_num = distances.index(min(distances))
        cluster_assignment.append(cluster_num)

    return cluster_assignment


def plot_3_clusters_grouped(df: pd.DataFrame, tournaments: pd.DataFrame, cols: List[str], clusters: np.array, group: int) -> None:
    fig, ax = plt.subplots()

    # cluster 0
    zero = df.query('cluster == 0')
    ax.scatter(zero[cols[0]], zero[cols[1]], alpha=0.6, label=0)

    # cluster 1
    first = df.query('cluster == 1')
    ax.scatter(first[cols[0]], first[cols[1]], alpha=0.6, label=1)

    # cluster 2
    second = df.query('cluster == 2')
    ax.scatter(second[cols[0]], second[cols[1]], alpha=0.6, label=2)

    # cluster centers
    ax.scatter(clusters[:, 0], clusters[:, 1])

    # plot the winner
    winner = df.query('pos == "1"')
    ax.scatter(winner[cols[0]], winner[cols[1]], c='#FF5C38', marker=(5, 1), s=200, label='winner')

    # create axis labels
    ax.set(
        xlabel=cols[0], ylabel=cols[1],
        title='{} vs. {} ({})'.format(cols[0], cols[1], tournaments['name'][group])
    )

    # show plot
    plt.legend()
    plt.show()


def plot_3_clusters(df: pd.DataFrame, cols: List[str], clusters: np.array) -> None:
    fig, ax = plt.subplots()

    # cluster 0
    zero = df.query('cluster == 0')
    ax.scatter(zero[cols[0]], zero[cols[1]], alpha=0.6, label=0)

    # cluster 1
    first = df.query('cluster == 1')
    ax.scatter(first[cols[0]], first[cols[1]], alpha=0.6, label=1)

    # cluster 2
    second = df.query('cluster == 2')
    ax.scatter(second[cols[0]], second[cols[1]], alpha=0.6, label=2)

    # cluster centers
    ax.scatter(clusters[:, 0], clusters[:, 1])

    # create axis labels
    ax.set(
        xlabel=cols[0], ylabel=cols[1],
        title='{} vs. {}'.format(cols[0], cols[1])
    )

    # set x and y-axis limits
    ax.set_xticks([i for i in range(-4, 5)])
    ax.set_yticks([i for i in range(-4, 5)])

    # show plot
    plt.legend()
    plt.show()