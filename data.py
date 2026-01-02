import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------
# Configuration
# -------------------------
NUM_LEADS = 500
NUM_DEALS = 350
NUM_ACTIVITIES = 600

industries = ["IT", "Finance", "Healthcare", "Education", "Retail", "Manufacturing"]
sources = ["Website", "Email", "Referral", "Social Media", "Google Ads", "LinkedIn Ads", "Cold Call", "Events"]
statuses = ["New", "Qualified", "Proposal", "Converted", "Lost"]
activity_types = ["Call", "Email", "Meeting"]

company_names = [
    "Tata Solutions", "Infosys Ltd", "Wipro Systems", "Reliance Digital",
    "HCL Technologies", "Tech Mahindra", "Flipkart India", "Byju's",
    "Paytm Services", "Zomato Pvt Ltd", "Swiggy Instamart", "ICICI Tech",
    "HDFC Analytics", "Axis Solutions", "L&T Infotech", "Mindtree",
    "Persistent Systems", "Udaan Pvt Ltd", "Ola Electric", "Airtel Digital"
]

start_date = datetime(2024, 1, 1)

# -------------------------
# Leads Table
# -------------------------
leads_data = []
for i in range(1, NUM_LEADS + 1):
    lead_id = f"L{i:04d}"
    name = random.choice(company_names) + f" {i}"
    industry = random.choice(industries)
    source = random.choice(sources)
    created_date = start_date + timedelta(days=random.randint(0, 365))
    status = random.choice(statuses)
    lead_score = random.randint(20, 100)

    leads_data.append([lead_id, name, industry, source, created_date.date(), status, lead_score])

leads_df = pd.DataFrame(
    leads_data,
    columns=["lead_id", "lead_name", "industry", "source", "created_date", "status", "lead_score"]
)

# -------------------------
# Deals Table
# -------------------------
deals_data = []
converted_leads = leads_df.sample(NUM_DEALS)

for i, row in enumerate(converted_leads.itertuples(), start=1):
    deal_id = f"D{i:04d}"
    deal_size = random.randint(50000, 500000)
    stage = random.choice(["Negotiation", "Closed Won", "Lost"])
    close_date = row.created_date + timedelta(days=random.randint(10, 120))

    deals_data.append([deal_id, row.lead_id, deal_size, stage, close_date])

deals_df = pd.DataFrame(
    deals_data,
    columns=["deal_id", "lead_id", "deal_size", "stage", "close_date"]
)

# -------------------------
# Activities Table
# -------------------------
activities_data = []
for i in range(1, NUM_ACTIVITIES + 1):
    activity_id = f"A{i:04d}"
    lead_id = random.choice(leads_df["lead_id"])
    activity_type = random.choice(activity_types)
    activity_date = start_date + timedelta(days=random.randint(0, 365))

    activities_data.append([activity_id, lead_id, activity_type, activity_date.date()])

activities_df = pd.DataFrame(
    activities_data,
    columns=["activity_id", "lead_id", "activity_type", "activity_date"]
)

# -------------------------
# Sources Table
# -------------------------
sources_df = pd.DataFrame({
    "source_id": range(1, len(sources) + 1),
    "source_name": sources
})

# -------------------------
# Save CSV Files
# -------------------------
leads_df.to_csv("leads.csv", index=False)
deals_df.to_csv("deals.csv", index=False)
activities_df.to_csv("activities.csv", index=False)
sources_df.to_csv("sources.csv", index=False)

print("✅ CRM Dataset Generated Successfully!")
