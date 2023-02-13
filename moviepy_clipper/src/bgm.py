from moviepy.editor import AudioFileClip


def _bgm(
    bgm_src: str,
):
    # === ファイルの読み込み
    audio = AudioFileClip(bgm_src)

    if not audio:
        print("Source Not Found")
        return None

    return audio
