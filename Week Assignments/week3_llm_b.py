import openai
import os

openai.api_key = "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"

try:
    openai.Model.list()
    print("API Key is valid ✅")
except openai.error.AuthenticationError:
    print("❌ Invalid API Key!")
    
models = openai.Model.list()
print([m.id for m in models["data"]])
    
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "List only the valid English words from these: IgwsJe6A, EnDFTY"}
    ]
)

# Print actual token usage
print("Tokens Used:", response['usage']['total_tokens'])


