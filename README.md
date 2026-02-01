# 📩 SMS / Email Spam Classifier

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![Status](https://img.shields.io/badge/Status-Deployed-success)

This project is a machine learning–powered web application that classifies SMS or email messages as **Spam** or **Not Spam**.
It uses natural language processing (NLP) techniques with **TF-IDF vectorization** and classical machine-learning models, deployed as an interactive web app using **Streamlit**.

---

## 🚀 Live Demo

👉[![Live App](https://img.shields.io/badge/Live-Streamlit-success)] https://sms-spam-detection-by-shraddha.streamlit.app/

---

## 📌 Features

- Text preprocessing with NLTK  
- TF-IDF vectorization  
- Multiple models evaluated (Naive Bayes, SVM, ensembles, etc.)
- Final trained model used is naive bayes
- Interactive Streamlit interface  
- Cloud-deployable via GitHub  

---

## 🧠 Machine Learning Pipeline

1. Text cleaning & normalization  
2. Tokenization and stopword removal  
3. TF-IDF feature extraction  
4. Model training & evaluation  
5. Model serialization using Pickle  
6. Deployment using Streamlit  

---

## 📂 Project Structure

```bash
sms-spam-detection/
│
├── app.py # Streamlit app
├── model.pkl # Trained ML pipeline
├── vectorizer.pkl
├── requirements.txt # Dependencies
├── Sms_Spam_classifier.ipynb # Notebook
├── README.md # Project documentation
├── .gitignore
├── screenshots/ # App screenshots for README
```

# 🛡️ NLTK Resources

The app automatically downloads required NLTK resources (punkt, punkt_tab, and stopwords) at runtime so that tokenization works correctly in cloud deployments.

# 📊 Models Evaluated

Several models were trained and compared:

- Multinomial Naive Bayes

- Support Vector Machine

- Logistic Regression

- Random Forest

- Gradient Boosting

- Voting & Stacking Ensembles

The best-performing model was selected and deployed.

---

## ⚙️ Installation & Running Locally

### Clone the repository

```bash
git clone https://github.com/smshelar/sms-spam-detection.git
cd sms-spam-detection
```

## 🧪 Example Inputs
```bash
Spam
Congratulations! You have won a free voucher. Click now!
```

```bash
Not Spam
Hi, are we still meeting tomorrow afternoon?
```

# 🔮 Future Improvements

- Deep-learning–based text models

- Language detection

- Probability score display

- Model explainability (SHAP / feature importance)

- Dataset expansion

# 👩‍💻 Author
### Shraddha Shelar