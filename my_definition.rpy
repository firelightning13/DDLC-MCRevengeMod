define config.developer = False #Change this flag to True to enable dev tools

#### Custom persistent and variables ####
default persistent.ggwp_monika = 0
default persistent.protecc = False
default persistent.parfait_girls = False
default persistent.tea_set = False
default persistent.mc_violent = False
default persistent.poster_seen = False
default persistent.cheat_mod = 0
default poster_checked = False
default closet_checked = False
#########################################
#$ preferences.skip_unseen = False ## For future reference

########## Curse words ############
default fgword = "ucking"
default bword = "itch"
default aword = "sshole"
default sword = "hit"
###################################

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
image bg spoopy = "bg/club-skill.png"
image bg res_gl = "mod_assets/bg/residential_glitch.png"
image p1 = "mod_assets/bg/p1.png"
image p1b = "mod_assets/bg/p1b.png"
image p1a = "mod_assets/bg/p1a.png"
image bg res_gl2 = "mod_assets/bg/residential_glitch2.png"
image bg cr_gl = "mod_assets/bg/class_glitch.png"
######################################################################

####################### Custom audio #################################
define audio.t1g = "mod_assets/sfx/1g.ogg"
define audio.spoopy = "<loop 105.51>mod_assets/sfx/spoopy_glitch.ogg"
define audio.aglitch1 = "mod_assets/sfx/glitch1.ogg"
define audio.t3l = "<loop 4.618>mod_assets/sfx/3l.ogg"
define audio.ap1 = "mod_assets/sfx/p1.ogg"
define audio.aglitch2 = "<loop 0>mod_assets/sfx/glitch2.ogg"
define audio.t2l = "<loop 4.499>mod_assets/sfx/2l.ogg"
define audio.t2o = "<loop 4.492>mod_assets/sfx/2o.ogg"
define audio.gb_gl = "mod_assets/sfx/gb_gl.ogg"
define audio.throw = "mod_assets/sfx/whoosh.ogg" # I know this isn't realistic ffs
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
