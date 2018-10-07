# <p align="center"> [Robust-FEC-CNN](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf) Results of Face Datasets </p>

This repository provides facial landmark detection results of several face datasets by the technique of [Robust-FEC-CNN](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf) (Won 2nd of [CVPR 2017 Faces "In-The-Wild" Workshop-Challenge](http://openaccess.thecvf.com/CVPR2017_workshops/CVPR2017_W33.py)). These landmarks can be used for aligning faces of these datasets (use [align.py](align.py)).


## Format
- bbox.txt
```
...
image x_min y_min x_max y_max
...
```

- landmark.txt
```
...
image x_1 y_1 ... x_i y_i ... x_68 y_68
...
```

## Facial Landmarks of Face Datasets
### Attribute
- CelebA [[Google Drive]](https://drive.google.com/open?id=1irMazxNBx2KDZXpaixza4KZTXDTstk3G)
    <p align="center"> <img src="pics\celeba.png"> </p>

### Age
- CACD [[Google Drive]](https://drive.google.com/open?id=1OdP7t0KQZ5sOyILGN71LORSLrBmDfVmi)
    <p align="center"> <img src="pics\cacd.png"> </p>
- MORPH [[Google Drive]](https://drive.google.com/open?id=15bFf1eBdPWvGbZoZ2ValYDY2tOBRfxdV)
    <p align="center"> <img src="pics\morph.png"> </p>

### Identity
- CASIA-WebFace [[Google Drive]](https://drive.google.com/open?id=1e2N7hR84XoV5WjDdC_QhVd7Q8IaXOOv0)
    <p align="center"> <img src="pics\casia-webface.png"> </p>

## Citation
If you find the results of [Robust-FEC-CNN](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf) useful in your research work, please consider citing:

    @InProceedings{He_2017_CVPR_Workshops,
        author = {He, Zhenliang and Zhang, Jie and Kan, Meina and Shan, Shiguang and Chen, Xilin},
        title = {Robust FEC-CNN: A High Accuracy Facial Landmark Detection System},
        booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
        month = {July},
        year = {2017}
    }