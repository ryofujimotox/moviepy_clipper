from moviepy.editor import ImageClip


def _image(src_path: str, block_duration: int):
    # === ファイルの読み込み
    clip = ImageClip(src_path)
    if not clip:
        print("Source Not Found")
        return None

    video = clip.set_duration(block_duration)

    return video
