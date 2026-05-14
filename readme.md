# 🏦 CreditGuard AI — Enterprise Risk Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An end-to-end **Machine Learning-powered Credit Risk Assessment System** built for modern financial institutions.  
CreditGuard AI predicts the likelihood of loan default using a **Gradient Boosting Classifier**, while providing **Explainable AI (XAI)** insights for each decision to ensure transparency, auditability, and regulatory compliance.

---

# 📌 Overview

Financial institutions process thousands of loan applications daily, and inaccurate risk assessment can lead to substantial **Non-Performing Assets (NPAs)**.

CreditGuard AI addresses this challenge by combining:

- Predictive analytics
- Explainable AI
- REST API deployment
- Interactive business dashboard

The platform enables banks to:

✅ Evaluate customer default risk in real time  
✅ Understand model reasoning behind every prediction  
✅ Process single or bulk applications  
✅ Integrate directly with banking systems  

---

# 🚀 Key Features

## 1. Intelligent Loan Default Prediction
- Predicts whether a customer is likely to default
- Uses historical financial attributes
- High-performance ensemble learning model

## 2. Explainable AI Engine
Provides transparent reasons for rejection such as:

- Low annual income
- High debt-to-income ratio
- Poor credit score
- Insufficient savings balance
- High existing liabilities

## 3. Dual User Interface

### Manual Assessment
Bank staff can enter individual applicant data manually.

### Bulk CSV Processing
Upload applicant datasets for:

- Batch evaluation
- Portfolio screening
- Risk auditing

## 4. API-Ready Architecture
FastAPI backend allows integration with:

- Core Banking Systems (CBS)
- Loan Management Systems
- Mobile banking apps
- Internal dashboards

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │  (Frontend Layer)   │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │   (Service Layer)   │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ ML Prediction Engine│
                    │ Gradient Boosting   │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Explainability Core │
                    │  Reason Generator   │
                    └─────────────────────┘