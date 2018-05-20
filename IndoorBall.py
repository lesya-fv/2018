from __future__ import division, print_function
from visual import *
from visual.controls import *
import threading
from visual.graph import *
import wx
import timeit
import random
from random import sample

manage = 'mouse'

def instruction():
    instr_label=label(pos=(0, 0, 0), text='Use mouse to control the spider',
                      height=25, border=50, color=(0, 1, 1), opacity=0.5)
    sleep(3)
    instr_label.visible=0
    del instr_label

def instruction1():
    instr_label=label(pos=(0, 0, 0), text='Use keyboard to control the spider',
                      height=25, border=50, color=(0, 1, 1), opacity=0.5)
    sleep(3)
    instr_label.visible=0
    del instr_label

def mouse_control(sc, spider):
    if sc.mouse.clicked:
            p = sc.mouse.getclick().pos
            distance = p - spider.pos
            if distance != (0, 0, 0):
                spider.pos += distance/2.5

def keyboard_control(sc, spider, dist):
    def keyInput(evt):
        s = evt.key
        if spider.pos.x + 2.5 < 11.9 and s == 'right':
            spider.pos.x += dist
        elif spider.pos.x - 2.5 > -11.9 and s == 'left':
            spider.pos.x -= dist
        elif spider.pos.z - 2.5 > -11.9 and s == 'up':
            spider.pos.z -= dist
        elif spider.pos.z + 2.5 < 11.9 and s == 'down':
            spider.pos.z += dist
    sc.bind('keydown', keyInput)

