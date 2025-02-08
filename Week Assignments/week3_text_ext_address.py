{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "address_response",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": {
          "addresses": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "zip": { "type": "number", "description": "The zip code, eg. 10001" },
                "longitude": { "type": "number", "description": "The longitude, -87.2564"  },
                "city": { "type": "string", "description": "The city, eg. New York"  }
              },
              "required": ["zip", "longitude", "city"],
              "additionalProperties": false
            }
          }
        },
        "required": ["addresses"],
        "additionalProperties": false
      }
    }
  }
}