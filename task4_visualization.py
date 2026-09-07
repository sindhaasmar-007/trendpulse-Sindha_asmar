import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("processed_trending_data.csv")

# Select top 10 stories
top_10 = df.nlargest(10, "score")

# Create a bar chart
plt.figure(figsize=(12, 6))

plt.barh(
    top_10["title"].str[:50],
    top_10["score"]
)

plt.xlabel("Score")
plt.ylabel("Trending Story")
plt.title("TrendPulse - Top 10 Trending Stories")

plt.gca().invert_yaxis()

plt.tight_layout()

# Save the visualization
plt.savefig("top_10_trending_stories.png", dpi=300)

plt.show()

print("Visualization completed!")
print("Saved as: top_10_trending_stories.png")