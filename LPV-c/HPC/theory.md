# Plant Disease Detection using Deep Learning — Viva Questions & Answers

## 1. What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses multi-layer neural networks to learn patterns from data.

---

## 2. What is CNN?

CNN (Convolutional Neural Network) is a deep learning algorithm mainly used for image processing and classification.

---

## 3. Why is CNN used in plant disease detection?

Because CNN automatically extracts important features from leaf images like:

* spots
* color changes
* texture
* edges

---

## 4. What is image classification?

Image classification means assigning an image to a specific category or class.

Example:

* Healthy leaf
* Early blight
* Late blight

---

## 5. What is convolution?

Convolution is the process of applying filters/kernels to extract important image features.

(I*K)(x,y)=\sum_m\sum_n I(x-m,y-n)K(m,n)

---

## 6. What is a kernel/filter in CNN?

A small matrix used to detect patterns like:

* edges
* corners
* textures

---

## 7. What is ReLU activation function?

ReLU removes negative values.

f(x)=\max(0,x)

Advantages:

* Fast training
* Solves vanishing gradient problem

---

## 8. What is pooling?

Pooling reduces image dimensions and computation.

Types:

* Max Pooling
* Average Pooling

---

## 9. What is Max Pooling?

Selects the maximum value from feature maps.

Benefits:

* Reduces dimensions
* Keeps important features

---

## 10. What is flattening?

Converts 2D feature maps into 1D vector before giving data to dense layer.

---

## 11. What is a Dense layer?

Fully connected neural network layer used for final classification.

---

## 12. What is Softmax?

Softmax converts outputs into probabilities.

P(y_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}

---

## 13. What is an epoch?

One complete pass through the training dataset.

---

## 14. What is batch size?

Number of images processed at one time during training.

Example:

```text
batch_size = 32
```

---

## 15. What is overfitting?

Model performs very well on training data but poorly on new data.

---

## 16. How to reduce overfitting?

Methods:

* Dropout
* Data augmentation
* More dataset
* Early stopping

---

## 17. What is Dropout?

Randomly disables neurons during training to reduce overfitting.

---

## 18. What is data augmentation?

Creating modified copies of images:

* rotation
* zoom
* flip
* shift

Used to improve accuracy.

---

## 19. Why normalize images?

To scale pixel values between 0 and 1 for faster learning.

---

## 20. What is the role of optimizer?

Optimizer updates weights to minimize loss.

Example:

```text
Adam Optimizer
```

---

## 21. What is loss function?

Measures prediction error of model.

---

## 22. Why categorical crossentropy is used?

Used for multi-class classification problems.

---

## 23. Difference between ANN and CNN?

| ANN                   | CNN                          |
| --------------------- | ---------------------------- |
| Used for tabular data | Used for images              |
| No feature extraction | Automatic feature extraction |
| More parameters       | Fewer parameters             |

---

## 24. What is feature extraction?

Finding important patterns from images automatically.

---

## 25. What is TensorFlow?

An open-source deep learning framework developed by Google.

---

## 26. What is Keras?

High-level API of TensorFlow used for building neural networks easily.

---

## 27. Why use ImageDataGenerator?

Used for:

* preprocessing
* augmentation
* loading images in batches

---

## 28. What is accuracy?

Percentage of correctly predicted images.

Accuracy=\frac{Correct\ Predictions}{Total\ Predictions}

---

## 29. What dataset did you use?

PlantVillage Dataset.

---

## 30. Applications of plant disease detection?

Applications:

* Smart farming
* Precision agriculture
* Crop monitoring
* Early disease detection
* Yield improvement

---

# Most Important Viva Questions

Usually asked by external examiner:

1. Why CNN instead of ANN?
2. What is pooling?
3. Why ReLU?
4. What is overfitting?
5. What is augmentation?
6. Explain CNN architecture.
7. Difference between training and testing data.
8. What optimizer did you use?
9. What is softmax?
10. Why deep learning for images?
