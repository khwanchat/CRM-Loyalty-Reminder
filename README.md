# 📣 CRM Loyalty Reminder App

A simple yet powerful Streamlit app to simulate a **loyalty reminder campaign** based on point expiration. Designed for marketers and CRM teams looking to build data-driven outreach strategies.

## 🚀 Live App

Check out the deployed dashboard here:  
👉 [RFM Segmentation Dashboard](https://crm-loyalty-reminder-6qefpdrqg4icqpktsmb7lv.streamlit.app/)

---

## ✨ Features

- 📊 Filters customers based on days to point expiry  
- 📨 Personalized reminder message preview  
- 📈 Urgency bar chart by expiry window  
- 📬 Channel segmentation: Email or SMS  
- 🧠 Real-time dashboard powered by Streamlit

---

## 🧾 Sample Use Case
> "Send reminders to customers whose points are expiring within the next 15 to 30 days, tailored by preferred channel (Email/SMS)."

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `loyalty_reminder_app.py` | Main Streamlit app |
| `loyalty_customers.csv` | Simulated customer loyalty dataset |
| `crm_remider.py` | Early version (backup/test script) |

---

## 📦 Requirements
Install dependencies with:
```bash
pip install -r requirements.txt
```

### Or manually:
```bash
pip install streamlit pandas matplotlib
```

---

## ▶️ Run Locally
```bash
streamlit run loyalty_reminder_app.py
```

---

## 📁 Dataset Preview
- 200 Customers
- Simulated point balances & expiry dates
- Channel preference: Email or SMS

---

## 👤 Author
**Khwanchat**  
Built as part of my portfolio for internship application.  
🔗 [GitHub Profile](https://github.com/khwanchat)

---

## 📝 License
MIT License
