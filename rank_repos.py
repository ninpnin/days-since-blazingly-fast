import pandas as pd
import progressbar

df = pd.read_csv("data/aggregated_results.csv")

df["is_rust"] = df["language"] == "Rust"

print(df)
df = df[df["is_rust"]]
df = df.sort_values("created_at")
print(df)

df.to_csv("data/frameworks_sorted.csv", index=False)
