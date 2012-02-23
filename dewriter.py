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
               
                sizeStr = str(img.size[0]) + 'x' + str(img.size[1])
               
                filenames = {
                        '57x57': 'Icon.png',
                        '114x114': 'Icon@2x.png',
                        '72x72': 'Icon~ipad.png',
                        '50x50': 'Icon-spot~ipad.png',
                        '512x512': 'iTunesArtwork.png',
                        '320x480': 'Default.png',
                        '640x960': 'Default@2x.png',
                        '768x1024': 'Default~ipad.png',
                        '58x58': 'Icon-settings@2x.png',
                        '22x29': 'Icon-doc.png',
                        '44x58': 'Icon-doc@2x.png',
                        '64x64': 'Icon-doc~ipad.png',
                        '320x320': 'Icon-doc320~ipad.png',
                        '768x1004': 'Default-PortraitUpsideDown~ipad.png',
                        '1024x768': 'Default-Landscape~ipad.png'
                }
               
                if sizeStr in filenames : os.rename(os.path.join(src_path, file), os.path.join(src_path, filenames[sizeStr]))