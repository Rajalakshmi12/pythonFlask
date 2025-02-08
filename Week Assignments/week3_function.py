import openai

openai.api_key = "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"
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

print(completion.choices[0].message.tool_calls)