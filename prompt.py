analyzations = {"appearance": "", "adjective": "", "matching_object": ""}
prompt_default = "A character with a (appearance) eyes, and specially (appearance)\n" \
" also wearing (appearance) and dressed in (appearance), \n" \
" a (adjective) (matching_object) character whose race is (matching_race), designed as a profile picture. With white background."

def prompt_generate(client, url, request):
    global analyzations, prompt_default

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
                        "text": "Identify approximately 2 distinctive physical features that make this person stand out from the average person. Focus only on genuinely unusual or highly noticeable features that clearly distinguish them from others. For each feature, describe its specific appearance in detail. Do not include ordinary or common features."
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
        instructions="Respond with a single word only.",
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

    analyzations["matching_race"] = client.responses.create(
        model="gpt-4o",
        # instructions="Respond with a single word only.",
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
                        "text": "Choose one race or species that best represents this person. The choice can be anything, including humans, animals, mythical creatures, or even inanimate objects. Both humanoid and non-humanoid forms are allowed. Select the single most fitting option based on the person's distinctive visual features. If it is difficult to choose, decide arbitrarily with your creativity. Always provide one definitive choice."
                    }
                ]
            }
        ]
    ).output_text
    print(analyzations["matching_race"])

    # 프롬프트 작성
    prompt = client.responses.create(
        model="gpt-4o",
        instructions="Output only the generated prompt.",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"{prompt_default}\n\nappearance: {analyzations['appearance']}\nadjective: {analyzations['adjective']}\nmatching_object: {analyzations['matching_object']}\nmatching_race: {analyzations['matching_race']}\n\nFill in the blanks in the prompt using the appearance details as a reference. For adjective and matching_object, use only the provided words. If any part is difficult to complete based on the given information, use your CREATIVITY to fill it in."
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
                        "text": f"{prompt}\n\nUser request: {request}\n\nBased on the user's request, replace the corresponding elements previously filled into the prompt. Any additional requests that do not replace existing elements should be added to the prompt."
                    }
                ]
            }
        ]
    ).output_text

    print(prompt_request)
    return prompt_request