def Simple_Game(sc, manage, level, absolute_win):
    walls_number = 1
    blocks_number = (level+1)**2
    blocks_creation=[]
    blocks_coords=[]
    b_size = 3
    
    def division(blocks_number, walls_number):
        if blocks_number >= 12:
            blocks_number = int(blocks_number/2)
            walls_number *= 2
            b_size = 1
        return walls_number
    
    walls_number=division(blocks_number, walls_number)

    def blocks(blocks_number, walls_number):
        random_pos=[sample(range(-10, 10), k=blocks_number)
                    for H in range(walls_number)]
        walls_pos=[11, -11]
        for i1 in range(walls_number):
            pos_y = walls_pos[i1]
            for j1 in range(blocks_number):
                pos_x = random_pos[i1][j1]
                pos_z = random_pos[-i1][-j1]
                blocks_coords.append([pos_x,pos_y,pos_z])
                blocks_creation.append(box(pos=vector(pos_x, pos_y, pos_z),
                                   size=(b_size, 1., b_size),
                                           color=(random.random(),
                                                      random.random(),
                                                      random.random()), ))

    wall1 = box(pos=vector(-12,0,0), size=(1., 25., 25.), color=(0.8, 0, 1), )
    wall2 = box(pos=vector(0,0,-12), size=(25., 25., 1.), color=(0.8, 0, 1), )
    wall3 = box(pos=vector(12,0,0), size=(1., 25., 25.), color=(0.8, 0, 1), )
    wall4 = box(pos=vector(0,-12.5,0), size=(25., 0., 25.), color=(0.8, 0, 1), )
    wall5 = box(pos=vector(0, 12,0), size=(25., 1., 25.), color=(0.8, 0, 1), )

    velocity=0.8
    ball = sphere( pos=vector(0,0,0),
                   velocity=vector(velocity+0.15, -velocity-0.2, velocity-0.05),
                   color=(0, 1, 1), radius = 1)
    A=[]
    AA=[]
    ASAS=[]
    BL=[]
    
    spider = box(pos=vector(0,-7,0), size=(5., 1., 5.), color=(0.5, 0.5, 0.5), )
    
    blocks(blocks_number, walls_number)
    
    def stars(a, b, c):
        if b == 11:
            random_numbers_i = [random.uniform(8, 11) for ran in range(4)]
        elif b == -11:
            random_numbers_i = [random.uniform(-11, -8) for ran in range(4)]
        random_numbers_j = [random.uniform(-3, 3) for rand in range(4)]
        random_numbers_s = [random.uniform(-pi, 0) for randi in range(4)]
        
        for i in random_numbers_i:
            for j in random_numbers_j:
                for k in random_numbers_j:
                    A.append(points(pos=[vector(a+j-0.25-i/20,i-0.25,c+k-0.25-i/20),
                                vector(a+k+0.25+i/20,i+0.25,c+j+0.25+i/20)],
                           radius=i, color=(random.random(),random.random(),random.random()),
                                    visible = 0.5))
        for ii in random_numbers_i:
            for jj in random_numbers_j:
                for kk in random_numbers_j:
                    AA.append(points(pos=[vector(a+jj-0.25-ii/30,ii-0.25,c+kk-0.25-ii/30),
                                vector(a+jj+0.25+ii/30,ii+0.25,c+kk+0.25+ii/30)],
                           radius=ii, color=color.red))
        for iii in random_numbers_i:
            for jjj in random_numbers_j:
                for kkk in random_numbers_j:
                    ASAS.append(points(pos=[vector(a+jjj-0.3-iii/30,iii-0.25,c+kkk-0.3-iii/30),
                                vector(a+jjj+0.3+iii/30,iii+0.25,c+kkk+0.3+iii/30)],
                           radius=jjj, color=(random.random(),random.random(),random.random()),
                                       visible = 0.5))

        for I in random_numbers_i:
            for J in random_numbers_s:
                BL.append(sphere(pos=vector(a-I/3*cos(J), I,
                                           c-I/3*sin(J)), radius=0.2, color=color.orange))


    def stars_disappear():
        for t0 in A:
            t0.visible = 0
        for t1 in AA:
            t1.visible = 0
        for t2 in ASAS:
            t2.visible = 0
        for t3 in BL:
            t3.visible = 0

    def control(sc, spider):
        if manage == 'mouse':
            mouse_control(sc, spider)
        else:
            keyboard_control(sc, spider, dist)

        
    dt = 0.15
    dist = 0.01
    WIN = blocks_number
    
    while True:
        rate(50)
        dist *= 0.99
        control(sc, spider)
                    
        if ball.pos.x <= -10.8 or ball.pos.x >= 10.8:
            ball.velocity.x *= (-1)
        if ball.pos.y <= -11.8 or ball.pos.y >= 10.8:
            ball.velocity.y *= (-1)
        if ball.pos.z <= -10.8 or ball.pos.z >= 10.8:
            ball.velocity.z *= (-1)
        if (ball.pos.y <= spider.pos.y + 1.2 and ball.pos.y > spider.pos.y or ball.pos.y >= spider.pos.y + 1.2 and ball.pos.y < spider.pos.y) and ball.pos.x >= spider.pos.x-3 and ball.pos.x <= spider.pos.x+3 and ball.pos.z >= spider.pos.z-3 and ball.pos.z >= spider.pos.z-3:
            ball.velocity *= (-1)
        if ball.pos.y <= spider.pos.y + 1.2 and ball.pos.y >= spider.pos.y - 1.2:
            if(ball.pos.x > spider.pos.x and ball.pos.x <= spider.pos.x + 3.2 or ball.pos.x < spider.pos.x and ball.pos.x >= spider.pos.x + 3.2):
                ball.velocity.x *= (-1)
            if (ball.pos.z > spider.pos.z and ball.pos.z <= spider.pos.z + 3.2 or ball.pos.z < spider.pos.z and ball.pos.z >= spider.pos.z + 3.2):
                ball.velocity.z *= (-1)
        
        ball.pos += ball.velocity*dt
        count = -1
        
        for u in range(len(blocks_coords)):
                count += 1
                
                if ball.pos.y >= 8.8:
                    if blocks_coords[count][0] - 2.2 <= ball.pos.x and blocks_coords[count][0] + 2.2 >= ball.pos.x:
                        if blocks_coords[count][2] - 2.2 <= ball.pos.z and blocks_coords[count][2] + 2.2 >= ball.pos.z:

                            b=11
                            a=blocks_coords[count][0]
                            c=blocks_coords[count][2]
                            stars(a, b, c)
                            ball.velocity.y*=(-1)
                            
                            try:
                                del blocks_coords[u]
                                blocks_creation[count].visible = False
                                del blocks_creation[count]
                                WIN -= 1
                            
                                count -= 1
                                sleep(0.02)
                                stars_disappear()
                            except:
                                pass

                elif level >=3 and ball.pos.y <= -8.8:
                    if blocks_coords[count][0] - 2.2 <= ball.pos.x and blocks_coords[count][0] + 2.2 >= ball.pos.x:
                        if blocks_coords[count][2] - 2.2 <= ball.pos.z and blocks_coords[count][2] + 2.2 >= ball.pos.z:
                            b=-11
                            a=blocks_coords[count][0]
                            c=blocks_coords[count][2]
                            stars(a, b, c)
                            ball.velocity.y*=(-1)
                            
                            try:
                                del blocks_coords[u]
                                blocks_creation[count].visible = False
                                del blocks_creation[count]
                                WIN -= 1
                            
                                count -= 1
                                sleep(0.02)
                                stars_disappear()
                            except:
                                pass
                            
        if WIN == 0:
            labelwin=label(pos=(0, 0, 0), text='YOU WIN',
                      height=50, border=50, color=(0, 1, 1), opacity=0.5)
            sleep(2)
            labelwin.text = 'SCORE:'+str(level*100)
            level += 1
            spider.visible=0
            ball.visible=0
            sleep(1)
            labelwin.visible=0
            del spider
            del ball
            
            if level == 4:
                absolute_win = 1
                labelwin.text = 'ABSOLUTE WINNER!'
                Menu()
            else:
                labelwin.text = 'LEVEL'+str(level)
                sleep(1)
                Simple_Game(sc, manage, level, 0)
        
    
def leave(evt):
    exit()
    
