import pandas as pd


def clean_data(csv_path):
    df = pd.read_csv(csv_path)
    df['name'] = df['name'].str.upper()  # Convert names to uppercase
    df = df[df['age'] > 28]  # Filter out ages <= 28
    return df


if __name__ == "__main__":
    df_cleaned = clean_data("data/sample.csv")
    print(df_cleaned)
