import pygame
import starting_screen
import choose_color
import player
import board_screen
import bg
import win_screen
import details_screen

def run(DISPLAY):
    #parallax background
    background = bg.parallax_bg(DISPLAY, "ashwin/snek_bg.jpg")

    
    start_screen = starting_screen.starting_screen(DISPLAY, background)

    #start screen has choice between singleplayer/multiplayer
    choice = start_screen.draw()
    
    
    if choice == 'sp': #singleplayer against AI
        color_choose = choose_color.choose_screen(DISPLAY, background)
        col = color_choose.draw() #choice of pawn color
        plyrs = []
        ai_col = (0,255,255)
        plyrs.append(player.player(DISPLAY, "player", col)) #player
        plyrs.append(player.player(DISPLAY, "AI", ai_col, True)) #ai

        bored = board_screen.board_screen(DISPLAY, plyrs)
        bored.draw()

        w_screen = win_screen.win_screen(DISPLAY, background, bored.winner)
        w_screen.draw()

    elif choice == 'mp':
        players = []
        player_colors = [(255,0,0),(0,255,0),(0,0,255),(255,0,255)]
        details = details_screen.details_screen(DISPLAY, background)
        player_names = details.draw()
        for c,n in enumerate(player_names):
            players.append(player.player(DISPLAY, n, player_colors[c]))

        bored = board_screen.board_screen(DISPLAY, players)
        bored.draw()

        w_screen = win_screen.win_screen(DISPLAY, background, bored.winner)
        w_screen.draw()
            
        

        


        



