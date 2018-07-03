from visual import *
from visual.controls import *
import random
N=500
OBSERV_TIME=1000
WAITING_TIME=-1000
side=2000
room_wall=2400
Radius=50

rw=2*room_wall+1
M=0.029
T=298
R=8.31
g=9.8
bv=(2*R*T/M)**0.5

def ch_vel_xy(bv):
    A = bv*0.9/3
    B = bv*1.1/3
    return random.uniform(A, B)

def ch_vel_z(bv, vx, vy):
    A = bv*0.9/3
    B = bv*1.1/3
    try:
        return (bv**2-vx**2-vy**2)**0.5
    except:
        print(bv, vx, vy)
        print(bv**2-vx**2-vy**2)
        return vz
            
        

sc=display(menus = True, title='Ideal Gas',width=625,height=650,
           center=(0,0,0), background=(1,1,1))
wall1 = box(pos=vector(-room_wall,0,0), size=(1, rw, rw), color=(0,0,0), )
wall2 = box(pos=vector(0,0,-room_wall), size=(rw, rw, 1), color=(0,0,0), )
wall3 = box(pos=vector(room_wall,0,0), size=(1, rw, rw), color=(0,0,0), )
wall4 = box(pos=vector(0,-room_wall,0), size=(rw, 1, rw), color=(0,0,0), )
wall5 = box(pos=vector(0, room_wall,0), size=(rw, 1, rw), color=(0,0,0), )

wall_1 = box(pos=vector(-side,0,0), opacity=0.15,
            size=(1., 2*side+1., 2*side+1.), color=(1,1,1), )
wall_2 = box(pos=vector(0,0,-side), opacity=0.15,
            size=(2*side+1., 2*side+1., 1.), color=(1,1,1), )
wall_3 = box(pos=vector(side,0,0), opacity=0.15,
            size=(1., 2*side+1., 2*side+1.), color=(1,1,1), )
wall_4 = box(pos=vector(0,-side,0), opacity=0.15,
            size=(2*side+1., 1., 2*side+1.), color=(1,1,1), )
wall_5 = box(pos=vector(0, side,0), opacity=0.15,
            size=(2*side+1., 1., 2*side+1.), color=(1,1,1), )

BALLS=[]
balls_velocities=[]
VX=0
VY=0
VZ=0
VV=0

znaki=[random.random() for u in range(62)]
for o in range(len(znaki)):
    if znaki[o] > 0.5:
        znaki[o] = 1
    else:
        znaki[o] = -1

def zn():
    return znaki[random.randint(0, 60)]

for f in range(N):
    vx=ch_vel_xy(bv)
    vy=ch_vel_xy(bv)
    vz=ch_vel_z(bv, vx, vy)
    balls_velocities.append([int(vx),int(vy),int(vz)])
    BALLS.append(sphere(pos=vector(0,0,0),
                        velocity=vector(vx*zn(),vy*zn(),vz*zn()),
                        color=(random.random(),random.random(),random.random()),
                        radius = Radius, material=materials.wood))
    VX+=vx*zn()
    VY+=vy*zn()
    VZ+=vz*zn()
    VV+=(vx**2+vy**2+vz**2)**0.5
print(int(VX/N), int(VY/N), int(VZ/N))
print(int(VV/N))

dt = 0.1
time_count = WAITING_TIME
A = 0
B = 0
C = 0
D = 0
E = 0
max = 0
min = 0
zero_height = -side+2*Radius
layer_height = (2*side-4*Radius)/5

while True:
    time_count += 1
    rate(100)
    for ball in BALLS:
        if abs(ball.pos.x) >= side-Radius*2:
            ball.velocity.x *= (-1)
            vy=ch_vel_xy(bv)
            vz=ch_vel_z(bv, ball.velocity.x, vy)
            a0=zn()
            b0=zn()
            ball.velocity.y = a0*vy
            ball.velocity.z = b0*vz
        if abs(ball.pos.y) >= side-Radius*2:
            ball.velocity.y *= (-1)
            vx=ch_vel_xy(bv)
            vz=ch_vel_z(bv, vx, ball.velocity.y)
            a0=zn()
            b0=zn()
            ball.velocity.x = a0*vx
            ball.velocity.z = b0*vz
        if abs(ball.pos.z) >= side-Radius*2:
            ball.velocity.z *= (-1)
            vy=ch_vel_xy(bv)
            vz=ch_vel_z(bv, ball.velocity.z, vy)
            a0=zn()
            b0=zn()
            ball.velocity.y = a0*vy
            ball.velocity.x = b0*vz
            
        if time_count >= 0:
            if ball.pos.y <= zero_height+layer_height:
                A += 1
            elif ball.pos.y <= zero_height+layer_height*2:
                B += 1
            elif ball.pos.y <= zero_height+layer_height*3:
                C += 1
            elif ball.pos.y <= zero_height+layer_height*4:
                D += 1
            else:
                E += 1
        if ball.pos.y > max:
            max = ball.pos.y
        elif ball.pos.y < min:
            min = ball.pos.y
        
        ball.pos += ball.velocity*dt
        if ball.pos.y > -(side-Radius*2):
            ball.pos.y -= g*dt**2/2

        if time_count == OBSERV_TIME:
            def expected(lvl):
                return str(int((A*2.7183**(-M*g*layer_height*lvl/R/T))/time_count))
            print('In block A: '+str(A//OBSERV_TIME)+', expected: '+str(int(A/time_count)))
            print('In block B: '+str(B//OBSERV_TIME)+', expected: '+expected(2))
            print('In block C: '+str(C//OBSERV_TIME)+', expected: '+expected(3))
            print('In block D: '+str(D//OBSERV_TIME)+', expected: '+expected(4))
            print('In block E: '+str(E//OBSERV_TIME)+', expected: '+expected(5))
            print("Corpuscules' number is "+str(N))
            print("Observation's time is "+str(time_count))
            sc.waitfor('click')


