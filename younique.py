from image_generator import image_generate
from image_transition import image_transition
from PIL import Image
from io import BytesIO

def MakeImage(url, request):
   return image_transition(
      Image.open(BytesIO(
        image_generate(url=url, request=request) 
      )).convert("RGB")
    )

MakeImage(url="https://cdn.discordapp.com/attachments/1452278739512725514/1574288207422427260/17951930023271.png?ex=6b0bb125&is=6b0a5fa5&hm=caff3c2cf597e9c99ef201f6bdbf16899de908647c5dcb2849e749129bf47bae&", request="")