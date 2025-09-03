# Healthcare Cost Prediction with TensorFlow

This project predicts individual healthcare expenses using a regression model built with TensorFlow and Keras. The dataset contains demographic and lifestyle information (such as age, sex, BMI, number of children, smoking status, and region) along with healthcare costs (`expenses`).  

The model learns from historical data to predict costs for new, unseen individuals.  

---

## 📂 Dataset

The dataset used is [`insurance.csv`](insurance.csv), which contains:

| Column   | Description |
|----------|-------------|
| age      | Age of the individual |
| sex      | Gender (male/female) |
| bmi      | Body Mass Index |
| children | Number of children covered by insurance |
| smoker   | Smoking status (yes/no) |
| region   | Residential region (northeast, northwest, southeast, southwest) |
| expenses | Actual medical costs billed |

---

## ⚙️ Steps Implemented

1. **Data Preprocessing**
   - Loaded dataset with Pandas.
   - Converted categorical columns (`sex`, `smoker`, `region`) into numerical values using one-hot encoding.
   - Split data into **80% training** and **20% testing**.
   - Separated `expenses` column as labels.

2. **Feature Scaling**
   - Applied normalization only to numeric features (`age`, `bmi`, `children`) using TensorFlow’s `Normalization` layer.
   - Concatenated normalized numeric features with categorical features.

3. **Model Architecture**
   - Built a neural network using Keras Functional API:
     - Input layer (numeric + categorical features).
     - Normalization layer for numeric features.
     - Dense layers with ReLU activations (`128 → 128 → 64`).
     - Output layer with 1 neuron (regression output).

4. **Training**
   - Optimizer: **Adam** (`lr=0.001`).
   - Loss function: **Mean Squared Error (MSE)**.
   - Metrics: **Mean Absolute Error (MAE)**.
   - Used **EarlyStopping** callback to prevent overfitting.

5. **Evaluation**
   - Evaluated on test dataset.
   - Achieved **MAE < 3500**, meaning predictions are within $3500 of the true healthcare costs on average.

6. **Visualization**
   - Plotted predicted vs. actual expenses to assess model performance.

---

## 🚀 Results

- The model generalizes well to unseen data.
- Achieved the challenge requirement of **MAE under 3500**.
- Visualization shows predictions closely align with actual expenses.

---

## 📊 Example Output

```text
Testing set Mean Abs Error: $ 3124.57
```

---

## 🛠️ Requirements

- Python 3.8+
- TensorFlow 2.x
- Pandas
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install tensorflow pandas numpy matplotlib
```

---

## ▶️ How to Run

1. Clone this repository or copy the notebook.
2. Place `insurance.csv` in the project directory.
3. Run the notebook cells step by step.
4. Check final evaluation and visualization of predictions.

---

## 📌 Notes

- This project demonstrates a **regression approach** to healthcare cost prediction.
- Feature scaling and careful preprocessing significantly impact model accuracy.
- Model can be further improved with **hyperparameter tuning** and **regularization** techniques.

---

✍️ **Author**: Recep Tunahan Özcan 
