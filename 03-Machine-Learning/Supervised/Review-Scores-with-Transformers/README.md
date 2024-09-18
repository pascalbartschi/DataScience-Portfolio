# Predicting Product Review Scores Using Transformer Models

## Project Description

This project aims to predict product review scores based on the review's title and content using machine learning techniques. The goal is to infer a continuous score between 0 and 10 for each review. The dataset consists of a training set containing review titles, content, and their associated scores, while the test set includes titles and content without scores.

The recommended approach utilizes the `transformers` library, exploring models such as DistilBERT, ALBERT, and GPT-2. While fine-tuning these models is encouraged for more realistic applications, using frozen weights is sufficient to meet the project's baseline. The task involves extracting embeddings from the pretrained transformers and saving them for subsequent model training. The code leverages the PyTorch deep learning framework and can be run on modern GPUs for efficient computation.

## Code Description

This script tackles an NLP problem where product reviews are used to predict scores ranging from 0 to 10. The preprocessing step involves using a lightweight spaCy model to clean the text, including stop-word removal, lemmatization, and handling negations. The preprocessed text data is split into training and validation sets in a 9:1 ratio.

The regression task is performed using the `DistilBERT` model, a variant of BERT. In the first layer of the regression network, the input is tokenized using the BERT tokenizer and passed through the model to obtain the CLS token representation in the hidden layer, which is then regularized using a dropout layer. Before producing the final output, this representation is passed through a linear layer. The network is trained in an alternating loop that calls `model.train()` and `model.eval()` to monitor the training process and avoid overfitting.

The population risk (loss on public, unseen data) of the final solution added up to 3.35 on 10k reviews.