import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from io import BytesIO

pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True
).to("cuda")

pipe.load_lora_weights("./my_lora")

def image_transition(image):
    result = pipe(
        prompt="Convert the image to my style.",
        image=image,
        strength=0.6,
        guidance_scale=7.5
    ).images[0]

    # result.save("output.png")
    image_buffer = BytesIO()
    result.save(image_buffer, format="PNG")
    image_buffer.seek(0)

    return image_buffer