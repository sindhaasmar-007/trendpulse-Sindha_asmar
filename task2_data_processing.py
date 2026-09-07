import pandas as pd

# Load the collected data
df = pd.read_csv("trending_data.csv")

print("Original data:")
print(df.head())

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows where title is missing
df = df.dropna(subset=["title"])

# Fill missing values
df["score"] = df["score"].fillna(0)
df["comments"] = df["comments"].fillna(0)
df["author"] = df["author"].fillna("Unknown")

# Convert score and comments to numbers
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)
df["comments"] = pd.to_numeric(df["comments"], errors="coerce").fillna(0)

# Clean the title
df["title"] = df["title"].str.strip()

# Sort by score
df = df.sort_values(by="score", ascending=False)

# Save processed data
df.to_csv("processed_trending_data.csv", index=False)

print("\nData processing completed!")
print(f"Total clean records: {len(df)}")
print("Saved as: processed_trending_data.csv")