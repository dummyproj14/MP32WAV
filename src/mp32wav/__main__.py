from . import mp3_to_wav as mod
from sys import argv, exit

if __name__ == "__main__":
    print(argv)
    if len(argv)  <= 1 : 
        print('Please provide a valid path')
        exit(-1)
    mod.mp3_2_wav(argv[1])
