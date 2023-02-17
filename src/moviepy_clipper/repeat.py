from moviepy.editor import concatenate_videoclips
from math import ceil


def repeat(duratedClip, duration: int = 0):
    """

    繰り返し再生を続けるclipを返す。
    再生時間(duration)を指定していない場合は、1回だけ流す。

    Parameters
    -----------
    duratedClip
      durationが指定されているclip
    duration
      再生時間。指定していない場合は、1回だけ流す。

    """

    # 指定した動画の再生時間
    source_duration = duratedClip.duration

    # 実際に流すべき時間 ( 指定のdurationが0のときは、動画の長さに合わせる )
    currentDuration = duration if duration else source_duration

    # 十分な数のclipを用意する。 余分な時間は後でカットする。
    num_loop = ceil(currentDuration / source_duration)
    clips = [duratedClip for i in range(num_loop)]

    # clipsを結合する
    combinedClip = concatenate_videoclips(clips)

    # 必要な時間でカットする
    combinedClip = combinedClip.subclip(0, currentDuration)

    return combinedClip
