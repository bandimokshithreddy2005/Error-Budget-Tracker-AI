# Prompt Engineering Documentation

## Overview

This document describes the prompts used in the Error Budget Tracker with AI project.

The system utilizes Google Gemini AI to generate Site Reliability Engineering (SRE) reports based on service reliability metrics and error budget consumption.

---

## Prompt Name

**SRE Weekly Error Budget Analysis Report**

---

## Objective

To generate a structured reliability assessment report that helps engineering teams understand service health, identify operational risks, and improve reliability practices.

---

## Input Parameters

The following metrics are dynamically passed to the AI model:

* Success Rate (%)
* Error Rate (%)
* Burn Rate
* Top Failure Service
* Remaining Error Budget (%)

---

## Prompt Template

Generate a professional SRE Weekly Error Budget Report.

Inputs:

* Success Rate
* Error Rate
* Burn Rate
* Top Failure Service
* Remaining Budget

Provide the report in the following format:

1. Executive Summary
2. Risk Assessment
3. Reliability Analysis
4. Recommendations

---

## Expected Output

The AI-generated report includes:

* Service Reliability Summary
* Error Budget Consumption Analysis
* Operational Risk Evaluation
* Recommended Corrective Actions

---

## AI Model

Google Gemini 2.5 Flash

---

## Use Case

The generated report assists Site Reliability Engineers (SREs), DevOps teams, and system administrators in monitoring reliability performance and making informed operational decisions.
