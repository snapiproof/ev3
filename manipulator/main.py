from math import atan2, degrees, acos, pi, sin, cos

l1 = 0
l2 = 100
l3 = 100


'''x = 15
y = 0
z = 0


alf = atan2(y, x)
r_xy = (x**2 + y**2)**0.5

c = ( (z - l1)**2 + r_xy**2 )**0.5

bet = pi/2 - atan2(z - l1, r_xy) - acos( (l2**2 + c**2 - l3**2)/(2*l2*c) )

gam = pi - acos( (l2**2 + l3**2 - c**2)/(2*l2*l3) )




alf = degrees(alf)
bet = degrees(bet)
gam = degrees(gam)



print(alf,bet,gam)'''


Z = 0
X = 0

import pygame


pygame.init()
width = 500
height = 500

zd = 8

fon = (255,255,255)

wind = pygame.display.set_mode((width,height))

x0 = width//2
y0 = height//2


RUNGAME = True

def line(ot, do):
    pygame.draw.line(wind, (0,0,0), (ot[0] + x0, y0 - ot[1]), (do[0] + x0, y0 - do[1]))

log = False    
wind.fill(fon)
while RUNGAME:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            RUNGAME = False
            break
        elif (event.type == pygame.MOUSEMOTION) :
            X = event.pos[0] - x0
            Z = y0 - event.pos[1]


    x = X
    y = 0
    z = Z

    try:

        alf = atan2(y, x)
        
        r_xy = (x**2 + y**2)**0.5
        

        c = ( (z - l1)**2 + r_xy**2 )**0.5

        bet = pi/2 - atan2(z - l1, r_xy) - acos( (l2**2 + c**2 - l3**2)/(2*l2*c) )

        gam = pi - acos( (l2**2 + l3**2 - c**2)/(2*l2*l3) )
        
        log = False
        print(alf)

        wind.fill(fon)
        x1,y1 = sin(bet)*l2, cos(bet)*l2
        dx2, dy2 = sin(bet+gam)*l3, cos(bet+gam)*l3
        
        line((0, 0), (x1, y1))
        line((x1,y1), (x1 + dx2,y1 + dy2))
        #pygame.draw.circle(wind, (0,0,0), (x0, y0), l2 - l3, 1)

    except:   
        if not(log):
            print("Не могу достать")
            log = True


    
    


    pygame.display.update()
    pygame.time.delay(zd)
    
    
   
    




pygame.quit()

















