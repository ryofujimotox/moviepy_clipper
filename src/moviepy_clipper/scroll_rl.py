LENGTH_PER_SECOND: float = 180  # 1秒間に進む長さ


# スクロールさせる
def repeatScroll(clip, stream_range, content_size):
    """
    clipを右から左に流し続ける

    Parameters
    -----------
    clip
        クリップ
    stream_range
        表示する範囲
    content_size
        流すコンテンツのサイズ
    """

    # 位置決め
    def position(second):
        return getScrollingPosition(content_size, stream_range, second)

    clip = clip.set_pos(position)
    return clip


# 指定秒に対する、クリップ位置の取得
def calculatePosition(second: float, stream_range: float):
    lengthMoved = second * LENGTH_PER_SECOND  # 現在の移動距離

    # 0なら左端の見える位置。 stream_rangeなら右端の見えない位置。 移動距離を徐々に引いていく
    position = 0 + stream_range - lengthMoved
    return position


# 指定秒に対する、クリップ座標の取得
# その時間にはそこにいるべきというイメージでscrolled ( リピートは考慮せず進み続ける )
def getScrolledPosition(second: float, stream_range: float):
    positionX = calculatePosition(second, stream_range)

    # 左右は秒ごとに変わる。　上下は底面に固定
    position = [positionX, "bottom"]
    return position


# 1回のスクロールにかかる時間 ( クリップが見えなくなるまで )
def getDurationScrolled(stream_range: float, content_size: str):
    end_position = stream_range + content_size  # クリップが見えなくなる位置
    duration = end_position / LENGTH_PER_SECOND  # スクロール終わるまでの秒数
    return duration


# 経過時間に対する、クリップ座標の取得
def getScrollingPosition(content_size, stream_range, second):
    # 1回のスクロールにかかる時間
    scroll_duration = getDurationScrolled(stream_range, content_size)

    # リピートを考慮して、60秒目でも実質3秒目の位置を取得するイメージ
    currentSecond = second % scroll_duration
    position = getScrolledPosition(currentSecond, stream_range)
    return position
