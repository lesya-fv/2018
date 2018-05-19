from __future__ import division, print_function
from visual import *
from visual.controls import *
import threading
from visual.graph import *
import wx
import timeit

manage = 'mouse'

def walls():
    wall1 = box(pos=vector(-12,0,0), size=(1., 25., 25.),
                color=(0.8, 0, 1), material=materials.marble )
    wall2 = box(pos=vector(0,0,-12), size=(25., 25., 1.),
                color=(0.8, 0, 1), material=materials.marble )
    wall3 = box(pos=vector(12,0,0), size=(1., 25., 25.),
                color=(0.8, 0, 1), material=materials.marble )
    wall4 = box(pos=vector(0,-12.5,0), size=(25., 0., 25.),
                color=(0.8, 0, 1), material=materials.marble )
    wall5 = box(pos=vector(0, 12,0), size=(25., 1., 25.),
                color=(0.8, 0, 1), material=materials.marble )

def leave(evt):
    exit()

def instruction():
    instr_label=label(pos=(0, 0, 0), text='Use mouse to manage your ball',
                      height=25, border=50, color=(0, 1, 1), opacity=0.5)
    sleep(3)
    instr_label.visible=0
    del instr_label

def instruction1():
    instr_label=label(pos=(0, 0, 0), text='Use keyboard to manage your ball',
                      height=25, border=50, color=(0, 1, 1), opacity=0.5)
    sleep(3)
    instr_label.visible=0
    del instr_label
    
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
    scene.delete()

