from moviepy.editor import TextClip
import os

FONT_SIZE: float = 70  # 文字サイズ
LENGTH_PER_SECOND: float = 180  # 1秒間に進む長さ


def getLibraryDir():
    cFile = __file__
    cDir = os.path.dirname(cFile)
    cDir = os.path.dirname(cDir)
    cDir = os.path.dirname(cDir)
    return cDir + "/"


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

    # 位置決め
    def text_position(second):
        return getScrollingPosition(text, stream_range, second)

    clip = clip.set_pos(text_position)

    return clip


# 指定秒に対する、テキスト位置の取得
def calculatePosition(second: float, stream_range: float):
    lengthMoved = second * LENGTH_PER_SECOND  # 現在の移動距離

    # 0なら左端の見える位置。 stream_rangeなら右端の見えない位置。 移動距離を徐々に引いていく
    position = 0 + stream_range - lengthMoved
    return position


# 指定秒に対する、テキスト座標の取得
# その時間にはそこにいるべきというイメージでscrolled ( リピートは考慮せず進み続ける )
def getScrolledPosition(second: float, stream_range: float):
    positionX = calculatePosition(second, stream_range)

    # 左右は秒ごとに変わる。　上下は底面に固定
    position = [positionX, "bottom"]
    return position


# 1回のスクロールにかかる時間 ( テキストが見えなくなるまで )
def getDurationTextScroll(stream_range: float, text: str):
    textsize = FONT_SIZE * len(text)  # テキスト全体のおおよそのサイズ
    end_position = stream_range + textsize  # テキストが見えなくなる位置
    duration = end_position / LENGTH_PER_SECOND  # スクロール終わるまでの秒数
    return duration


# 経過時間に対する、テキスト座標の取得
def getScrollingPosition(text, stream_range, second):
    # 1回のスクロールにかかる時間
    scroll_duration = getDurationTextScroll(stream_range, text)

    # リピートを考慮して、60秒目でも実質3秒目の位置を取得するイメージ
    currentSecond = second % scroll_duration
    position = getScrolledPosition(currentSecond, stream_range)
    return position
