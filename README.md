<p align="center">
  <img src="https://github.com/user-attachments/assets/your_logo_here" alt="NSAP Logo" height="60">
</p>

<h1 align="center">NSAP Scheme Eligibility Predictor</h1>

<p align="center">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/NSAP-Scheme-Eligibility?style=social">
  <img src="https://img.shields.io/github/forks/YOUR_USERNAME/NSAP-Scheme-Eligibility?style=social">
  <img src="https://img.shields.io/github/issues/YOUR_USERNAME/NSAP-Scheme-Eligibility">
  <img src="https://img.shields.io/github/license/YOUR_USERNAME/NSAP-Scheme-Eligibility">
</p>

---

## 📌 About the Project
This project predicts **the most suitable NSAP welfare scheme** for applicants based on their **demographic and socio-economic details** using an AI/ML pipeline built with **IBM Watsonx AutoAI Studio**.

🚀 **Deployed App:** [Add your app link here]  
📂 **GitHub Repo:** [https://github.com/YOUR_USERNAME/NSAP-Scheme-Eligibility](https://github.com/YOUR_USERNAME/NSAP-Scheme-Eligibility)

---

## 📸 Project Preview
| Model Training (AutoAI) | Data Processing |
|-------------------------|-----------------|
| <img src="Screenshot 2025-07-30 190226.png" width="600"> | <img src="Screenshot 2025-07-30 190330.png" width="600"> |

---

## 🚀 Features
✅ **AI-based NSAP Scheme Prediction** using IBM Watsonx AutoAI  
✅ **Streamlit Web App** with interactive inputs and instant results  
✅ **Trained on socio-economic dataset (nsapallschemes.csv)**  
✅ **Clean UI with balloons animation** after prediction  

---

## 📊 Dataset Overview
The dataset includes the following features:  
- Age, Gender, Marital Status, Income  
- Disability, BPL Status, Number of Dependents  
- Scheme Code (Target Column)

Data preprocessing included:  
✔ Handling missing values  
✔ Label Encoding categorical variables  
✔ Scaling numeric features  

---

## 🤖 Model Details
| Model Type | Accuracy | Notes |
|------------|----------|-------|
| Random Forest | 90% | Best performing |
| XGBoost | 88% | Slightly lower accuracy |
| Decision Tree | 84% | Overfitting tendency |

> Final model selected: **Random Forest Classifier** (Accuracy = ~90%)  

---

## 📂 Project Structure
```
NSAP-Scheme-Eligibility/
├── app.py                     # Streamlit app for prediction
├── nsap_model_training.ipynb  # Notebook for training (AutoAI/Manual)
├── best_model.pkl             # Trained model file
├── dataset.csv                # Dataset used for training
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
```

---

## 🛠 Installation Guide

### 🔹 Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/NSAP-Scheme-Eligibility.git
cd NSAP-Scheme-Eligibility
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Run the App
```bash
streamlit run app.py
```

---

## 🌍 Deployment
- **IBM Watsonx AutoAI** → Model Training  
- **Render / Streamlit Cloud** → Deployment Platform  

---

## 👩‍💻 Author
👩‍💻 Developed by **YOUR NAME**  
🔗 [LinkedIn](https://linkedin.com/in/YOUR_USERNAME) | ✉️ yourmail@example.com  

---

⭐ **If you like this project, please give it a star on GitHub!** ⭐
