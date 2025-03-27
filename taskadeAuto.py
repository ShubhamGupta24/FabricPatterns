import requests
import pandas as pd

TASKADE_API_KEY = "your-taskade-api-key"
TASKADE_AI_AGENT_ID = "your-ai-agent-id"

def generate_business_ideas(prompt):
    url = f"https://api.taskade.com/ai/{TASKADE_AI_AGENT_ID}/generate"
    headers = {"Authorization": f"Bearer {TASKADE_API_KEY}", "Content-Type": "application/json"}
    payload = {"input": prompt}

    response = requests.post(url, headers=headers, json=payload)

    # Debugging: Print raw response
    print(f"Raw Response: {response.text}")

    try:
        data = response.json()  # Attempt to parse JSON
        return data.get("ideas", ["No idea generated"]), data.get("tech_stack", "Unknown")
    except requests.exceptions.JSONDecodeError:
        print("❌ Error: Could not decode JSON response")
        return ["Error generating ideas"], "Unknown"

# Load your DataFrame
df = pd.read_csv("patterns.csv")  

# Apply function safely
df["Business Ideas"], df["Tech Stack"] = zip(*df["Prompt"].apply(generate_business_ideas))

# Save to Excel
df.to_excel("business_ideas.xlsx", index=False)

print("✅ Data successfully saved to business_ideas.xlsx")
