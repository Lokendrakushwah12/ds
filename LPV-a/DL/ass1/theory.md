# Assignment 1: Linear Regression vs Neural Network (Boston Housing)

Problem:
Predict house prices using (a) Linear Regression and (b) a feedforward neural network. Preprocess data, train both models, and compare metrics.

Expected Output:
- Data preprocessing steps (scaling, train/test split)
- Linear Regression coefficients and evaluation (MSE, MAE, R²)
- Neural network architecture, training history, and evaluation metrics
- Sample prediction on a new scaled input

## Viva QnA
- Why scale features before training neural networks?: Scaling ensures similar feature ranges so gradients behave well and training converges faster.
- How do you interpret Linear Regression coefficients?: Coefficients give expected change in target per unit change in feature, holding others constant.
- What does R² indicate about model fit?: Proportion of variance explained by the model; 1 = perfect, 0 = no improvement over mean.
- Explain the NN architecture and role of ReLU and output layer.: ReLU adds non-linearity and avoids vanishing gradients; output layer for regression is linear to predict continuous values.
- Why use validation split and how to detect overfitting?: Validation monitors generalization; overfitting shows training loss decreasing while validation loss increases.
- How to compare models fairly?: Use same train/test split, same preprocessing, and compare identical metrics (MSE/MAE/R²) on test set.