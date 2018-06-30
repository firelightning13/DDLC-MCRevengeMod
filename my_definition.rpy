init 10 python:
    config.developer = "auto"

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
default mc_blocked = False
default mc_boring = False # he's literally bored with his life
#############################################
default persistent.day1_gl = 0
default persistent.ggwp_monika = 0
default persistent.accepts_invite = None
default persistent.protecc = False
default persistent.tea_set = False
default persistent.mc_violent = False
default persistent.poster_seen = False
default persistent.cheat_mod = 0
default persistent.mc_realise = False
default persistent.parfait_girls = False
default persistent.natsuki_glitch = 0
default persistent.screen_glitch = 0
default persistent.poetappeal = ""
default persistent.mod_cps = 50
default persistent.played_once = False
#############################################
default persistent.monika_secret = [False, False, False, False]
# 0 = mod-poemresponse.rpy; a serious conversation between monika and mc
# 1 = mod-poemresponse.rpy; where monika failed to explain at the end of her conversation with mc
# 2 = day2b.rpy; natsuki and yuri intense conversations battle
# 3 = day2b.rpy; ny_fight_alt, under if poeappeal == "mp" or "cute"
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
image club_gl2 = "mod_assets/bg/club_room_glitch.png"
image mod_one_eye = "mod_assets/cg/one_eye_gl.png"
image m_smile = "mod_assets/cg/m_smile.png"
image end_credit1 = "mod_assets/cg/end_credit1.png"
image end_credit2 = "mod_assets/cg/end_credit2.png"
image natsuki gl:
    "natsuki 1w"
    0.25
    parallel:
        0.01
        "mod_assets/natsuki/1.png"
        0.01
        "mod_assets/natsuki/2.png"
        0.01
        "mod_assets/natsuki/3.png"
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
######################################################################

################ Custom Transformations and Styles ###################
style window_lq is window:
    background Image("mod_assets/textbox_lq.png", xalign=0.5, yalign=1.0)

style window_ghost is window:
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0, alpha=0.5)

style jp is default:
    font "mod_assets/gui/MSGOTHIC.ttf"
    #kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

transform m_pos:
    xpos 320
    ypos 500

### f21(400) and t22(880) | f32(640) and f33(1040); refer to day2b.rpy
transform mod_pos_gl(x=540, alt_x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    block:
        xcenter alt_x zoom z*1.05
        alpha 1.00
        parallel:
            easein .3 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0
        repeat
    time 1.5
    xcenter x

transform mod_finstant(x=400, z=0.80): # special finstant for yuri; refer to day2b.rpy
        xcenter x yoffset 0 zoom z*1.05 alpha 1.00 yanchor 1.0 ypos 1.03

transform mod_malpha(a=1.00):
    i31
    alpha a
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
define audio.tgl3 = "<loop 4.444>mod_assets/sfx/glitch3.ogg"
define audio.tpj = "<loop 0>mod_assets/sfx/pj.ogg"
define audio.t7fast = "<loop 31.880>bgm/7g.ogg"
define audio.start_gl = "<loop 0>mod_assets/sfx/start_gl.ogg"
define audio.t8g = "<loop 9.938>mod_assets/sfx/8g.ogg"
define audio.t8g2 = "mod_assets/sfx/8g2.ogg"
define audio.dhglitch = "mod_assets/sfx/dhg.ogg"
define audio.dhglitch2 = "<loop 6.424>mod_assets/sfx/dhg2.ogg"
define audio.t99 = "<loop 3.172>mod_assets/sfx/monika_r_u_ok.ogg"
define audio.endc = "<loop 3.172>mod_assets/sfx/end_credit.ogg"
define audio.ngl = "mod_assets/sfx/ngl.ogg"
define audio.end7 = "mod_assets/sfx/7end.ogg"
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
                config.keymap['dismiss'] = dismiss_keys
                renpy.display.behavior.clear_keymap_cache()
                renpy.jump("skip_2_2a")

    def monika_showed_up(event, interact=True, **kwargs):
        if event == "begin":
            config.keymap['dismiss'] = []
            renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
            config.keymap['dismiss'] = dismiss_keys
            renpy.display.behavior.clear_keymap_cache()

    renpy.music.register_channel("trans", mixer="music", tight=True)
