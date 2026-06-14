import pandas as pd
import random
from datetime import datetime, timedelta

# =========================
# CONFIG
# =========================
services = ["PaymentAPI", "OrderAPI", "UserAPI", "AuthAPI", "InventoryAPI"]
statuses = ["Success", "Failed"]

data = []

start_date = datetime(2026, 6, 1)
days_in_month = 30

# =========================
# GENERATE DATA
# =========================
for day in range(days_in_month):

    current_day = start_date + timedelta(days=day)

    week_number = (day // 7) + 1
    week_label = f"W{week_number}"

    for i in range(7):

        service = random.choice(services)
        status = random.choices(statuses, weights=[70, 30])[0]

        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        timestamp = current_day.replace(hour=hour, minute=minute, second=second)

        data.append([week_label, timestamp, service, status])

# =========================
# CREATE DATAFRAME
# =========================
df = pd.DataFrame(data, columns=["Week", "timestamp", "service", "status"])

df = df.sort_values("timestamp")

# =========================
# ONLY ONE CSV OUTPUT
# =========================
df.to_csv("monthly_logs.csv", index=False)

print("✅ ONLY ONE FILE CREATED: monthly_logs.csv")