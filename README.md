## Install

Only pip installations using git are supported.

```
pip install git+https://github.com/ryofujimotox/moviepy_clipper
```

## Example


### All Products Pack

- repeat mp4
- resize fit
- scrolling text
- override sound

https://github.com/ryofujimotox/moviepy_clipper/blob/main/src/moviepy_clipper/sample/neon_mp4.py

``` python
from moviepy_clipper import neon_mp4

def main():
    source_path = "/〇〇/movie.mp4"
    duration = 10 # cut 10 second
    size = (500,500) # (width: int, height: int)
    scrolling_text = "hello world" # scrolling text
    sound_path = "./upload/music.mp3" # override sound
    clip = neon_mp4(
        source_path,
        duration,
        size,
        scrolling_text,
        sound_path
    )

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```





### Scrolling

#### scrolling clip

Scroll clip right to left 
https://github.com/ryofujimotox/moviepy_clipper/blob/main/src/moviepy_clipper/scroll_rl.py

``` python
from moviepy_clipper import repeatScroll

def main():
    # clip
    clip = VideoFileClip("/〇〇/sample.mp4")
    
    # scroll
    stream_range = 100 # range scroll stream
    content_size = 100 # content size
    clip = repeatScroll(clip, stream_range, content_size)

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```




#### scrolling text

Scroll text clip right to left
https://github.com/ryofujimotox/moviepy_clipper/blob/main/src/moviepy_clipper/sample/scrolling_text.py

``` python
from moviepy_clipper import ScrollingText

def main():
    # scrolling text
    scrolling_text = "hello world"
    duration = 10 # cut 10 second
    stream_range = 100 # range scroll stream
    clip = ScrollingText(
        text=scrolling_text, duration=duration, stream_range=stream_range
    )

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```








### Resize

https://github.com/ryofujimotox/moviepy_clipper/blob/main/src/moviepy_clipper/resize.py

``` python
from moviepy_clipper import resize

def main():
    # clip
    clip = VideoFileClip("/〇〇/sample.mp4")
    
    # resize
    size = (500, 500) # (width, height)
    method = "contain" # full is normal resize
    backgroundColor = [0, 0, 0] # RGB
    clip = resize(clip, size, method=method, backgroundColor=backgroundColor):

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```



#### resize fit

``` python
from moviepy_clipper import resizeFit

def main():
    # clip
    clip = VideoFileClip("/〇〇/sample.mp4")
    
    # resize
    size = (500, 500) # (width, height)
    backgroundColor = [0, 0, 0] # RGB
    clip = resizeFit(clip, size, backgroundColor=backgroundColor):

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```







### Repeat

`concatenate_videoclips` and `cut`

https://github.com/ryofujimotox/moviepy_clipper/blob/main/src/moviepy_clipper/repeat.py

``` python
from moviepy_clipper import repeat

def main():
    # clip
    clip = VideoFileClip("/〇〇/sample.mp4")
    
    # resize
    duration = 10 # cut 10 second
    clip = repeat(clip, duration)

    # output
    clip.write_videofile("/〇〇/new_movie.mp4")
```















