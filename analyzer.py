import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv("logs.csv")

total_requests = len(df)

success_requests = len(df[df["status"] == "Success"])
failed_requests = len(df[df["status"] == "Failed"])

success_rate = (success_requests / total_requests) * 100
error_rate = (failed_requests / total_requests) * 100

allowed_error_rate = 1

budget_used = (error_rate / allowed_error_rate) * 100
burn_rate = error_rate / allowed_error_rate

# Top failure service
failed_df = df[df["status"] == "Failed"]
failure_counts = failed_df["service"].value_counts()
top_service = failure_counts.idxmax()

# Forecast
remaining_budget = max(0, 100 - budget_used)

if burn_rate > 0:
    weeks_left = remaining_budget / burn_rate
else:
    weeks_left = 999

forecast_date = datetime.now() + timedelta(weeks=weeks_left)

# Print summary
print("SUCCESS RATE:", round(success_rate, 2))
print("ERROR RATE:", round(error_rate, 2))
print("BURN RATE:", round(burn_rate, 2))
print("TOP SERVICE:", top_service)
print("FORECAST DATE:", forecast_date.strftime("%d-%b-%Y"))

# 👉 AI Report file ki save chestham
with open("ai_input.txt", "w") as f:
    f.write(f"""
Success Rate: {success_rate}
Error Rate: {error_rate}
Burn Rate: {burn_rate}
Top Service: {top_service}
Forecast Date: {forecast_date.strftime('%d-%b-%Y')}
""")