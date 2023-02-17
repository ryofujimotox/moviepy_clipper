from moviepy.editor import AudioFileClip


def _audio(
    bgm_src: str,
):
    # === ファイルの読み込み
    audio = AudioFileClip(bgm_src)

    if not audio:
        print("Source Not Found")
        return None

    return audio


def mergeAudio(clip, source):
    audio = _audio(source)
    if audio:
        clip = clip.set_audio(audio)

    return clip
