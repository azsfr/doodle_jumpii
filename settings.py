# -*- coding: utf-8 -*-
from pygame.font import SysFont
from pygame import init
init()
# ==================================

#Window Settings
XWIN, YWIN = 600,800 #                Resolution
HALF_XWIN,HALF_YWIN = XWIN/2,YWIN/2 # Center
DISPLAY = (XWIN,YWIN)
FLAGS = 0 #                           Fullscreen, resizeable... 
FPS = 60 #                            Render frame rate

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
LIGHT_GREEN = (131,252,107)
ANDROID_GREEN = (164,198,57)
FOREST_GREEN = (87,189,68)
PRUJINKA_IMAGE = "images/пружинка.png"

# Player
PLAYER_SIZE = (100,40)
PLAYER_IMAGE = "images/Enemy_Tank.png"
PLAYER_MAX_SPEED = 20
PLAYER_JUMPFORCE = 20
PLAYER_BONUS_JUMPFORCE = 70
GRAVITY = .98

# Platforms
PLATFORM_GRASS_IMAGE = "images/grass.png"
PLATFORM_ROCK_IMAGE = "images/rock.png"
PLATFORM_SIZE = (100, 35)
PLATFORM_DISTANCE_GAP = (50,210)
MAX_PLATFORM_NUMBER = 10
BONUS_SPAWN_CHANCE = 10
BREAKABLE_PLATFORM_CHANCE = 12

# Fonts
LARGE_FONT = SysFont("",128)
SMALL_FONT = SysFont("arial",24)