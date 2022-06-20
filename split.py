import subprocess,os

class Split:
    def __init__(self,maxSize,path):
        '''Size of the chunks in MB and path to save the pieces'''
        self.maxSize = int((maxSize-10) * 1024)
        self.path = path
    def splitVid(self,file):
        '''File to split'''
        video_size = os.path.getsize(file)
        video_size = video_size / 1024
        video_duration = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file], stdout=subprocess.PIPE).stdout.decode('utf-8')
        pieces_duration = round(float(video_duration) / (int(video_size / self.maxSize) + 1))
        subprocess.run(["ffmpeg", "-i", file, "-c", "copy", "-f", "segment", "-segment_time", str(pieces_duration), "-loglevel", "quiet", "-reset_timestamps", "1", f"{self.path}part%02d_vid.mp4"])