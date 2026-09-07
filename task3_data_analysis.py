import pandas as pd

# Load processed data
df = pd.read_csv("processed_trending_data.csv")

print("===== TrendPulse Data Analysis =====")

# Basic statistics
print("\nTotal Trending Stories:", len(df))
print("Total Score:", df["score"].sum())
print("Average Score:", round(df["score"].mean(), 2))
print("Average Comments:", round(df["comments"].mean(), 2))

# Highest scoring story
top_story = df.loc[df["score"].idxmax()]

print("\n===== Top Trending Story =====")
print("Title:", top_story["title"])
print("Score:", top_story["score"])
print("Comments:", top_story["comments"])

# Top 10 stories
top_10 = df.nlargest(10, "score")

print("\n===== Top 10 Trending Stories =====")
for index, row in top_10.iterrows():
    print(f"{row['score']} points - {row['title']}")

# Save analysis results
analysis = {
    "total_stories": len(df),
    "total_score": df["score"].sum(),
    "average_score": round(df["score"].mean(), 2),
    "average_comments": round(df["comments"].mean(), 2),
    "top_story": top_story["title"],
    "top_story_score": top_story["score"],
    "top_story_comments": top_story["comments"]
}

analysis_df = pd.DataFrame([analysis])

analysis_df.to_csv("analysis_results.csv", index=False)

print("\nData analysis completed!")
print("Saved as: analysis_results.csv")