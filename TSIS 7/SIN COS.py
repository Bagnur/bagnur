import pygame
import sys
import math





pygame.init()


screen = pygame.display.set_mode((800,600))


pygame.display.set_caption("SIN,COS")
xy = [ ]
xyy=[ ]
r=True
n=6
A=180
screen.fill([255,255,255])

pygame.draw.rect(screen, (0,0,0), (30,50, 740 , 400), 4)

pygame.draw.line(screen, (0,0,0), (30,70),(770,70), 2)
pygame.draw.line(screen, (0,0,0), (30,81.25),(36,81.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+2*11.25),(40,70+2*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+3*11.25),(36,70+3*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,115),(770,115), 2)
pygame.draw.line(screen, (0,0,0), (30,70+5*11.25),(36,70+5*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+6*11.25),(40,70+6*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+7*11.25),(36,70+7*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,160),(770,160), 2)
pygame.draw.line(screen, (0,0,0), (30,70+9*11.25),(36,70+9*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+10*11.25),(40,70+10*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+11*11.25),(36,70+11*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,205),(770,205), 2)
pygame.draw.line(screen, (0,0,0), (30,70+13*11.25),(36,70+13*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+14*11.25),(40,70+14*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+15*11.25),(36,70+15*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,250),(770,250), 3)
pygame.draw.line(screen, (0,0,0), (30,70+17*11.25),(36,70+17*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+18*11.25),(40,70+18*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+19*11.25),(36,70+19*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,295),(770,295), 2)
pygame.draw.line(screen, (0,0,0), (30,70+21*11.25),(36,70+21*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+22*11.25),(40,70+22*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+23*11.25),(36,70+23*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,340),(770,340), 2)
pygame.draw.line(screen, (0,0,0), (30,70+25*11.25),(36,70+25*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+26*11.25),(40,70+26*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+27*11.25),(36,70+27*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,385),(770,385), 2)
pygame.draw.line(screen, (0,0,0), (30,70+29*11.25),(36,70+29*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+30*11.25),(40,70+30*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,70+31*11.25),(36,70+31*11.25), 2)
pygame.draw.line(screen, (0,0,0), (30,430),(770,430), 2)

pygame.draw.rect(screen, (0,0,0), (50,70, 700 , 360), 2)

pygame.draw.line(screen, (0,0,0), (50,50),(50,450), 2)

pygame.draw.line(screen, (0,0,0), (166.6,50),(166.6,450), 2)

pygame.draw.line(screen, (0,0,0), (283.3,50),(283.3,450), 2)

pygame.draw.line(screen, (0,0,0), (399.9,50),(399.9,450), 3)

pygame.draw.line(screen, (0,0,0), (516.6,50),(516.6,70), 2)

pygame.draw.line(screen, (0,0,0), (516.6,115),(516.6,450), 2)

pygame.draw.line(screen, (0,0,0), (633.3,50),(633.3,450), 2)
pygame.draw.line(screen, (0,0,0), (749.9,50),(749.9,450), 2)
a3=0
for i in range(0,8):
    pygame.draw.line(screen, (0,0,0), (770,a3*45+70+1*11.25),(770-6,a3*45+70+1*11.25), 2)
    pygame.draw.line(screen, (0,0,0), (770,a3*45+70+2*11.25),(770-10,a3*45+70+2*11.25), 2)
    pygame.draw.line(screen, (0,0,0), (770,a3*45+70+3*11.25),(770-6,a3*45+70+3*11.25), 2)
    a3=a3+1


a2=0
for i in range(0,6):
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+1*14.583,50),(50+a2*116.6+1*14.583,56), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+2*14.583,50),(50+a2*116.6+2*14.583,60), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+3*14.583,50),(50+a2*116.6+3*14.583,56), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+4*14.583,50),(50+a2*116.6+4*14.583,65), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+5*14.583,50),(50+a2*116.6+5*14.583,56), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+6*14.583,50),(50+a2*116.6+6*14.583,60), 2)
    pygame.draw.line(screen, (0,0,0), (50+a2*116.6+7*14.583,50),(50+a2*116.6+7*14.583,56), 2)
    a2=a2+1