def New_Game_Mouse():
    scene=window(menus = False, title='GAME',width=900,height=725,
                 center=(0,0,0), background=(0,1,1),
                 style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

    sc = display(window=scene, x=25, y=25, width=625, height=625,
                 background=(0.15, 0.15, 0.15))

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
    
    walls()
    instruction()

    ball = sphere( pos=vector(0,0,0), velocity=vector(1, -1, 1),
                   color=(0, 1, 1), radius = 1,)
    spider = box(pos=vector(0,-7,0), size=(5., 1., 5.),
                 color=(0.5, 0.5, 0.5), visible=0.5)

    block1 =box(pos=vector(-7, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block2 =box(pos=vector(-7, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block3 =box(pos=vector(-7, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block4 =box(pos=vector(0, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block5 =box(pos=vector(0, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block6 =box(pos=vector(0, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block7 =box(pos=vector(7, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block8 =box(pos=vector(7, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block9 =box(pos=vector(7, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)

    blocks_coords = []
    blocks = {0: block1, 1: block2, 2: block3, 3: block4,
              4: block5, 5: block6, 6: block7, 7: block8, 8: block9}

    for j in range(3):
        for q in range(3):
            blocks_coords.append([-7+7*j, 10, -7+7*q])

    dt = 0.15
    WIN = 9
    
    while True:
        rate(50)

        if sc.mouse.clicked:
            p = sc.mouse.getclick().pos
            distance = p - spider.pos
            if distance != (0, 0, 0):
                spider.pos += distance/2.5

        if ball.pos.x <= -10.7 or ball.pos.x >= 10.7:
            ball.velocity.x *= (-1)
        if ball.pos.y <= -11.7 or ball.pos.y >= 10.7:
            ball.velocity.y *= (-1)
        if ball.pos.z <= -10.7 or ball.pos.z >= 10.7:
            ball.velocity.z *= (-1)

        if (ball.pos.y <= spider.pos.y + 1.2 and ball.pos.y > spider.pos.y or ball.pos.y >= spider.pos.y + 1.2 and ball.pos.y < spider.pos.y) and ball.pos.x >= spider.pos.x-3 and ball.pos.x <= spider.pos.x+3 and ball.pos.z >= spider.pos.z-3 and ball.pos.z >= spider.pos.z-3:
            ball.velocity.y *= (-1)
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
                            ball.velocity.y*=(-1)
                            del blocks_coords[u]
                            blocks[count].visible = False
                            del blocks[count]
                            WIN -= 1

                            count -= 1
                            blocks_parts = {}
                            for s in range(count+2, len(blocks_coords)+1):
                                blocks_parts[s-1] = blocks.pop(s)
                                blocks.update(blocks_parts)

        if WIN == 0:
            labelwin=label(pos=(0, 0, 0), text='YOU WIN',
                      height=50, border=50, color=(0, 1, 1), opacity=0.5)
            sleep(3)
            sc.delete()
            try:
                scene.delete()
                begin()
            except:
                begin()
            


def New_Game_Keyboard():
    sc = display(menus = False, title='GAME',width=950,height=725,
                 center=(0,0,0), background=(0.25,0.25,0.25),
               style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

    menu1 = box(pos=vector(15.1,0,12.5), size=(4., 25., 0.),
                color=(0, 1, 1), material=materials.marble, )
    menu2 = box(pos=vector(-15,0,12.5), size=(4., 25., 0.),
                color=(0, 1, 1), material=materials.marble, )

    walls()
    instruction1()

    ball = sphere( pos=vector(0,0,0), velocity=vector(1, -1, 1),
                   color=(0, 1, 1), radius = 1,)
    spider = box(pos=vector(0,-10,0), size=(5., 1., 5.),
                 color=(0.5, 0.5, 0.5), visible=0.5)

    block1 =box(pos=vector(-7, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block2 =box(pos=vector(-7, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block3 =box(pos=vector(-7, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block4 =box(pos=vector(0, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block5 =box(pos=vector(0, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block6 =box(pos=vector(0, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block7 =box(pos=vector(7, 10, -7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block8 =box(pos=vector(7, 10, 0), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)
    block9 =box(pos=vector(7, 10, 7), size=(3., 1., 3.),
                color=(0.25, 0.25, 0.25), material=materials.wood)

    blocks_coords = []
    blocks = {0: block1, 1: block2, 2: block3, 3: block4,
              4: block5, 5: block6, 6: block7, 7: block8, 8: block9}

    for j in range(3):
        for q in range(3):
            blocks_coords.append([-7+7*j, 10, -7+7*q])

    dt = 0.15
    WIN = 9

    def keyInput(evt):
        s = evt.key
        if spider.pos.x + 2.5 < 11.9 and s == 'right':
                spider.pos.x += 0.01
        elif spider.pos.x - 2.5 > -11.9 and s == 'left':
                spider.pos.x -= 0.01
        elif spider.pos.z - 2.5 > -11.9 and s == 'up':
                spider.pos.z -= 0.01
        elif spider.pos.z + 2.5 < 11.9 and s == 'down':
                spider.pos.z += 0.01

    while True:
        rate(50)

        sc.bind('keydown', keyInput)
                
        if ball.pos.x <= -10.7 or ball.pos.x >= 10.7:
            ball.velocity.x *= (-1)
        if ball.pos.y <= -11.7 or ball.pos.y >= 10.7:
            ball.velocity.y *= (-1)
        if ball.pos.z <= -10.7 or ball.pos.z >= 10.7:
            ball.velocity.z *= (-1)

        if (ball.pos.y <= spider.pos.y + 1.2 and ball.pos.y > spider.pos.y or ball.pos.y >= spider.pos.y + 1.2 and ball.pos.y < spider.pos.y) and ball.pos.x >= spider.pos.x-3 and ball.pos.x <= spider.pos.x+3 and ball.pos.z >= spider.pos.z-3 and ball.pos.z >= spider.pos.z-3:
            ball.velocity.y *= (-1)
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
                            ball.velocity.y*=(-1)
                            del blocks_coords[u]
                            blocks[count].visible = False
                            del blocks[count]
                            WIN -= 1

                            count -= 1
                            blocks_parts = {}
                            for s in range(count+2, len(blocks_coords)+1):
                                blocks_parts[s-1] = blocks.pop(s)
                                blocks.update(blocks_parts)

        if WIN == 0:
            labelwin=label(pos=(0, 0, 0), text='YOU WIN',
                      height=25, border=50, color=(0, 1, 1), opacity=0.5)
            sleep(3) 
            sc.delete()
            try:
                scene.delete()
                begin()
            except:
                begin()

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

