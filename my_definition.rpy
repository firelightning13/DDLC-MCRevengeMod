#### Custom persistent and variables ####
default persistent.ggwp_monika = 0
#########################################

######################## Custom images ############################
image splash_gl = "mod_assets/bg/splash_glitch.png"
image splash_n = "bg/splash.png"
image intro_rendered:
    "mod_assets/gl/01.png"
    pause 0.01666
    "mod_assets/gl/02.png"
    pause 0.01666
    "mod_assets/gl/03.png"
    pause 0.01666
    "mod_assets/gl/04.png"
    pause 0.01666
    "mod_assets/gl/05.png"
    pause 0.01666
    "mod_assets/gl/06.png"
    pause 0.01666
    "mod_assets/gl/07.png"
    pause 0.01666
    "mod_assets/gl/08.png"
    pause 0.01666
    "mod_assets/gl/09.png"
    pause 0.01666
    "mod_assets/gl/10.png"
    pause 0.01666
    repeat
image bg s_hang = "mod_assets/cg/s_hang.png"
image bg s_hang_glitch = "mod_assets/cg/s_hang_glitch.png"
######################################################################

####################### Custom audio #################################
define audio.t1g = "mod_assets/sfx/1g.ogg"
define audio.spoopy = "<loop 105.51>mod_assets/sfx/spoopy_glitch.ogg"
######################################################################

###################### Custom Functions ############################
init python:
    def monika_showed_up(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
           config.keymap['dismiss'] = []
           renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
           config.keymap['dismiss'] = dismiss_keys
           renpy.display.behavior.clear_keymap_cache()

    renpy.music.register_channel("trans", mixer="music", tight=True)
####################################################################