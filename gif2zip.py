import Image
import zipfile
import sys
import os

#src_dest = sys.argv[1]
src_dest = "e:\misc\MediaTools\dog.gif"

img = Image.open(src_dest)

try:
    while 1:
        img.seek(img.tell()+1)
        tr = img.info['transparency']
        palette = []
        levels = 8
        stepsize = 256 // levels
        for i in range(256):
            v = i // stepsize * stepsize
            palette.extend((v, v, v))

        assert len(palette) == 768

        converted = Image.new('P', img.size)
        converted.putpalette(palette)
        converted.paste(img, (0, 0))
        converted.save("test{0}.png".format(img.tell()), "PNG")
except EOFError:
    pass # end of sequence

#import Image
#
#
#
#im = Image.open("e:\misc\MediaTools\dog.gif")
#
#
#
#def iter_frames(im):
#
#    try:
#
#        i= 0
#
#        while 1:
#
#            im.seek(i)
#
#            imframe = im.copy()
#
#            if i == 0:
#
#                palette = imframe.getpalette()
#
#            else:
#
#                imframe.putpalette(palette)
#
#            yield imframe
#
#            i += 1
#
#    except EOFError:
#
#        pass
#
#
#
#for i, frame in enumerate(iter_frames(im)):
#
#    frame.save('test%d.png' % i,**frame.info)