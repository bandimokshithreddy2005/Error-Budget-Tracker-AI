<p align="center">
#🚨 Error Budget Tracker with AI
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit" />
<img src="https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Google-Gemini%20AI-green?style=for-the-badge&logo=google" />
</p>

<h3 align="center">⚡ AI-Powered Site Reliability Engineering (SRE) Dashboard ⚡</h3>
<p align="center">Monitor Reliability • Track Error Budgets • Analyze Failures • Generate AI Reports</p>

👥 Team Squid
Name	Branch
Bandi Mokshith Reddy	AI & ML
Bavigadda Yamuna Lakshmi	CSE (AI)
Bellam Nikitha	AI & DS
Balaraju Sudhaveena	AI & DS


📌 Overview
Error Budget Tracker with AI is a Streamlit-based dashboard designed for Site Reliability Engineering (SRE) monitoring and reliability analysis.

It empowers engineering teams to:

✅ Monitor service health

🎯 Calculate error budgets

📊 Visualize reliability metrics

🤖 Generate AI-powered operational reports using Google Gemini AI

✨ Features
📂 CSV Log Upload & Processing

📊 Success & Failure Rate Calculation

🎯 Error Budget Monitoring

🔥 Burn Rate Analysis

🔍 Service-wise Filtering

📈 Interactive Data Visualization

🥧 Success vs Failure Pie Chart

📉 Service-wise Failure Analysis

📋 Budget Utilization Trend Tracking

🤖 AI-Powered SRE Report Generation

⚡ Real-Time Reliability Insights

🖥️ Dashboard Modules
<details>
<summary>📄 Log Data Viewer</summary>

Upload CSV log files

View processed request data

Highlight Success and Failed requests
</details>

<details>
<summary>📊 Metrics Dashboard</summary>

Total Requests

Success Rate

Failure Rate

Budget Utilization
</details>

<details>
<summary>📈 Visual Insights</summary>

Success vs Failure Pie Chart

Service-wise Failure Analysis

Budget Utilization Trend
</details>

<details>
<summary>🤖 AI Report Generator</summary>
Generates professional SRE reports including:

Executive Summary

Reliability Assessment

Risk Analysis

Burn Rate Evaluation

Actionable Recommendations
</details>

🛠️ Tech Stack
Technology	Usage
🐍 Python	Backend Processing
🎨 Streamlit	Interactive Dashboard
📊 Pandas	Data Analysis
📈 Matplotlib	Data Visualization
🤖 Google Gemini AI	AI Report Generation


📂 Project Structure
text
Error-Budget-Tracker-AI/
│
├── README.md                # Project documentation
├── prompts.md               # AI prompt templates
├── AI_USAGE_NOTE.md         # Notes on AI usage guidelines
├── LLM_EXAMPLES.md          # Example prompts & outputs
├── requirements.txt         # Python dependencies
├── sample_logs.csv          # Example log file for testing
├── streamlit_app.py         # Main Streamlit dashboard app
├── app.py                   # Core application logic
├── analyzer.py              # Reliability metrics analyzer
├── ai_report.py             # AI-powered report generator
├── generate_logs.py         # Utility to generate sample logs
├── monthly_logs.csv         # Example monthly log dataset
├── ai_input.txt             # Input file for AI report generation
│
├── tests/                   # Unit tests
│   └── test_basic.py        # Basic functionality tests
│
├── outputs/                 # Generated outputs
│   ├── dashboard.png        # Dashboard screenshot
│   ├── ai_report.png        # AI report screenshot
│   └── ai_report.md         # Sample AI-generated report
│
└── DEMO VIDEO LINK          # Link to demo video

🚀 Installation
bash
# Clone Repository
git clone https://github.com/YOUR_USERNAME/Error-Budget-Tracker-AI.git  

# Install Dependencies
pip install -r requirements.txt  

# Run the Application
streamlit run streamlit_app.py  
🎥 Demo
Dashboard Preview: http://localhost:8501/

Demo Video: Watch Here

📊 Sample Metrics
Metric	Value
✅ Success Rate	99.2%
❌ Error Rate	0.8%
🔥 Burn Rate	0.8
🎯 Remaining Budget	20%


🔮 Future Enhancements
🔔 SLA Breach Prediction (ML)

📡 Real-Time Monitoring

📧 Email Alert System

⚠️ Incident Prediction

📊 Advanced Analytics Dashboard

🛠️ Multi-Service Monitoring

🤖 Automated Reliability Recommendations

📚 Documentation
README.md

prompts.md

AI_USAGE_NOTE.md

LLM_EXAMPLES.md

tests/test_basic.py

⭐ Support
If you found this project useful, please give it a Star ⭐ on GitHub!
