import pandas as pd

# ---------------------------
# Load dataset (use sold for analysis)
# ---------------------------
sold = pd.read_csv("CombinedSold_Residential.csv", low_memory=False)

print("=" * 80)
print("DATASET SHAPE")
print("=" * 80)
print(sold.shape)


# ---------------------------
# 1. Unique property types
# ---------------------------
print("\n" + "=" * 80)
print("UNIQUE PROPERTY TYPES")
print("=" * 80)

property_types = sorted(sold["PropertyType"].dropna().astype(str).unique())

for p in property_types:
    print("-", p)


# ---------------------------
# 2. Filtering logic
# ---------------------------
print("\n" + "=" * 80)
print("FILTERING LOGIC")
print("=" * 80)

if property_types == ["Residential"]:
    print("Dataset already contains only Residential properties. No filtering applied.")
else:
    print("Dataset contains multiple property types. Filtering would be required.")


# ---------------------------
# 3. Null-count summary table
# ---------------------------
print("\n" + "=" * 80)
print("NULL SUMMARY")
print("=" * 80)

null_count = sold.isnull().sum()
null_percent = (null_count / len(sold)) * 100

null_summary = pd.DataFrame({
    "Column": sold.columns,
    "NullCount": null_count.values,
    "NullPercent": null_percent.values
}).sort_values("NullPercent", ascending=False)

print(null_summary.to_string(index=False))


# ---------------------------
# 4. Missing value report (>90%)
# ---------------------------
print("\n" + "=" * 80)
print("COLUMNS > 90% NULL")
print("=" * 80)

high_missing = null_summary[null_summary["NullPercent"] > 90]

if high_missing.empty:
    print("No columns above 90% null.")
else:
    print(high_missing.to_string(index=False))


# ---------------------------
# 5. Numeric distribution summary
# ---------------------------
print("\n" + "=" * 80)
print("NUMERIC DISTRIBUTION SUMMARY")
print("=" * 80)

numeric_cols = ["ClosePrice", "LivingArea", "DaysOnMarket"]

for col in numeric_cols:
    s = pd.to_numeric(sold[col], errors="coerce")

    print(f"\n--- {col} ---")
    print("Min:", s.min())
    print("Max:", s.max())
    print("Mean:", s.mean())
    print("Median:", s.median())
    print("10th percentile:", s.quantile(0.10))
    print("25th percentile:", s.quantile(0.25))
    print("50th percentile:", s.quantile(0.50))
    print("75th percentile:", s.quantile(0.75))
    print("90th percentile:", s.quantile(0.90))


# ---------------------------
# 6. Save ONE filtered dataset
# ---------------------------
# Since dataset is already residential, we just save it as validated

sold.to_csv("Filtered_Residential_Sold.csv", index=False)

print("\nFiltered dataset saved as: Filtered_Residential_Sold.csv")