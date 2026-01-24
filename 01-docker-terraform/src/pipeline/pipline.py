import sys
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print("arguments", sys.argv)
print(df.head())
month = int(sys.argv[1])
print(f"Running pipeline for month {month}")

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")



