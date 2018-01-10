####### Just incase if I'm too lazy for making a moving image
# image movie_intro = Movie(play="file.ogv", pos=(0, 0), anchor=(0, 0))
# renpy.movie_cutscene("file.ogv")
# Ren'Py is capable of using libav (included) to play movies using the video codecs:
### VP9
### VP8
### Theora
### MPEG 4 part 2 (including Xvid and DivX)
### MPEG 2
### MPEG 1

# and the following audio codecs:
### OPUS
### Vorbis
### MP3
### MP2
### PCM

# inside the following container formats:
# WebM
# Matroska
# Ogg
# Avi
# Various kinds of MPEG stream.

image rgb_flash: 

label intro_mod:
    $ delete_character("sayori")
    $ quick_menu = False
    $ config.allow_skipping = False
    stop music
    play music g2
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    hide screen tear
    stop music
    window auto
    scene black with trueblack
    
    
    return
