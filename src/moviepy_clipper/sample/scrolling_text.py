from moviepy.editor import TextClip
import os

from ..scroll_rl import repeatScroll
from ..scroll_rl_text import FONT_SIZE, getTextContentSize


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
