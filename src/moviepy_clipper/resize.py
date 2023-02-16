from moviepy.editor import (
    ColorClip,
    CompositeVideoClip,
)


# クリップをリサイズする。 contain対応
def resize(clip, size, method="full", backgroundColor=[0, 0, 0]):
    if method == "full":
        clip = clip.resize(size)

    elif method == "contain":
        # sizeに含まれるようにリサイズする
        clip = resizeFit(clip, size, backgroundColor)

    return clip


# クリップを指定したサイズにする。 余白はcolor
def resizeFit(clip, size, color=[0, 0, 0]):
    clip = resizeContain(clip, size)

    # 背景クリップ
    backClip = ColorClip(size, color=color).set_duration(clip.duration)

    # 背景クリップに含める
    clip = clip.set_pos(("center", "center"))
    clip = CompositeVideoClip([backClip, clip])
    return clip


# sizeに含まれるようにリサイズする
def resizeContain(clip, size):
    clipsize = clip.size
    uppedHeight = (size[0] / clipsize[0]) * clipsize[1]
    alignHeight = uppedHeight > size[1]
    if alignHeight:
        clip = clip.resize(height=size[1])
    else:
        clip = clip.resize(width=size[0])
    return clip
