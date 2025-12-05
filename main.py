import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------

def create_all_plots(df):

    # Daily temperature line chart
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df["temperature"])
    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.savefig("outputs/plots/daily_temperature.png")
    plt.close()

    # Monthly rainfall bar chart
    monthly_rain = df["rainfall"].resample("M").sum()
    plt.figure(figsize=(10, 5))
    plt.bar(monthly_rain.index, monthly_rain)
    plt.title("Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.savefig("outputs/plots/monthly_rainfall.png")
    plt.close()

    # Scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df["temperature"], df["humidity"])
    plt.title("Humidity vs Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.savefig("outputs/plots/humidity_vs_temperature.png")
    plt.close()

    # Combined plot
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df["temperature"], label="Temperature")
    plt.plot(df.index, df["humidity"], label="Humidity")
    plt.title("Combined Temperature & Humidity")
    plt.xlabel("Date")
    plt.legend()
    plt.savefig("outputs/plots/combined_plot.png")
    plt.close()

#---------------------------------------------

def generate_statistics(df):
    stats = {
        "mean": df.mean(),
        "min": df.min(),
        "max": df.max(),
        "std": df.std(),
        "monthly": df.resample("M").mean(),
        "yearly": df.resample("Y").mean()
    }
    return stats

#---------------------------------------------

def save_summary_report(df, stats):
    summary = f"""
WEATHER DATA ANALYSIS REPORT
----------------------------

Mean Values:
{stats['mean']}

Minimum Values:
{stats['min']}

Maximum Values:
{stats['max']}

Standard Deviation:
{stats['std']}

(See cleaned CSV and plots inside the outputs folder)
"""

    with open("outputs/reports/summary_report.txt", "w") as f:
        f.write(summary)

#---------------------------------------------

def load_and_clean_data():
    df = pd.read_csv("data/raw_weather.csv")

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Keep important columns
    df = df[["temperature", "rainfall", "humidity"]]

    # Handle missing values
    df = df.fillna(method="ffill")

    # Save cleaned file
    df.to_csv("data/cleaned_weather.csv")

    return df

#---------------------------------------------

def main():
    print("Loading and cleaning data...")
    df = load_and_clean_data()

    print("Generating statistics...")
    stats = generate_statistics(df)

    print("Creating visualizations...")
    create_all_plots(df)

    print("Saving summary report...")
    save_summary_report(df, stats)

    print("\nProject completed successfully!")
    print("Check the 'outputs/' folder for plots and reports.")

if __name__ == "__main__":
    main()
