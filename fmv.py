import os
import shutil
import id3reader

src_folder = "e:\\misc\\Radiohead\\"

albums = list()

for file in os.listdir(src_folder):
    if ".mp3" in file:
        id3r = id3reader.Reader(src_folder+file)
        album_name = id3r.getValue('album')
        #somehow id3r.getValue('year') didn't work for me
        #year = id3r.getValue('TDRC')
        year = id3r.getValue('year')
        new_album = True
        for title in albums:
            if album_name == title:
                new_album = False
        if new_album:
            os.mkdir(src_folder+'('+year+')'+' '+album_name)
            albums.append(album_name)
        shutil.move(src_folder+file, os.path.join(os.path.join(src_folder, '('+year+')'+' '+ album_name), file))
    
    