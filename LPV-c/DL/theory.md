# LPV-c DL: Assignment Theory Overview

This folder contains the DL assignment notebooks (ass1..ass4). The theory and expectations mirror LPV-a DL assignments:

- ass1: Boston Housing — Linear Regression vs Neural Network, preprocessing, metrics.
- ass2: MNIST & IMDB — dense models for image and text, preprocessing and evaluation.
- ass3: Fashion-MNIST CNN — Conv2D/MaxPool/Dropout architecture and accuracy reporting.
- ass4: LSTM for stock prediction — windowing, scaling, LSTM training, inverse transform.

See LPV-a/DL `ass*/theory.md` files for per-assignment problem statements, expected outputs, and viva QnA.

## Viva QnA (summary)
- Linear Regression vs NN: scale inputs, compare on same test split; NN can capture non-linearities but needs regularization.
- MNIST/IMDB: normalize inputs, one-hot/softmax for multi-class, vectorize text or use embeddings for better results.
- CNNs: preserve spatial structure via 2D tensors, use convolution + pooling + dropout to generalize.
- LSTMs: use sliding windows and scale data; `return_sequences` for stacking and repeat-inverse-transform for predictions.