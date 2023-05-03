import torch
from PIL import Image
import requests
import os
import glob
from lavis.models import load_model_and_preprocess

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# cheking GPU memory
info = torch.cuda.mem_get_info()
print(info)

filenames = glob.glob("/image_karpathy_test_images/*.jpg")

filenames.sort()
for image in filenames:
  input_image = Image.open(image)
  
  model, vis_processors, _ = load_model_and_preprocess(name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=device)
      
      
  image = vis_processors["eval"](input_image).unsqueeze(0).to(device)
     
      
  caption = model.generate({"image": image})
 


  print('caption: '+str(caption))

  
  with open('/result_BLIP_2.7b.txt', 'a') as fp:
      fp.write(str(caption))
      fp.write('\n')