def begin():
    scene=display(menus = True, title='GAME',width=950,height=725,
                  center=(0,0,0), background=(0.1, 0.1, 0.1),)

    labelplay=label(pos=(0, 45, 0), text='PLAY', height=100, border=50,
                    color=(0, 1, 1), linecolor=(0.5, 0.5, 0.5))
    play_text1 = text(text='\n\nclick PLAY to begin\nclick FILE to exit',
                     align='center', height=25, color=(0.2, 0.2, 0.2),)    

    scene.waitfor('click keydown')
    labelplay.linecolor=(0, 1, 1)
    play_text1.color=scene.background
    labelplay1=label(pos=(0, -20, 0), text='click again to begin',
                     height=25, color=(0, 1, 1), linecolor=scene.background)

    scene.waitfor('click keydown')
    
    labelplay.height = 25
    labelplay.text = 'Enter your name, please:'
    labelplay.linecolor=scene.background
    labelplay.color=color.white

    labelplay1.visible = 0
    del labelplay1
    play_text1.visible = 0
    del play_text1

    player_s_name = label(pos=(0, 0, 0), text='', height=50,
                  border=20, color=(0, 1, 1), linecolor=(0.5, 0.5, 0.5))

    def nameInput(evt):
        name_lit = evt.key
        if len(name_lit) == 1:
            player_s_name.text += name_lit # append new character
        elif ((name_lit == 'backspace' or s == 'delete') and
                len(player_s_name.text)) > 0:
            if evt.shift:
                player_s_name.text = '' # erase all text
            else:
                player_s_name.text = player_s_name.text[:-1] # erase letter

    scene.bind('keydown', nameInput)
    scene.waitfor('click')
    Name = player_s_name.text
    name = 'Hello, '+Name+' !'
    sleep(0.2)
    labelplay.visible = 0
    labelplay.text = name
    labelplay.color = color.white
    player_s_name.visible = 0
    labelplay.pos=(0,0,0)
    labelplay.height = 75
    labelplay.visible = 1
    sleep(3)
    labelplay.visible = 0
    sleep(0.5)

    scene.delete()
    return Name


def New_Game_Mouse():
    scene=window(menus = False, title='GAME',width=900,height=725,
                 center=(0,0,0), background=(0,1,1),
                 style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

    p = scene.panel
    
    def make_pause(evt):
        sc.waitfor('click')

    pause_button = wx.Button(p, label='Pause', pos=(728,285))
    pause_button.Bind(wx.EVT_BUTTON, make_pause)

    exit_program_button = wx.Button(p, label='Exit', pos=(728,435))
    exit_program_button.Bind(wx.EVT_BUTTON, leave)

    def play_new_game(evt):
        sc.delete()
        New_Game_Mouse()

    new_game_button = wx.Button(p, label='New Game', pos=(728,235))
    new_game_button.Bind(wx.EVT_BUTTON, play_new_game)

    def BMenu(evt):
        Menu()

    def Bbegin(evt):
        begin()

    back_game_button = wx.Button(p, label='Return', pos=(728,335))
    back_game_button.Bind(wx.EVT_BUTTON, BMenu)

    menu_game_button = wx.Button(p, label='Menu', pos=(728,385))
    menu_game_button.Bind(wx.EVT_BUTTON, Bbegin)    
    
    sc = display(window=scene, title='GAME',width=625,height=625,
                 center=(0,0,0), background=(0.25,0.25,0.25),
               style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    instruction()

    Simple_Game(sc, 'mouse', 1, 0)            


def New_Game_Keyboard():
    sc = display(menus = False, title='GAME',width=950,height=725,
                 center=(0,0,0), background=(0.25,0.25,0.25),
               style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    menu1 = box(pos=vector(15.1,0,12.5), size=(4., 25., 0.), color=(0, 1, 1), )
    menu2 = box(pos=vector(-15,0,12.5), size=(4., 25., 0.), color=(0, 1, 1), )

    instruction1()

    Simple_Game(sc, 'keyboard', 1, 0)


def Menu():
    menu=window(menus = False, title='MENU',width=900,height=725,
                center=(0,0,0), background=(0,1,1),
                style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

    pu = menu.panel
    
    exit_program_button = wx.Button(pu, label='Exit', pos=(430,435))
    exit_program_button.Bind(wx.EVT_BUTTON, leave)

    back_button = wx.Button(pu, label='Return', pos=(430,385))
    back_button.Bind(wx.EVT_BUTTON, begin)

    wx.StaticText(pu, pos=(371, 125),
                  label='How do you want to manage your ball?') 
    
    def m_mouse(evt):
        manage = 'mouse'
        New_Game_Mouse()

    def m_keyboard(evt):
        manage = 'keyboard'
        New_Game_Keyboard()

    m_mouse_button = wx.Button(pu, label='Mouse', pos=(369,155))
    m_mouse_button.Bind(wx.EVT_BUTTON, m_mouse)
    
    m_keyboard_button = wx.Button(pu, label='Keyboard', pos=(492,155))
    m_keyboard_button.Bind(wx.EVT_BUTTON, m_keyboard)
    
begin()
Menu()

