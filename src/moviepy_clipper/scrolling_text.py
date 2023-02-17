from moviepy.editor import TextClip
import os

from .scrolling import repeatScroll, getDurationScrolled

FONT_SIZE: float = 70  # 文字サイズ


# スクロールするテキストClipを返す
def ScrollingText(text: str, duration: float, stream_range: float):

    # テキストclip生成
    clip = TextClip(
        text,
        font=getLibraryDir() + "/font/LINESeedJP_A_TTF_Bd.ttf",
        fontsize=FONT_SIZE,
        color="white",
        stroke_color="#4C444D",
        stroke_width=2,
    ).set_duration(duration)

    # コンテンツサイズ取得
    content_size = getTextContentSize(text)

    # スクロールアニメーション
    clip = repeatScroll(clip, stream_range, content_size)

    return clip


# ライブラリのパス取得
def getLibraryDir():
    return os.path.dirname(os.path.abspath(__file__))


# テキストのコンテンツサイズを取得する
def getTextContentSize(text):
    return FONT_SIZE * len(text)


# 1回のスクロールにかかる時間 ( テキストが見えなくなるまで )
def getDurationTextScroll(stream_range, text):
    content_size = getTextContentSize(text)
    return getDurationScrolled(stream_range, content_size)
