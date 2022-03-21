from os import walk
from os.path import join as pjoin
from sys import argv
from subprocess import run as prun


def mp3_2_wav(folder):
    print(f'[wav2MP3] Target folder {folder}')
    for root, _ , fnames in walk(folder):
        for fname in fnames:
            path = pjoin(root, fname)
            print(f'[wav2MP3] converting {path}')
            n_path = path[:-3] + 'wav'
            proc = ["ffmpeg", "-i", f"{path}", f"{n_path}"]
            prun(proc) 


            
if __name__ == "__main__":
    if not len(argv) > 1 : print('Please provide a valid path')
    else : mp3_2_wav(argv[1])
    
