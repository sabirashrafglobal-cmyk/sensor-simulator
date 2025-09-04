import os
import requests
import random
import time
from datetime import datetime, timezone

# Read Supabase info from environment variables
SUPABASE_URL = os.environ.get("https://crlyhftxibuzefhingij.supabase.co")
SUPABASE_API_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNybHloZnR4aWJ1emVmaGluZ2lqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY5NjkxMjIsImV4cCI6MjA3MjU0NTEyMn0.pa_FhGKUK40PNeb4iZNJUp14YoYht003GhGma6rTXiQ")

if not SUPABASE_URL or not SUPABASE_API_KEY:
    raise Exception("Please set SUPABASE_URL and SUPABASE_API_KEY environment variables.")

TABLE_NAME = "sensor_data"
DEVICE_ID = "python_simulator_01"

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
}

def send_random_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 70.0), 2)
    timestamp = datetime.now(timezone.utc).isoformat()

    data = {
        "device_id": DEVICE_ID,
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp,
    }

    url = f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Sent data: {data}")
    else:
        print(f"Failed to send data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    print("Starting sensor data simulator...")
    while True:
        send_random_sensor_data()
        time.sleep(10)  # Wait 10 seconds
