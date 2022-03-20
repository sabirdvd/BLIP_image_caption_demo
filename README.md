# BLIP image caption demo
BLIP image caption demo [paper](https://arxiv.org/abs/2201.12086) and [demo](https://colab.research.google.com/github/salesforce/BLIP/blob/main/demo.ipynb)

For image captioning only with the **Larger model** with the two proposed caption generation methods (beam search and nucleus sampling), that runs on your local machine with multiple images 
```
conda create -n BLIP_demo python=3.7 anaconda
conda activate BLIP_demo
```

```
git clone https://github.com/salesforce/BLIP
pip install -r requirements.txt

git clone https://github.com/sabirdvd/BLIP_image_caption_demo.git
cp caption_Inference_L.py ../
python caption_Inference_L.py
```
or just refer to the notebook 
```
BLIP_demo_muti_images.ipynb
```

Result on COCO Caption Karpathy test (my run) 


| model   | B1|    B2 |    B3 |    B4 |     M |     C |     S |
| ------------- | ------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------ |
| BLIP_ViT-L   | 0.797  | 0.649 | 0.514 | 0.403 | 0.311 | 1.365 | 0.243 |




please refer to the original work for main information

```
https://github.com/salesforce/BLIP
```
