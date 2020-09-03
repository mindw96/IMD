# Face Detector and Mask detection

## Install
1. Install MXNet with GPU support.  
2. Install OpenCV. 
3. Type ``make`` to build cxx tools.  
  
## Download Pretrained Models
Pretrained Model: RetinaFace-R50 ([TrainedModel](https://www.dropbox.com/s/53ftnlarhyrpkg2/retinaface-R50.zip?dl=0)).  
and create model folder in IMD/Retinaface. and Move to downloaded file in model folder.  

## Run
- You can run Face and Mask detection algorithm with Detection_MaskwithFace.py  
- When installing the MXNet-GPU library, you need to install a versing that matches your cuda version to avoid any problems. (Support CUDA < 11.0)

## Quick Start

```python
$ python Detection_MaskwithFace.py
```
