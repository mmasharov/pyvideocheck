import os
from pymediainfo import MediaInfo

ffmpegp = 'D:\\ffmpeg\\bin\\ffmpeg.exe'
fnames = os.walk(r'D:\FFOutput')
for f in fnames:
    for x in f[2]:
        print(x, end=',')
        fpath = f'D:\\FFOutput\\{x}'
        media_info = MediaInfo.parse(fpath)
        for track in media_info.tracks:
            if track.track_type == "Video":
                print(track.format, track.internet_media_type, track.width, track.height, track.frame_rate, track.color_space, track.chroma_subsampling)
                if track.chroma_subsampling != '4:2:0':
                    inputv = '-i ' + fpath
                    outv = inputv[3:-4] + '_conv.mp4'
                    os.system(f'{ffmpegp} {inputv} -pix_fmt yuv420p {outv}')

print('All done!')