# 🚨 Error Budget Tracker with AI

<p align="center">
  <h3 align="center">AI-Powered Site Reliability Engineering (SRE) Dashboard</h3>
  <p align="center">
    Monitor Reliability • Track Error Budgets • Analyze Failures • Generate AI Reports
  </p>
</p>

---

## 👥 Team Details

### 🧑‍💻 Team Name: **Team Squid**

| Name | Branch |
|------|--------|
| Bandi Mokshith Reddy | AI&ML |
| Bavigadda Yamuna Lakshmi | CSE (AI) |
| Bellam Nikitha | AI&DS |
| Balaraju Sudhaveena | AI&DS |

---

## 📌 Overview

**Error Budget Tracker with AI** is a Streamlit-based dashboard designed for Site Reliability Engineering (SRE) monitoring and reliability analysis.

The application helps engineering teams monitor service health, calculate error budgets, visualize reliability metrics, and generate AI-powered operational reports using Google Gemini AI.

---

## ✨ Features

* 📂 CSV Log Upload & Processing
* 📊 Success Rate & Failure Rate Calculation
* 🎯 Error Budget Monitoring
* 🔥 Burn Rate Analysis
* 🔍 Service-wise Filtering
* 📈 Interactive Data Visualization
* 🥧 Success vs Failure Pie Chart
* 📉 Service-wise Failure Analysis
* 📋 Budget Utilization Trend Tracking
* 🤖 AI-Powered SRE Report Generation
* ⚡ Real-Time Reliability Insights

---

## 🖥️ Dashboard Modules

### 📄 Log Data Viewer
* Upload CSV log files  
* View processed request data  
* Highlight Success and Failed requests  

### 📊 Metrics Dashboard
* Total Requests  
* Success Rate  
* Failure Rate  
* Budget Utilization  

### 📈 Visual Insights
* Success vs Failure Pie Chart  
* Service-wise Failure Analysis  
* Budget Utilization Trend  

### 🤖 AI Report Generator
Generate professional SRE reports including:
* Executive Summary  
* Reliability Assessment  
* Risk Analysis  
* Burn Rate Evaluation  
* Actionable Recommendations  

---

## 🛠️ Technology Stack

| Technology       | Usage                 |
|----------------|----------------------|
| Python           | Backend Processing    |
| Streamlit        | Interactive Dashboard |
| Pandas           | Data Analysis         |
| Matplotlib       | Data Visualization    |
| Google Gemini AI | AI Report Generation  |

---

## 📂 Project Structure

```text
Error-Budget-Tracker-AI/
│
├── README.md
├── prompts.md
├── AI_USAGE_NOTE.md
├── LLM_EXAMPLES.md
├── requirements.txt
├── sample_logs.csv
├── streamlit_app.py
│
├── tests/
│   └── test_basic.py
│
└── output/
    ├── dashboard.png
    ├── ai_report.png
    └── ai_report.md
