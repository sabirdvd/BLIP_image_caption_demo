from PIL import Image
import requests
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from models.blip import blip_decoder
import os
import glob
import sys


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_demo_image(image_size,device, input_image):
    
    raw_image = Image.open(input_image)
    w,h = raw_image.size
    #display(raw_image.resize((w//5,h//5)))
    
    transform = transforms.Compose([
        transforms.Resize((image_size,image_size),interpolation=InterpolationMode.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))
        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
    
    image = transform(raw_image).unsqueeze(0).to(device)   
    return image




image_size = 384

model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_large_caption.pth'
model = blip_decoder(pretrained=model_url, image_size=image_size, vit='large')

#model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_capfilt_large.pth'
#model = blip_decoder(pretrained=model_url, image_size=image_size, vit='base')


# all images 
#filenames = glob.glob("image_karpathy_test_images/*.jpg")
#filenames = glob.glob("COCO_val2014_000000039068.jpg")
filenames = glob.glob("BLIP_image_caption_demo/COCO_val2014_000000000042.jpg")

filenames.sort()
for image in filenames:
  input_image = Image.open(image)
  try:
      image = load_demo_image(image_size=image_size, device=device, input_image=image)
  
      model.eval()
      model = model.to(device)

      with torch.no_grad():
          caption = model.generate(image, sample=False, num_beams=3, max_length=20, min_length=5)
          #print(caption[0])
  except:
      caption = 'gary_images'
    # nucleus sampling
    # caption = model.generate(image, sample=True, top_p=0.9, max_length=20, min_length=5) 
  print('caption: '+caption[0])
  with open('result_b3_fixed.txt', 'a') as fp:
      fp.write(caption[0])
      fp.write('\n')
