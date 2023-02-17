from moviepy.editor import CompositeVideoClip, VideoFileClip
from .resize import resizeFit
from .scrolling_text import ScrollingText
from .audio import mergeAudio

from .repeat import repeat


def neon_mp4(
    source: str,
    duration: int = 0,
    size: list = None,
    scrolling_text: str = None,
    bgm: str = None,
):
    """
    繰り返し再生を続けるclipを返す。
    再生時間(duration)を指定していない場合は、1回だけ流す。

    Parameters
    -----------
    source
        ビデオまでのパス。
    duration
        再生時間。指定していない場合は、1回だけ流す。
    size
        (width, heigth) fitさせる。余白は黒色
    scrolling_text
        右下から左下をスクロールするテキスト
    bgm
        音楽を流す
    """

    # 動画クリップ
    clip = RepeatVideo(source, duration)

    # リサイズ
    if size:
        clip = resizeFit(clip, size, color=[0, 0, 0])

    # 字幕をつける
    if scrolling_text:
        stream_range = clip.size[0]
        txt_clip = ScrollingText(
            text=scrolling_text, duration=clip.duration, stream_range=stream_range
        )
        clip = CompositeVideoClip([clip, txt_clip])

    # BGMをつける
    if bgm:
        clip = mergeAudio(clip, bgm)

    return clip


def RepeatVideo(
    source: str,
    duration: int = 0,
):

    # === ファイルの読み込み
    clip = VideoFileClip(source)
    if not clip:
        print("Source Not Found")
        return None

    clip = repeat(clip, duration)

    # clipと実際の再生時間を返す
    return clip
