from openai import OpenAI
import base64
from prompt import prompt_generate

client = OpenAI()

def image_generate(url, request):
    global client
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=" Draw as human only when explicitly stated to be human. Never draw as human if is not",
        input=f"Generate an image of {prompt_generate(client, url, request)}.",
        tools=[{"type": "image_generation", "model": "gpt-image-2.6-flare"}],
    )

    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    if image_data:
        image_base64 = image_data[0]
        image_bytes = base64.b64decode(image_base64)

        return image_bytes

    # Save the image to a file
    # if image_data:
    #     image_base64 = image_data[0]
    #     with open("profile.png", "wb") as f:
    #         f.write(base64.b64decode(image_base64))