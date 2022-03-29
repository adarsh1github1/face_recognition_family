import os
import bz2
from urllib.request import urlopen

def download_landmarks(file):
    url = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'
    decompressor = bz2.BZ2Decompressor()

    with urlopen(url) as src, open(file,'wb') as dst:
        data = src.read(1024)
        while len(data) > 0:
            dst.write(decompressor.decompress(data))
            data = src.read(1024)

dst_dir = 'landmarks'
dst_file = os.path.join(dst_dir,'landmarks.dat')

if not os.path.exists(dst_file):
    os.mkdir(dst_dir)
    download_landmarks(dst_file)



