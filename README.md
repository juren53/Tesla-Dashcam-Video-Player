### TeslaCam Video Player [ TVP ]

This code reads reads MP4 files from a Teslacam thumb drive. and plays the 
collection of front views of the 60 second clips continuously
[ side and rear views may be addedd at a furture date ]

TVP is written in Python3 using the OpenCV libraries so it should run on any computer 
that can read a thumbdrive and runs Python.

TVP expects to find Teslacam videos on an inserted thumb drive in the directory:

/TeslaCam/TeslaCam/RecentClips/

Run TVP from the command line:

```
python3 tvp.py
```

- Press 'n' to jump to the next 60 second clip
- Press 'p' to jump back to the previous 60 second clip
- Press 'j' to jump forward 10 seconds in the current clip
- Press 'q' to exit the script.
