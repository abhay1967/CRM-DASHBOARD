# 📊 CRM Analytics Dashboard (Power BI)

A complete **CRM Analytics Dashboard** built using **Power BI**, **SQL**, and **CSV datasets** to analyze lead performance, deal values, conversion metrics, and business KPIs.

This project demonstrates **end-to-end data analysis** — from raw CSV ingestion and SQL querying to interactive dashboard visualization.

---

## 🚀 Project Overview

The CRM Dashboard provides insights into:

- Total leads and lead status distribution  
- Conversion rate and average deal size  
- Lead aging analysis  
- Industry-wise lead segmentation  
- Lead source performance  
- High-value deal identification  

It is designed for **sales teams, business analysts, and decision-makers** to quickly understand CRM performance and trends.

---

## 🛠 Tools & Technologies Used

- **Power BI Desktop**
- **SQL (MySQL syntax)**
- **CSV Data Sources**
- **Python (optional preprocessing)**
- **Relational Data Modeling**

---

## 📂 Project Structure
CRM-DASHBOARD/
├── abhaykadashboard.pbix # Power BI dashboard file
├── activities.csv # CRM activities data
├── leads.csv # Leads dataset
├── deals.csv # Deals dataset
├── sources.csv # Lead sources data
├── crm_queries.sql # SQL queries for KPI analysis
├── data.py # Optional data preprocessing script
├── screenshots/ # Dashboard & SQL query screenshots
└── README.md # Project documentation

---

## 📊 Dashboard KPIs & Visuals

### 🔹 Key Metrics
- **Total Leads**
- **Conversion Rate**
- **Average Deal Size**
- **Average Lead Age**

### 🔹 Visualizations
- Leads by Industry (Bar Chart)
- Lead Source Distribution (Donut Chart)
- Lead Status Breakdown
- High-Value Leads Table
- Interactive Filters (Industry & Status)

---

## 🧮 SQL Analysis Highlights

Key SQL queries include:

- **Top 100 High-Value Leads**
- **Lead Aging (KPI)**
- **Conversion Rate Calculation**
- **Industry & Status-wise Aggregation**

Example:
```sql
SELECT 
  l.lead_id,
  l.lead_name,
  l.industry,
  d.deal_size
FROM leads l
JOIN deals d ON l.lead_id = d.lead_id
ORDER BY d.deal_size DESC
LIMIT 100;

