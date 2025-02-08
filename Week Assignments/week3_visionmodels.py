{
    "model": "gpt-4o-mini",
    "messages": [{
        "role":"user",
        "content": [
            {
               "type": "text",
               "text": "Extract text from this image"
            },
            {
                "type": "image_url",
                "image_url": {"url": "data:image/png;base64,{image_b64}"}
            }            
        ]
    }
    ]
}