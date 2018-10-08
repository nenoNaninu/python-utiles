# -*- coding: utf-8 -*-
import sys
import os


# 第1引数に対象のディレクトリ
# 第2引数に対象の拡張子
# 第3引数に変換後の拡張子

if __name__ == "__main__":
    args = sys.argv
    target_dir = args[1]
    target_ex = args[2]
    dst_ex = args[3]
    print("target dir is " + target_dir)
    print("target extention is " + target_ex)
    print("target ex is " + dst_ex)

    # 一覧を取得
    files = os.listdir(target_dir)
    target_files_list = []
    
    # 拡張子がtarget_exをリストに詰め込む
    for f in files:
        if os.path.isfile(f):
            _, ext = os.path.splitext(f)
            if ext == "." + target_ex:
                target_files_list.append(f)

    print("target file is")
    print(target_files_list)
    # 拡張子置き換え。
    for f in target_files_list:
        bname, ext = os.path.splitext(f)
        os.rename(f,bname + "." +dst_ex)
