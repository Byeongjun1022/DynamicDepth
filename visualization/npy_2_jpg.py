import os
import argparse
import numpy as np
import PIL.Image as pil
import matplotlib.pyplot as plt
import glob

_DEPTH_COLORMAP = plt.get_cmap('plasma', 256)  # for plotting
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--npy_pth', type=str,
                        help='path to npy')
    parser.add_argument('--output_pth',type=str,
                        help='where output is stored',default='./pred_disp_jpg')

    return parser.parse_args()


def npy_to_jpg(args):
    if not os.path.exists(args.output_pth):
        print('Since output path does not exist, make output folder')
        os.makedirs(args.output_pth)

    npy_list = glob.glob('pred_disp/*.npy')

    # npy_list = np.load(args.npy_pth)
    for i in range(len(npy_list)):
        npy = np.load(npy_list[i])
        depth_color=_DEPTH_COLORMAP(npy)[..., :3]
        img=pil.fromarray((depth_color*255).astype(np.uint8))
        num = npy_list[i].split('/')[1].split('.')[0]
        img.save(os.path.join(args.output_pth, f'disp_{num}.jpg'))


if __name__ == '__main__':
    args=parse_args()
    npy_to_jpg(args)
    # gt_to_jpg(args)
