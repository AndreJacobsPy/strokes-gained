from dataclasses import dataclass
from scipy.cluster.vq import kmeans
from functions import assign_points, plot_3_clusters
from typing import List
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt


@dataclass
class KMeans:
    n_clusters: int
    data: pd.DataFrame
    cols: List[str]

    def fit(self, seed: bool=False) -> np.array:
        if seed:
            self.clusters, self.score = kmeans(self.data[self.cols], self.n_clusters, seed=42)
        else:
            self.clusters, self.score = kmeans(self.data[self.cols], self.n_clusters)

        return self.clusters

    def transform(self) -> pd.DataFrame:
        assignments = assign_points(self.clusters, self.data[self.cols].values)
        self.data['cluster'] = assignments

        return self.data.copy()


@dataclass
class KMeans2D(KMeans):
    """This is a class that allows object creation for k-means clustering with some useful support methods"""
    def plot(self) -> None:
        plot_3_clusters(self.data, self.cols, self.clusters)


# build model
class NeuralNetwork(nn.Module):
    def __init__(self, input_shape: int) -> None:
        super(NeuralNetwork, self).__init__()

        # dimensions of model
        self.layer1 = nn.Linear(input_shape, 64)
        self.relu1 = nn.ReLU()
        self.layer2 = nn.Linear(64, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.layer1(x)
        x = self.relu1(x)
        x = self.layer2(x)
        return torch.sigmoid(x)

    @staticmethod
    def train_loop(self, model: nn.Module, epochs: int, optim, loss_fn, xtr, xte, ytr, yte) -> tuple:
        losses = []
        test_losses = []

        for epoch in range(epochs):
            model.train()

            # make predictions and calculate loss
            # (forward pass)
            y_pred: torch.tensor = model(xtr)
            loss: torch.tensor = loss_fn(y_pred, ytr)
            losses.append(loss)

            loss.backward()

            # update weights
            # (backpropagation)
            optim.step()
            optim.zero_grad()

            # testing loop
            with torch.inference_mode():
                model.eval()

                # calculate test loss
                test_pred = model(xte)
                test_loss = loss_fn(test_pred, yte)
                test_losses.append(test_loss)

        return torch.Tensor(losses), torch.Tensor(test_losses)

    @staticmethod
    def plot_loss(losses: torch.Tensor, test_losses: torch.Tensor) -> None:
        plt.plot(losses.detach(), label='loss')
        plt.plot(test_losses.detach(), label='test_loss')
        plt.title('Loss Curves')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    model = NeuralNetwork(6)
