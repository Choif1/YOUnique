from openai import OpenAI
import base64
from prompt import prompt_generate

client = OpenAI()

def image_generate(client, url, request):

    response = client.responses.create(
        model="gpt-4o",
        instructions=" Draw as human only when explicitly stated to be human. Never draw as human if is not",
        input=f"Generate an image of {prompt_generate(client, url, request)}.",
        tools=[{"type": "image_generation", "model": "gpt-image-2.6-flare"}],
    )

    # Save the image to a file
    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    if image_data:
        image_base64 = image_data[0]
        with open("profile.png", "wb") as f:
            f.write(base64.b64decode(image_base64))
            
image_generate(client=client, url="https://cdn.discordapp.com/attachments/1452278739512725514/1574288207422427260/17951930023271.png?ex=6b0519a5&is=6b03c825&hm=b727fd7f9a887abc27f692f9c4e6d6638bbc19f63438217324ade7b63f75bb54&", request="")