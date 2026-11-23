
from openai import OpenAI

client = OpenAI()

url = ""
analyzations = {"appearance": "", "adjective": "", "matching_object": ""}
request = ""

# 사진 분석
analyzations["appearance"] = client.responses.create(
    model="gpt-4o",
    instructions="Output only the relevant answer.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": url
                },
                {
                    "type": "input_text",
                    "text": "Are there any distinctive features that make this person stand out from an average person? If so, describe which features are distinctive and what they look like."
                }
            ]
        }
    ]
).output_text

analyzations["adjective"] = client.responses.create(
    model="gpt-4o",
    instructions="Give a concise answer.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": url
                },
                {
                    "type": "input_text",
                    "text": "Provide only one adjective that best suits this person."
                }
            ]
        }
    ]
).output_text

analyzations["matching_object"] = client.responses.create(
    model="gpt-4o",
    instructions="Respond with a single word only. It can be anything, including a human, animal, or object.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": url
                },
                {
                    "type": "input_text",
                    "text": "Choose one thing that best suits this person."
                }
            ]
        }
    ]
).output_text

# 프롬프트 작성
prompt_default = "A character with a (appearance) face shape, (appearance) eyes, (appearance) nose, and \n" \
" (appearance) lips, also wearing (appearance) and dressed in (appearance), \n" \
" a (adjective) (matching_object) character."

prompt = client.responses.create(
    model="gpt-4o",
    instructions="Output only the generated prompt.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": f"Prompt: {prompt_default}\n\nappearance: {analyzations['appearance']}\nadjective: {analyzations['adjective']}\nmatching_object: {analyzations['matching_object']}\n\nNaturally fill in the blanks in the prompt using the appearance details as a reference. For adjective and matching_object, use only the provided words. If any part is difficult to complete based on the given information, use your creativity to fill it in."
                }
            ]
        }
    ]
).output_text

prompt_request = client.responses.create(
    model="gpt-4o",
    instructions="Output only the generated prompt.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": f"Prompt: {prompt}\n\nUser request: {request}\n\nBased on the user's request, replace the corresponding elements previously filled into the prompt. Any additional requests that do not replace existing elements should be added to the third line of the prompt."
                }
            ]
        }
    ]
).output_text

print(prompt_request)