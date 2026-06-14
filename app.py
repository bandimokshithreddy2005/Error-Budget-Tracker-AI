from flask import Flask, render_template
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_metrics():
    df = pd.read_csv("logs.csv")

    total_requests = len(df)
    success_requests = len(df[df["status"] == "Success"])
    failed_requests = len(df[df["status"] == "Failed"])

    success_rate = (success_requests / total_requests) * 100
    error_rate = (failed_requests / total_requests) * 100

    allowed_error_rate = 1
    burn_rate = error_rate / allowed_error_rate

    failed_df = df[df["status"] == "Failed"]
    top_service = failed_df["service"].value_counts().idxmax()

    remaining_budget = max(0, 100 - (error_rate / allowed_error_rate) * 100)
    weeks_left = remaining_budget / burn_rate if burn_rate > 0 else 0

    forecast_date = datetime.now() + timedelta(weeks=weeks_left)

    return {
        "success_rate": round(success_rate, 2),
        "error_rate": round(error_rate, 2),
        "burn_rate": round(burn_rate, 2),
        "top_service": top_service,
        "forecast_date": forecast_date.strftime("%d-%b-%Y")
    }

@app.route("/")
def home():
    data = calculate_metrics()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)