import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("loyalty_customers.csv")
df["PointsExpiryDate"] = pd.to_datetime(df["PointsExpiryDate"])
df["LastPurchaseDate"] = pd.to_datetime(df["LastPurchaseDate"])

# Set current date
current_date = datetime(2025, 3, 28)
df["DaysToExpire"] = (df["PointsExpiryDate"] - current_date).dt.days

# Title and instructions
st.set_page_config(page_title="Loyalty Reminder Campaign", page_icon="📣", layout="centered")
st.title("📣 Loyalty Reminder Campaign Simulator")
st.markdown("Filter customers with expiring points and preview reminder messages.")

# Filter range
min_days = st.slider("Minimum days until point expiry", 0, 30, 7)
max_days = st.slider("Maximum days until point expiry", 7, 60, 30)

# Filter expiring customers
expiring_customers = df[(df["DaysToExpire"] >= min_days) & (df["DaysToExpire"] <= max_days)]

# Generate messages
expiring_customers["ReminderMessage"] = expiring_customers.apply(
    lambda row: f"Hi {row['CustomerName']}, your {row['PointsBalance']} points will expire in {row['DaysToExpire']} days. Redeem soon via {row['PreferredChannel']}!",
    axis=1
)

# Show total count
st.metric("📬 Customers to Remind", len(expiring_customers))

# Plot urgency buckets
bins = [0, 7, 15, 30, 60]
labels = ["0-7 days", "8-15 days", "16-30 days", "31-60 days"]
expiring_customers["UrgencyBucket"] = pd.cut(expiring_customers["DaysToExpire"], bins=bins, labels=labels, right=True)

fig, ax = plt.subplots()
expiring_customers["UrgencyBucket"].value_counts().sort_index().plot(kind="bar", color="#ff9999", ax=ax)
ax.set_title("Customers by Urgency Bucket")
ax.set_ylabel("Number of Customers")
ax.set_xlabel("Days to Expiry")
st.pyplot(fig)

# Display messages
toggle = st.checkbox("📋 Show Reminder Messages")
if toggle:
    st.dataframe(expiring_customers[["CustomerID", "CustomerName", "PointsBalance", "DaysToExpire", "PreferredChannel", "ReminderMessage"]].reset_index(drop=True))

# Footer
st.markdown("---")
st.caption("Simulated by Khwanchat | Dataset: loyalty_customers.csv")