a1=0
for i in range(0,6):
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+1*14.583,450),(50+a1*116.6+1*14.583,450-6), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+2*14.583,450),(50+a1*116.6+2*14.583,450-10), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+3*14.583,450),(50+a1*116.6+3*14.583,450-6), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+4*14.583,450),(50+a1*116.6+4*14.583,450-15), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+5*14.583,450),(50+a1*116.6+5*14.583,450-6), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+6*14.583,450),(50+a1*116.6+6*14.583,450-10), 2)
    pygame.draw.line(screen, (0,0,0), (50+a1*116.6+7*14.583,450),(50+a1*116.6+7*14.583,450-6), 2)
    a1=a1+1


font = pygame.font.Font(None,20)
text = font.render("1.00", True, (0,0,0))
screen.blit(text, (0,65))
font = pygame.font.Font(None,20)
text = font.render("0.75", True, (0,0,0))
screen.blit(text, (0,65+1*45))
font = pygame.font.Font(None,20)
text = font.render("0.50", True, (0,0,0))
screen.blit(text, (0,65+2*45))
font = pygame.font.Font(None,20)
text = font.render("0.25", True, (0,0,0))
screen.blit(text, (0,65+3*45))
font = pygame.font.Font(None,20)
text = font.render("0.00", True, (0,0,0))
screen.blit(text, (0,65+4*45))
font = pygame.font.Font(None,20)
text = font.render("-0.25", True, (0,0,0))
screen.blit(text, (0,65+5*45))
font = pygame.font.Font(None,20)
text = font.render("-0.50", True, (0,0,0))
screen.blit(text, (0,65+6*45))
font = pygame.font.Font(None,20)
text = font.render("-0.75", True, (0,0,0))
screen.blit(text, (0,65+7*45))
font = pygame.font.Font(None,20)
text = font.render("-1.00", True, (0,0,0))
screen.blit(text, (0,65+8*45))

font = pygame.font.Font(None,20)
text = font.render("-3п", True, (0,0,0))
screen.blit(text, (40,460))
font = pygame.font.Font(None,20)
text = font.render("-5п/2", True, (0,0,0))
screen.blit(text, (40+1*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("-2п", True, (0,0,0))
screen.blit(text, (40+2*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("-3п/2", True, (0,0,0))
screen.blit(text, (40+3*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("-п", True, (0,0,0))
screen.blit(text, (40+4*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("-п/2", True, (0,0,0))
screen.blit(text, (40+5*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("0", True, (0,0,0))
screen.blit(text, (40+6*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("п/2", True, (0,0,0))
screen.blit(text, (40+7*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("п", True, (0,0,0))
screen.blit(text, (40+8*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("3п/2", True, (0,0,0))
screen.blit(text, (40+9*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("5п/2", True, (0,0,0))
screen.blit(text, (40+10*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("2п", True, (0,0,0))
screen.blit(text, (40+11*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("5п/2", True, (0,0,0))
screen.blit(text, (40+12*58.3,460))
font = pygame.font.Font(None,20)
text = font.render("3п", True, (0,0,0))
screen.blit(text, (40+13*58.3,460))


font = pygame.font.Font(None,25)
text = font.render("sin x", True, (0,0,0))
screen.blit(text, (490,70))

pygame.draw.line(screen, (255,0,0), (540,78),(580,78), 3)

font = pygame.font.Font(None,25)
text = font.render("cos x", True, (0,0,0))
screen.blit(text, (490,95))
pygame.draw.line(screen, (0,0,255), (540,103),(547,103), 3)
pygame.draw.line(screen, (0,0,255), (550,103),(557,103), 3)
pygame.draw.line(screen, (0,0,255), (560,103),(567,103), 3)
pygame.draw.line(screen, (0,0,255), (570,103),(580,103), 3)


for x in range(700):
    y=int(math.sin(x/700 * n * math.pi)*A + 250)
    xy.append([x+50,y])
pygame.draw.lines(screen, [255,0,0], False, xy, 3)
pygame.display.flip()


for x in range(700):

    y=int(math.cos(x/700 * n * math.pi)*A + 250)
    xyy.append([x+50,y])
pygame.draw.lines(screen, [0,0,255], False, xyy, 3)
pygame.display.flip()

for x in range(700):
    y=int(math.cos(x/700 * n * math.pi)*A + 250)
    if (x%10==0):
        pygame.draw.circle(screen, [255,255,255], (x+50,y), 2)
        pygame.display.flip()



while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            r=False
