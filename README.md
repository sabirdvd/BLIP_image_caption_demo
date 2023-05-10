# BLIP image caption extended demo 

Please refer to this [medium blog post](https://medium.com/@iee_53136/paper-summary-blip-bootstrapping-language-image-pre-training-for-unified-vision-language-c1df6f6c9166) for more detail.

The original paper and colab

[![arXiv](https://img.shields.io/badge/arXiv-2201.12086-b31b1b.svg)](https://arxiv.org/abs/2201.12086) [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/salesforce/BLIP/blob/main/demo.ipynb)





<!-- [demo]<!(https://colab.research.google.com/github/salesforce/BLIP/blob/main/demo.ipynb) -->


For image captioning only with the **Larger model** with the two proposed caption generation methods (beam search and nucleus sampling), that runs on your local machine with multiple images:

<!--

[Colab](https://colab.research.google.com/drive/1RNE_nxNrcDcSHSEiBLmMBmC40w9w_yE4?usp=sharing) 
 -->
 



 [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RNE_nxNrcDcSHSEiBLmMBmC40w9w_yE4?usp=sharing)
 
 




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

For BLIP 2 
``` 
pip install salesforce-lavis
```

```
BILP-2_caption_Inference_2.7B.py

```
Note that BLIP-2  (can't run on Colab) only runs on ``A100 GPU``, pls find the output ``BLIP_2_2.7b.json`` 

For COCO Caption Karpathy test (image caption dataset COCO benchmark) (my run using the L_check_point) 

Download COCO-caption metrics from [here](https://github.com/salaniz/pycocoevalcap)

```
python coco_eval_run.py
```


| model   | B1|    B2 |    B3 |    B4 |     M |     C |     S |
| ------------- | ------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------ |
| BLIP_ViT-L Nucleus Sampling  | 0.660 | 0.456 | 0.308 |0.205 | 0.239 |  0.869 |  0.190 |
| BLIP_ViT-L  paper result (BS)  | 0.797  | 0.649 | 0.514 | 0.403 | 0.311 | 1.365 | 0.243 |
| BLIP2_ViG-OPT2.7B  paper result (BS)  |  0.831  | 0.691 | 0.555 |0.438 | 0.317 | 1.460 | 0.252 |

<!-- | BLIP-2    paper result (BS)  | 0.797  | 0.649 | 0.514 | 0.404 | 0.311 | 1.367 | 0.243 | --> 




Please refer to the original work for main information

```
https://github.com/salesforce/BLIP
```
