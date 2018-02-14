define config.developer = True #Change this flag to True to enable dev tools

###### Custom persistent and variables ######
default ihorror = False
default isit = False
default accepts_invite = False
default mod_chapter = 0
default poster_checked = False
default closet_checked = False
default seen_day = 0
default parfait_girls = False
default natsuki_out = False
#############################################
default persistent.ggwp_monika = 0
default persistent.accepts_invite = None
default persistent.protecc = False
default persistent.tea_set = False
default persistent.mc_violent = False
default persistent.poster_seen = False
default persistent.cheat_mod = 0
default persistent.mc_realise = False
default persistent.natsuki_glitch = 0
#############################################

#$ preferences.skip_unseen = False ## For future reference
#if persistent.clear[8] == True: ## Accepts sayori's confession in old saves, for future reference.
                                 ## If the player imports their old saves
# image movie_intro = Movie(play="file.ogv", pos=(0, 0), anchor=(0, 0)) ## Just incase if i need this
#$ _history_list[-1].what = "I don't even know what my dad would do if he found this."

########## Curse words ############
default fword = "uck"
default fgword = "ucking"
default bword = "itch"
default aword = "sshole"
default sword = "hit"
###################################

######################## Custom images ###############################
image splash_gl = "mod_assets/bg/splash_glitch.png"
image splash_n = "bg/splash.png"
image intro_rendered:
    "mod_assets/gl/01.png"
    pause 0.5
    "black"
    pause 1.0
    "mod_assets/gl/02.png"
    pause 0.2
    "mod_assets/gl/03.png"
    pause 0.2
    "mod_assets/gl/04.png"
    pause 0.2
    "black"
    pause 1.0
    "mod_assets/gl/05.png"
    pause 0.5
    "mod_assets/gl/06.png"
    pause 0.5
    "black"
    pause 1.0
    "mod_assets/gl/07.png"
    pause 0.3
    "mod_assets/gl/08.png"
    pause 0.3
    "mod_assets/gl/09.png"
    pause 0.5
    "mod_assets/gl/10.png"
    pause 0.2
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
image bg cord_gl = "mod_assets/bg/corridor_glitch.png"
image s_hacker = "mod_assets/cg/s_hacker.png"
image bg club_gl = "mod_assets/bg/club_room_glitch.png"
image mod_one_eye = "mod_assets/cg/one_eye_gl.png"
######################################################################

################ Custom Transformations and Styles ###################
style window_lq is window:
    background Image("mod_assets/textbox_lq.png", xalign=0.5, yalign=1.0)

transform m_pos:
    xpos 320
    ypos 500
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
define audio.sgl = "mod_assets/sfx/select_gl.ogg"
define audio.t2gl = "<loop 4.492>mod_assets/sfx/2gl.ogg"
define audio.t9gl = "<loop 3.172>mod_assets/sfx/9gl.ogg"
define audio.t666 = "<loop 10.893>mod_assets/sfx/666.ogg"
define audio.ggg = "mod_assets/sfx/ggg.ogg"
define audio.s_gl = "mod_assets/sfx/s_gl.ogg"
define audio.fall_gl = "mod_assets/sfx/fall_gl.ogg"
define audio.gl = "mod_assets/sfx/gl.ogg"
######################################################################

###################### Custom Functions ############################
init python:
    def ModWarningSave():
            if not player: return
            persistent.playername = player
            renpy.hide_screen("confirm")
            renpy.jump_out_of_context("start")

    def player_pls_skip(event, interact=True, **kwargs):
        if event == "end":
            if persistent.ggwp_monika >= 3:
                renpy.jump("skip_2_2a")

    def monika_showed_up(event, interact=True, **kwargs):
        if event == "begin":
           config.keymap['dismiss'] = []
           renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
           config.keymap['dismiss'] = dismiss_keys
           renpy.display.behavior.clear_keymap_cache()

    renpy.music.register_channel("trans", mixer="music", tight=True)

    #def censorship():
        #if persistent.protecc:
            #fgword = "******"
            #bword = "****"
            #aword = "******"
            #sword = "***"
####################################################################
