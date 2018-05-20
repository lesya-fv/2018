from visual import *
from visual.controls import *
import threading
import random

scene=display(menus = True, title='Simple Game',width=625,height=625,center=(0,0,0),
                                               background=(1,1,1))
wall1 = box(pos=vector(-12,0,0), size=(1., 25., 25.), color=(0.8, 0, 1), )
wall2 = box(pos=vector(0,0,-12), size=(25., 25., 1.), color=(0.8, 0, 1), )
wall3 = box(pos=vector(12,0,0), size=(1., 25., 25.), color=(0.8, 0, 1), )
wall4 = box(pos=vector(0,-12.5,0), size=(25., 0., 25.), color=(0.8, 0, 1), )
wall5 = box(pos=vector(0, 12,0), size=(25., 1., 25.), color=(0.8, 0, 1), )

ball = sphere( pos=vector(0,0,0), velocity=vector(1, -1, 1),
               color=(0, 1, 1), radius = 1)
A=[]
AA=[]
ASAS=[]
BL=[]
spider = box(pos=vector(0,-7,0), size=(5., 1., 5.), color=(0.5, 0.5, 0.5), )
def stars(a, c):
    random_numbers_i = [random.uniform(8, 11) for ran in range(4)]
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


block1 =box(pos=vector(-7, 10, -7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block2 =box(pos=vector(-7, 10, 0), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block3 =box(pos=vector(-7, 10, 7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block4 =box(pos=vector(0, 10, -7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block5 =box(pos=vector(0, 10, 0), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block6 =box(pos=vector(0, 10, 7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block7 =box(pos=vector(7, 10, -7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block8 =box(pos=vector(7, 10, 0), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )
block9 =box(pos=vector(7, 10, 7), size=(3., 1., 3.), color=(0.25, 0.25, 0.25), )

blocks_coords = []
blocks = {0: block1, 1: block2, 2: block3, 3: block4,
          4: block5, 5: block6, 6: block7, 7: block8, 8: block9}
for j in range(3):
    for q in range(3):
        blocks_coords.append([-7+7*j, 10, -7+7*q])

dt = 0.15
while True:
    rate(50)
    if scene.mouse.clicked:
        p = scene.mouse.getclick().pos
        distance = p - spider.pos
        if distance != (0, 0, 0):
            spider.pos += distance/5
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
                        a=blocks_coords[count][0]
                        c=blocks_coords[count][2]
                        stars(a, c)
                        ball.velocity.y*=(-1)
                        del blocks_coords[u]
                        blocks[count].visible = False
                        del blocks[count]
                        
                        count -= 1
                        blocks_parts = {}
                        for s in range(count+2, len(blocks_coords)+1):
                            blocks_parts[s-1] = blocks.pop(s)
                            blocks.update(blocks_parts)

                        sleep(0.02)
                        stars_disappear() 
                        
