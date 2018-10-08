# -*- coding: utf-8 -*-
import sys
import os
import cv2
import tqdm

# 画像のデカイ辺を基準に第4引数で与えられたサイズに画像の縮尺比

# python resize_img.py ./src/ ./dst/ jpg 800

if __name__ == "__main__":
    args = sys.argv
    target_dir = args[1]
    dst_dir = args[2]    
    target_ex = args[3]
    dst_size = float(args[4])
    print("target dir is " + target_dir)
    print("target extention is " + target_ex)

    # 一覧を取得
    files = os.listdir(target_dir)
    target_files_list = []
    print(files)
    # 拡張子がtarget_exをリストに詰め込む
    for f in files:
        if os.path.isfile(os.path.join(target_dir, f)):
            _, ext = os.path.splitext(f)
            if ext == "." + target_ex:
                target_files_list.append(f)

    # dst_dirがなければ作成する。
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    
    print("start resize and save")
    # リサイズして保存
    for f in tqdm.tqdm(target_files_list):
        img = cv2.imread(os.path.join(target_dir, f))
        if img.shape[0] > dst_size or img.shape[1] > dst_size:
            big_size = img.shape[0] if img.shape[1] < img.shape[0] else img.shape[1]
            rate = big_size / dst_size
            # 縦
            dst_height = int(img.shape[0]/rate)
            # 横
            dst_width = int(img.shape[1]/rate)

            # 画素、偶数じゃないと嫌だ()
            if not is_even(dst_height):
                dst_height += 1
            
            if not is_even(dst_width):
                dst_width += 1

            dst_img = cv2.resize(img, (dst_width, dst_height))
            cv2.imwrite(os.path.join(dst_dir,f), dst_img)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False