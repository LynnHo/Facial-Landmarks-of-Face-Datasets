from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from functools import partial
from multiprocessing import Pool
import os

import cropper
import numpy as np


# ==============================================================================
# =                                      param                                 =
# ==============================================================================
parser = argparse.ArgumentParser()
# main
parser.add_argument('--img_dir', dest='img_dir', required=True)
parser.add_argument('--save_dir', dest='save_dir', required=True)
parser.add_argument('--landmark_file', dest='landmark_file', default='landmark.txt')
parser.add_argument('--standard_landmark_file', dest='standard_landmark_file', default='standard_landmark_68pts.txt')
parser.add_argument('--crop_size_h', dest='crop_size_h', type=int, default=256)
parser.add_argument('--crop_size_w', dest='crop_size_w', type=int, default=256)
parser.add_argument('--move_h', dest='move_h', type=float, default=0.175)
parser.add_argument('--move_w', dest='move_w', type=float, default=0.)
parser.add_argument('--save_format', dest='save_format', choices=['jpg', 'png'], default='jpg')
parser.add_argument('--n_worker', dest='n_worker', type=int, default=8)
# others
parser.add_argument('--face_factor', dest='face_factor', type=float, help='The factor of face area relative to the output image.', default=0.6)
parser.add_argument('--align_type', dest='align_type', choices=['affine', 'similarity'], default='similarity')
parser.add_argument('--order', dest='order', type=int, choices=[0, 1, 2, 3, 4, 5], help='The order of interpolation.', default=3)
parser.add_argument('--mode', dest='mode', choices=['constant', 'edge', 'symmetric', 'reflect', 'wrap'], default='edge')
args = parser.parse_args()


# ==============================================================================
# =                                opencv first                                =
# ==============================================================================
_DEAFAULT_JPG_QUALITY = 95
try:
    import cv2
    imread = cv2.imread
    imwrite = partial(cv2.imwrite, params=[int(cv2.IMWRITE_JPEG_QUALITY), _DEAFAULT_JPG_QUALITY])
    align_crop = cropper.align_crop_opencv
    print('Use OpenCV')
except:
    import skimage.io as io
    imread = io.imread
    imwrite = partial(io.imsave, quality=_DEAFAULT_JPG_QUALITY)
    align_crop = cropper.align_crop_skimage
    print('Importing OpenCv fails. Use scikit-image')


# ==============================================================================
# =                                     run                                    =
# ==============================================================================
save_dir = os.path.join(args.save_dir, 'align_size(%d,%d)_move(%.3f,%.3f)_%s' % (args.crop_size_h, args.crop_size_w, args.move_h, args.move_w, args.save_format), 'data')
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

# count landmarks
with open(args.landmark_file) as f:
    line = f.readline()
n_landmark = line.count(' ') // 2

# read data
img_names = np.genfromtxt(args.landmark_file, dtype=np.str, usecols=0)
landmarks = np.genfromtxt(args.landmark_file, dtype=np.float, usecols=range(1, n_landmark * 2 + 1)).reshape(-1, n_landmark, 2)
standard_landmark = np.genfromtxt(args.standard_landmark_file, dtype=np.float).reshape(n_landmark, 2)
standard_landmark[:, 0] += args.move_w
standard_landmark[:, 1] += args.move_h


def work(i):  # a single work
    try:
        img = imread(os.path.join(args.img_dir, img_names[i]))
        img_crop = align_crop(img,
                              landmarks[i],
                              standard_landmark,
                              crop_size=(args.crop_size_h, args.crop_size_w),
                              face_factor=args.face_factor,
                              align_type=args.align_type,
                              order=args.order,
                              mode=args.mode)
        name = os.path.splitext(os.path.basename(img_names[i]))[0] + '.' + args.save_format
        imwrite(os.path.join(save_dir, name), img_crop)
    except:
        print('%s fails!' % img_names[i])

pool = Pool(args.n_worker)
pool.map(work, range(len(img_names)))
pool.close()
pool.join()
