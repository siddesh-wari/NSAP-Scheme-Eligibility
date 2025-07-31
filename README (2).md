
# NSAP Eligibility Prediction 🧠🌐




## 🧩 Problem Statement

The National Social Assistance Programme (NSAP) provides financial assistance to elderly, widows, and persons with disabilities. However, identifying the most appropriate scheme (like IGNDPS, IGNOAPS, etc.) for beneficiaries based on district/state-wise data is manual, time-consuming, and error-prone.

> Goal: Automate the prediction of the eligible NSAP scheme using historical data and machine learning.

## 💡 Proposed Solution
We built a multiclass classification machine learning model using IBM AutoAI on Watsonx.ai Studio to predict the most suitable NSAP scheme (schemecode) for a given demographic and geographic input. The model was deployed and made publicly accessible through an online interface for predictions.

## 🔧 Technologies Used
Python (Auto-generated via AutoAI)

Jupyter Notebook (optional for code viewing)

CSV for dataset

JSON for prediction output


##  ☁️ IBM Cloud Services

IBM Watsonx.ai (AutoAI): For model training and experiment automation

Watson Machine Learning (WML): Model deployment and API endpoint

Cloud Object Storage (COS): Dataset handling and upload
## 🧑‍💼 End Users

Government departments for welfare program targeting

Data analysts in social services

NGO stakeholders to evaluate scheme reachability

Policy makers monitoring scheme distribution
## 🚀 Wow Factor

Fully automated AI/ML pipeline using IBM AutoAI — no manual coding required!

Real-time prediction of scheme eligibility through a user-friendly test UI

Model confidence scores add transparency and interpretability

Easily deployable and scalable as an API



##  🌟 Key Features

Multiclass classification for schemecode prediction

Uses demographic attributes like state, district, and gender distribution

Snap Random Forest Classifier selected for optimal accuracy

Simple UI for input data and prediction output

JSON format support for integration
##  ⚙️ How It Works
1. Upload Dataset (nsapallschemes.csv)


2. AutoAI Workflow:

Data split: 90% training, 10% holdout

Pipeline generation with multiple algorithms

Hyperparameter tuning and feature engineering

Snap Random Forest Classifier selected (best pipeline)



3. Deployment:

Model deployed to IBM Cloud

API and UI made available for testing



4. Prediction:

Input: State, district, year, gender stats, etc.

Output: Predicted NSAP Scheme Code with confidence %


## 📸 Screenshots

## 🧠 Train-Test Split Visualization

<img width="100%" alt="AutoAI Pipeline" src="https://github.com/user-attachments/assets/3f90d2f4-98c6-4a91-8dca-2b3d1a6dd2da" />

---

## 🔄 AutoAI Pipeline Overview

<img width="100%" alt="Input Data" src="https://github.com/user-attachments/assets/fdd06d1d-8204-4b03-a976-748ce9ce5356" />

---

## 🧪 Input Dataset Sample

<img width="100%" alt="Prediction Output" src="https://github.com/user-attachments/assets/b4b38b43-e140-4731-a9be-eddbd81f8e92" />

---

## ✅ Prediction Output


<img width="100%" alt="Train-Test Split" src="https://github.com/user-attachments/assets/992ae882-c0fd-460f-a7f7-18d276c0b610" />

---

## 🏃‍♀️ How to Run and Deploy
1. Log in to IBM Cloud


2. Launch Watson Studio → Create a new project


3. Upload nsapallschemes.csv to Assets


4. Use AutoAI Experiment to:

Select schemecode as target column

Let AutoAI train and rank pipelines



5. Select the best model (e.g., Snap Random Forest Classifier)


6. Deploy model → Create deployment space → Deploy as web service


7. Test via UI or send data as JSON to the model endpoint

##  🔮 Future Scope
Expand to support real-time data streaming

Add visualization dashboards for prediction trends

Introduce interpretability with SHAP or LIME

Support regional languages in UI

Integrate with mobile apps for rural outreach

##  🔗 Useful Link
1. IBM Watson Studio
https://cloud.ibm.com/catalog/services/watson-studio


2. NSAP Official Website
https://nsap.nic.in/


3. IBM AutoAI Documentation
https://www.ibm.com/docs/en/watson-studio


4. IBM Cloud (Login)
https://cloud.ibm.com/


5. IBM Watsonx.ai Overview
https://www.ibm.com/products/watsonx-ai


6. Open Government Data (OGD) Platform India
https://data.gov.in/
