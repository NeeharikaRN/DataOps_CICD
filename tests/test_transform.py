import pandas as pd
from transform import clean_data

def test_clean_data_large_file():
    # Load original 30-row dataset
    df_raw = pd.read_csv("data/sample.csv")

    # Run the transformation
    df_transformed = clean_data("data/sample.csv")

    # --- Test 1: All names should be uppercase ---
    assert all(df_transformed['name'].str.isupper()), "Not all names are uppercase."

    # --- Test 2: All ages should be > 28 ---
    assert all(df_transformed['age'] > 28), "Some ages are not greater than 28."

    # --- Test 3: Row count should match expected ---
    expected_count = len(df_raw[df_raw['age'] > 28])
    actual_count = len(df_transformed)

    assert actual_count == expected_count, f"Expected {expected_count} rows, but got {actual_count}."

    print(f"Test passed: {actual_count} rows returned with age > 28 and names in uppercase.")
