import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IPScnd1SwFKrqWQYy9FoSL5epaqKsbXQvq6R2ocvxBYA")

# Read data from analyzer output file
with open("ai_input.txt", "r") as f:
    data = f.read()

prompt = f"""
You are an SRE expert.

Generate a weekly production report based on:

{data}

Make it simple, clear, and executive friendly.
"""

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(prompt)

print(response.text)