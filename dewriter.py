import os
import sys
import Image
from PIL import *

src_path = "/Users/lexvkrotin/Desktop/testfolder"

for file in os.listdir(src_path):
    if ".png" in file:
        img = Image.open(os.path.join(src_path, file))
        print file
        print img.size
        if img.size[0]== 57 and img.size[1] == 57: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon.png"))
        if img.size[0]== 114 and img.size[1] == 114: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon@2x.png"))
        if img.size[0]== 72 and img.size[1] == 72: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon~ipad.png"))
        if img.size[0]== 50 and img.size[1] == 50: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-spot~ipad.png"))
        if img.size[0]== 512 and img.size[1] == 512: os.rename(os.path.join(src_path, file), os.path.join(src_path, "iTunesArtwork.png"))
        if img.size[0]== 320 and img.size[1] == 480: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Default.png"))
        if img.size[0]== 640 and img.size[1] == 960: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Default@2x.png"))
        if img.size[0]== 768 and img.size[1] == 1024: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Default~ipad.png"))
        if img.size[0]== 58 and img.size[1] == 58: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-settings@2x.png"))
        if img.size[0]== 22 and img.size[1] == 29: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-doc.png"))
        if img.size[0]== 44 and img.size[1] == 58: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-doc@2x.png"))
        if img.size[0]== 64 and img.size[1] == 64: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-doc~ipad.png"))
        if img.size[0]== 320 and img.size[1] == 320: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Icon-doc320~ipad.png"))
        if img.size[0]== 768 and img.size[1] == 1004: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Default-PortraitUpsideDown~ipad.png"))
        if img.size[0]== 1024 and img.size[1] == 768: os.rename(os.path.join(src_path, file), os.path.join(src_path, "Default-Landscape~ipad.png"))