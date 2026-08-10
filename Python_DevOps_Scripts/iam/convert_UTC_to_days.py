import pandas as pd
from datetime import datetime, timezone

# Read IAM credential report
df = pd.read_csv("credential_report.csv")

today = datetime.now(timezone.utc)

def calculate_days(date_value):

    if pd.isna(date_value):
        return "Never"

    last_used = pd.to_datetime(date_value)

    days = (today - last_used).days

    return days


df["console_last_used_days"] = df["password_last_used"].apply(calculate_days)

df["access_key_1_last_used_days"] = df["access_key_1_last_used_date"].apply(calculate_days)

df["access_key_2_last_used_days"] = df["access_key_2_last_used_date"].apply(calculate_days)


df.to_excel("iam_user_audit.xlsx", index=False)

print("IAM audit report generated successfully")