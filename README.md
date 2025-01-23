<h1 align="center"> 
    <a href="http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf">Robust-FEC-CNN</a> Results of Face Datasets 
</h1>

<a href="http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf"><img src="https://img.shields.io/badge/CVPRW 2017-3A98B9?label=%F0%9F%93%9D&labelColor=FFFDD0" style="height: 28px" /></a>
<a href="https://kdocs.cn/l/cdazHvg3gdca"><img src="https://img.shields.io/badge/FG 2017-3A98B9?label=%F0%9F%93%9D&labelColor=FFFDD0" style="height: 28px" /></a>

> **[Robust FEC-CNN: A High Accuracy Facial Landmark Detection System](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf)** \
> [Zhenliang He](https://lynnho.github.io)<sup>1,2</sup>, [Jie Zhang](https://scholar.google.com/citations?user=hJAhF0sAAAAJ&hl=en)<sup>1,2</sup>, [Meina Kan](https://scholar.google.com/citations?user=4AKCKKEAAAAJ)<sup>1,3</sup>, [Shiguang Shan](https://scholar.google.com/citations?user=Vkzd7MIAAAAJ)<sup>1,3</sup>, [Xilin Chen](https://scholar.google.com/citations?user=vVx2v20AAAAJ&hl=zh-CN)<sup>1</sup>
>
> **[A Fully End-to-End Cascaded CNN for Facial Landmark Detection](https://kdocs.cn/l/cdazHvg3gdca)** \
> [Zhenliang He](https://lynnho.github.io)<sup>1,2</sup>, [Meina Kan](https://scholar.google.com/citations?user=4AKCKKEAAAAJ)<sup>1,3</sup>, [Jie Zhang](https://scholar.google.com/citations?user=hJAhF0sAAAAJ&hl=en)<sup>1,2</sup>, [Xilin Chen](https://scholar.google.com/citations?user=vVx2v20AAAAJ&hl=zh-CN)<sup>1</sup>, [Shiguang Shan](https://scholar.google.com/citations?user=Vkzd7MIAAAAJ)<sup>1,3</sup>
> 
> <sup>1</sup>Key Lab of Intelligent Information Processing, Institute of Computing Technology, CAS, China \
> <sup>2</sup>University of Chinese Academy of Sciences, China \
> <sup>3</sup>CAS Center for Excellence in Brain Science and Intelligence Technology, China

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

## Landmarks File of Face Datasets
### Attribute
- CelebA [[Google Drive]](https://drive.google.com/open?id=1irMazxNBx2KDZXpaixza4KZTXDTstk3G) [[Baidu Netdisk]](https://pan.baidu.com/s/1mo6v0o9dUkOMXElFZ-UGgQ)
    <p align="center"> <img src="pics\celeba.png"> </p>

### Age
- CACD [[Google Drive]](https://drive.google.com/open?id=1OdP7t0KQZ5sOyILGN71LORSLrBmDfVmi) [[Baidu Netdisk]](https://pan.baidu.com/s/1Tin8dsD9-Sh7JoBA4zWwVQ)
    <p align="center"> <img src="pics\cacd.png"> </p>
- IMDB-WIKI [[Google Drive]](https://drive.google.com/open?id=1lHYRHKK9AwuPJbyyjK1ZbbS9n01BqwI5) [[Baidu Netdisk]](https://pan.baidu.com/s/17dY91S3X47oh9GGbwODNdw)
    <p align="center"> <img src="pics\imdb-wiki.png"> </p>
- FG-NET [[Google Drive]](https://drive.google.com/open?id=1qR_9hAp9m6dQDupbsTozbZdE1VslK7XP) [[Baidu Netdisk]](https://pan.baidu.com/s/1AA3cNaoi50EaKRNOBMzRZg)
    <p align="center"> <img src="pics\fg-net.png"> </p>
- MORPH [[Google Drive]](https://drive.google.com/open?id=15bFf1eBdPWvGbZoZ2ValYDY2tOBRfxdV) [[Baidu Netdisk]](https://pan.baidu.com/s/1ENoI5X7aq3Tzo7-HRF1L7g)
    <p align="center"> <img src="pics\morph.png"> </p>

### Identity
- CASIA-WebFace [[Google Drive]](https://drive.google.com/open?id=1e2N7hR84XoV5WjDdC_QhVd7Q8IaXOOv0) [[Baidu Netdisk]](https://pan.baidu.com/s/1Hic8PjmmWWcLqf4SZYcXmg)
    <p align="center"> <img src="pics\casia-webface.png"> </p>
- LFW [[Google Drive]](https://drive.google.com/open?id=15P_KoC4PjwkWjcRQI8uKIgwHxdQKT0xa) [[Baidu Netdisk]](https://pan.baidu.com/s/12Hr9lOyJq8K0WCf8c-kzeQ)
    <p align="center"> <img src="pics\lfw.png"> </p>

## Citation
If you find the results of [Robust-FEC-CNN](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w33/papers/He_Robust_FEC-CNN_A_CVPR_2017_paper.pdf) useful in your research work, please consider citing:

    @InProceedings{he2017robust,
        author = {He, Zhenliang and Zhang, Jie and Kan, Meina and Shan, Shiguang and Chen, Xilin},
        title = {Robust FEC-CNN: A High Accuracy Facial Landmark Detection System},
        booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
        year = {2017}
    }
    
    @InProceedings{he2017fully,
        author={He, Zhenliang and Kan, Meina and Zhang, Jie and Chen, Xilin and Shan, Shiguang},
        title={A Fully End-to-end Cascaded CNN for Facial Landmark Detection},
        booktitle={The IEEE International Conference on Automatic Face \& Gesture Recognition (FG)},
        year={2017}
    }
