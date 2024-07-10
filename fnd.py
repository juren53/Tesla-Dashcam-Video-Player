import glob
import fnmatch

# Specify the directory you want to search in
#directory = '/path/to/your/directory'
directory = '/home/juren/'

# Use glob.glob() with a pattern to match 'front.mp4'
files = glob.glob(f'{directory}/**/*front.mp4', recursive=True)

for file in files:
    print(file)

