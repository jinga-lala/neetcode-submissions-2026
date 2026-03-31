import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        # return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N
        return - 2 * X.T@(ground_truth - model_prediction) / N
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)
        w = initial_weights
        for i in range(num_iterations):
            preds = self.get_model_prediction(X, w)
            grads = self.get_derivative(preds, Y, len(X), X, 0 )
            w = w - self.learning_rate * grads
        
        return np.round(w, 5)



