import requests
import pandas as pd
from datetime import datetime

# Hacker News API
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Get trending story IDs
response = requests.get(url)
story_ids = response.json()

data = []

# Collect top 30 trending stories
for story_id in story_ids[:30]:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    story_response = requests.get(story_url)

    if story_response.status_code == 200:
        story = story_response.json()

        if story:
            data.append({
                "id": story.get("id"),
                "title": story.get("title"),
                "score": story.get("score", 0),
                "author": story.get("by"),
                "comments": story.get("descendants", 0),
                "url": story.get("url"),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save collected data
df.to_csv("trending_data.csv", index=False)

print("TrendPulse - Data Collection Completed!")
print(f"Total stories collected: {len(df)}")
print("Data saved to: trending_data.csv")