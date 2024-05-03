import asyncio
import os
from functools import wraps, partial

from pytube import YouTube


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


@async_wrap
def download_video_from_youtube(youtube_url, path='/'):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.get_audio_only()
    output_file = audio_stream.download(output_path=path)
    return os.path.normpath(output_file)

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=HK5BRAApMp8"
    outp = r"D:\projects\AIPO_V2\insighter_worker\temp"
    asyncio.run(download_video_from_youtube(youtube_url='https://www.youtube.com/watch?v=HK5BRAApMp8',path=outp))