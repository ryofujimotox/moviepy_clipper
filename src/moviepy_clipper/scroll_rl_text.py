from .scroll_rl import getDurationScrolled

FONT_SIZE: float = 70  # 文字サイズ


# テキストのコンテンツサイズを取得する
def getTextContentSize(text):
    return FONT_SIZE * len(text)


# 1回のスクロールにかかる時間 ( テキストが見えなくなるまで )
def getDurationTextScroll(stream_range, text):
    content_size = getTextContentSize(text)
    return getDurationScrolled(stream_range, content_size)
