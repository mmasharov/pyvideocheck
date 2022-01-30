import os
from pymediainfo import MediaInfo

#ffmpegp = 'D:\\ffmpeg\\bin\\ffmpeg.exe'
#vdir = r'D:\FFOutput'

def video_check(ffmpeg_path, videodir):
    fnames = os.walk(videodir)
    for f in fnames:
        for x in f[2]:
            print(x, end=',')
            fpath = f'{videodir}\\{x}'
            media_info = MediaInfo.parse(fpath)
            for track in media_info.tracks:
                if track.track_type == "Video":
                    print(track.format, track.internet_media_type, track.width, track.height, track.frame_rate, track.color_space, track.chroma_subsampling)
                    if track.chroma_subsampling != '4:2:0':
                        inputv = '-i ' + fpath
                        outv = inputv[3:-4] + '_conv.mp4'
                        os.system(f'{ffmpeg_path} {inputv} -pix_fmt yuv420p {outv}')

#video_check(ffmpegp, vdir)
#print('All done!')