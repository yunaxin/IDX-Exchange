import pandas as pd

listing = pd.read_csv("CombinedListing_Residential.csv")
sold = pd.read_csv("CombinedSold_Residential.csv")

# Check Structure
listing.head()
listing.info()
listing.describe()

sold.head()
sold.info()
sold.describe()

# Clean column names
listing.columns = listing.columns.str.strip()
sold.columns = sold.columns.str.strip()
