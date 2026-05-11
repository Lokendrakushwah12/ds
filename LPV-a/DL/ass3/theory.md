# Assignment 3: CNN for Fashion-MNIST

Problem:
Implement a Convolutional Neural Network (Conv2D, MaxPool, Dropout, Dense) to classify Fashion-MNIST images and report accuracy and loss.

Expected Output:
- Preprocessed data tensors (shape: samples,28,28,1)
- Trained CNN model and validation curves
- Test accuracy and sample predictions (class labels)

## Viva QnA
- What advantage do CNNs have over dense networks for images?: CNNs exploit spatial locality and weight sharing, dramatically reducing parameters and improving generalization on images.
- Explain convolution, pooling, and weight sharing.: Convolution applies local filters to produce feature maps; pooling downsamples spatially; weight sharing uses same filter across positions.
- Why reshape images to (28,28,1) rather than flatten?: To preserve spatial structure so convolutions can extract local features.
- What are common kernel sizes and why choose 3×3?: 3×3 is a good trade-off between receptive field and parameter count; stacking 3×3 approximates larger receptive fields.
- How does dropout reduce overfitting?: Randomly drops activations during training so network learns redundant, robust features.
- How to interpret confusion matrix?: Rows = true classes, columns = predicted; diagonal high means correct predictions; off-diagonal shows common confusions.