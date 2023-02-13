## Install

Only pip installations using git are supported.

```
pip install git+https://github.com/ryofujimotox/moviepy_clipper
```

## Example

``` python
from moviepy.editor import CompositeVideoClip, concatenate_videoclips
from moviepy_clipper import (
    RepeatVideo,
    ScrollingText,
    getDurationTextScroll,
)

def main():
    # repeat_video
    source_path = "/〇〇/movie.mp4"
    duration = 10 # cut 10 second
    clip, clip_duration = RepeatVideo(source_path, duration)

    # scrolling_text
    text = "hello world"
    duration = 10 # cut 10 second
    stream_range = 1010 # screen size
    txt_clip = ScrollingText(text, duration, stream_range)


    # let's composite ( 重ねる )
    composite_clip = concatenate_videoclips([clip, txt_clip])

    # let's write ( 出力 )
    dest = "/〇〇/new_movie.mp4"
    composite_clip.write_videofile(dest)
```

