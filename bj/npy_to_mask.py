import os
import numpy as np
import PIL.Image as pil
import glob

data_pth='/mnt/study/depth/Datasets/Cityscapes_video_jpg/leftImg8bit_sequence/train'
fol_list=os.listdir(data_pth)
f=open('bj/cityscape')
# npy_list=sorted(glob.glob('data/CS/train_mask/*.npy'))

total_num=0
for folder in fol_list:
    img_list=glob.glob(os.path.join(data_pth, folder)+'/*.jpg')
    total_num+=len(img_list)
print(total_num)
# print(len(npy_list))
# for pth_name in npy_list:
#     frame_name=os.path.basename((pth_name))
#     city, seq, frame= frame_name.split('_')
#     frame=frame.split('.')[0]
#     mask_np = np.load('data/CS/train_mask/{}_{}_{}.npy'.format(city, seq, frame))
#     mask=pil.fromarray(mask_np)
#     mask.save(f'data/CS/train_mask_jpg/{city}_{seq}_{frame}.jpg','JPEG')


# mask_np=np.load('data/CS/train_mask/aachen_000000_3.npy')
# mask=pil.fromarray(mask_np)
# mask.show()
# mask.save('mask.jpg','JPEG')