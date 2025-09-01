# 🐱🐶 Cat vs Dog Image Classifier

This project is a **Convolutional Neural Network (CNN)** built using **TensorFlow and Keras** to classify images of cats and dogs.  
It uses **ImageDataGenerator** for preprocessing, augmentation, and feeding data into the model, helping reduce overfitting and improve generalization.

---

## 📂 Dataset
The dataset is divided into three folders:
- **train/** → 2000 labeled images (cats and dogs)
- **validation/** → 1000 labeled images (cats and dogs)
- **test/** → 50 unlabeled images (for final predictions)

Each image is resized to `(150, 150)` pixels and rescaled from `[0, 255]` to `[0, 1]`.

---

## 🔧 Preprocessing
- Used `ImageDataGenerator` with:
  - **Rescaling** (normalize pixel values)
  - **Data augmentation** (rotation, shifting, zoom, flipping, shearing, etc.) for the training set
- Validation and test sets were only rescaled.

---

## 🧠 Model Architecture
Built with **Keras Sequential API**:

1. **Convolutional + MaxPooling Layers**
   - Conv2D(32) + MaxPooling2D  
   - Conv2D(64) + MaxPooling2D  
   - Conv2D(128) + MaxPooling2D  

2. **Fully Connected Layers**
   - Flatten  
   - Dense(512, ReLU)  
   - Dropout(0.5) to reduce overfitting  
   - Dense(1, Sigmoid) → outputs probability of "dog" vs "cat"

---

## ⚙️ Compilation
- **Optimizer:** Adam  
- **Loss:** Binary Crossentropy  
- **Metrics:** Accuracy  

---

## 📈 Training
- **Batch size:** 128  
- **Epochs:** 15 (can be adjusted)  
- Monitored **training accuracy** and **validation accuracy** each epoch.  
- Observed that data augmentation improved generalization and reduced overfitting.  

---

## 🧪 Testing
- Predictions were made on the **50 test images** using the trained model.  
- Each image was displayed with a label showing how confident the model was that the image is a **cat or dog**.  
- Example:  
  - `92.00% dog`  
  - `88.00% cat`

---

## 🚀 Future Improvements
- Use a deeper CNN or pretrained models (e.g., VGG16, ResNet, MobileNet) for higher accuracy.  
- Collect more training images to reduce overfitting further.  
- Experiment with different optimizers, learning rates, and regularization techniques.

---

## 📌 Requirements
- Python 3.x  
- TensorFlow (>=2.0)  
- Keras  
- Matplotlib, NumPy  

---

## 🖼️ Results
The final test set predictions aligned closely with validation accuracy. With more training data or transfer learning, the model can achieve even higher performance.
