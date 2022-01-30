import os
from pymediainfo import MediaInfo

# Функция проверки и конвертации кодировки цвета в видеофайлах (в качестве параметров берет путь к папке с видео и путь к файлу ffmpeg)
def video_check(ffmpeg_path, videodir):
    # Получаем список файлов в каталоге
    fnames = os.walk(videodir)
    for f in fnames:
        for x in f[2]:
            # Выводим имя файла
            print(x, end=',')
            fpath = f'{videodir}\\{x}'
            media_info = MediaInfo.parse(fpath)
            for track in media_info.tracks:
                if track.track_type == "Video":
                    # Выводим информацию о файле
                    print(track.format, track.internet_media_type, track.width, track.height, track.frame_rate, track.color_space, track.chroma_subsampling)
                    # В случае отличия кодировки цвета от yuv420 конвертируем файл
                    if track.chroma_subsampling != '4:2:0':
                        inputv = '-i ' + fpath
                        outv = inputv[3:-4] + '_conv.mp4'
                        # Вызываем ffmpeg с параметрами для переконвертации кодирвоки цвета
                        os.system(f'{ffmpeg_path} {inputv} -pix_fmt yuv420p {outv}')
