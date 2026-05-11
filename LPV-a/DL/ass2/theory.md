# Assignment 2: MNIST OCR & IMDB Sentiment

Problem:
Build (a) dense neural network for MNIST digit recognition and (b) a text classification model for IMDB sentiment using vectorized inputs; train and report accuracy/loss.

Expected Output:
- Data preprocessing (reshape/normalize for MNIST; vectorize/one-hot for IMDB)
- Trained models with training/validation curves
- Final test accuracy and example predictions

## Viva QnA
- Why normalize image pixels and one-hot encode labels?: Normalization stabilizes training; one-hot encoding is required for categorical cross-entropy and softmax outputs.
- What is softmax and why used for MNIST output?: Softmax converts logits to a probability distribution across classes for multi-class classification.
- How is IMDB text vectorized and what are alternatives (embeddings)?: Simple vectorization uses one-hot word presence; alternatives include embeddings (Word2Vec, GloVe) or learned Embedding layers.
- Explain dropout and why used.: Dropout randomly disables neurons during training to prevent co-adaptation and reduce overfitting.
- How to interpret training vs validation accuracy curves?: If training >> validation, model overfits; if both low, underfitting; use curves to tune model capacity and regularization.
- How to improve model performance?: Use deeper/wider models, data augmentation, embeddings for text, hyperparameter tuning, and regularization.