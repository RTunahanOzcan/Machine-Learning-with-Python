# SMS Spam Classifier (Ham vs Spam)

This project builds a machine learning model using TensorFlow/Keras to classify SMS messages as either **ham** (normal message) or **spam** (advertisement or unwanted message). The dataset used is the [SMS Spam Collection Dataset], which is already split into training and test sets (`train_file`, `test_file`).

---

## 📌 Project Overview
- **Goal**: Classify SMS messages into two categories: `ham` or `spam`.
- **Input**: A text message string (e.g., "You have won £1000 cash!").
- **Output**: 
  1. A probability score between `0` and `1` (closer to 1 → spam).
  2. The predicted label `"ham"` or `"spam"`.

---

## 🛠️ Approach
1. **Preprocessing**
   - Use Keras `TextVectorization` to tokenize text, lower-case, strip punctuation, and pad/truncate sequences to a fixed length (`output_len=120`).
   - Vocabulary size is limited to `20,000` most frequent words as `max_tokens`.

2. **Model Architecture**
   - Input: Raw text string
   - `TextVectorization` → integer sequence
   - `Embedding` layer (64-dim vectors)
   - `Bidirectional LSTM` layers to capture context from both directions
   - `Dense (ReLU)` + `Dropout` for regularization
   - Output: `Dense(1, sigmoid)` → probability of spam

3. **Training**
   - Loss: `binary_crossentropy`
   - Optimizer: `adam`
   - Metrics: `accuracy`
   - Epochs: 5 (can be adjusted manually)
   - Batch size: 16

4. **Prediction**
   - Implemented `predict_message(message)` function:
     - Takes a string input
     - Returns `[probability, "ham"/"spam"]`

---

## 📊 Results
- Achieves ~90–99% accuracy depending on hyperparameters and training duration.
- Handles raw text directly — no manual preprocessing required.

---

## 🚀 Usage
Example:

```python
prediction = predict_message("Congratulations! You have won free tickets!")
print(prediction)
# Example output: [0.93, "spam"]
