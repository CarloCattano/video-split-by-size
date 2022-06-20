### Split a video by a given size
Uses [ffmpeg](https://ffmpeg.org/download.html) to split a video by a given size 

```python 
splitter = Split(100,"./")
splitter.splitVid("vid.mp4")
```
Will split the desired video by chunks of approx. 100MB and save them to the ./ directory or any other specified.

ffmpeg **must be** installed in your system path
