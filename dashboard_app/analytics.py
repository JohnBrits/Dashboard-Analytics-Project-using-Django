import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"\n✅ Successfully loaded '{file_path}'\n")
        return data
    except Exception as e:
        print(f"\n❌ Failed to load file: {e}")
        sys.exit(1)

def basic_info(data):
    print("🔹 Shape of the data:", data.shape)
    print("\n🔹 Column names:")
    print(data.columns.tolist())

    print("\n🔹 Data types:")
    print(data.dtypes)

def missing_values(data):
    print("\n🔹 Missing values (count):")
    print(data.isnull().sum())

def descriptive_stats(data):
    print("\n🔹 Descriptive statistics (numeric columns):")
    print(data.describe())

def plot_histograms(data, output_dir="plots"):
    numeric_cols = data.select_dtypes(include=["number"]).columns
    if not numeric_cols.any():
        print("\n⚠️ No numeric columns to plot.")
        return

    os.makedirs(output_dir, exist_ok=True)

    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(data[col].dropna(), kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plot_path = os.path.join(output_dir, f"{col}_hist.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"📊 Saved histogram: {plot_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <path_to_csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    data = load_csv(csv_file)
    basic_info(data)
    missing_values(data)
    descriptive_stats(data)
    plot_histograms(data)

if __name__ == "__main__":
    main()
