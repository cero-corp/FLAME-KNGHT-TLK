import pygame 
import time

pygame.init()
pygame.display.set_caption("THE LOST KINGDOMS")
screen = pygame.display.set_mode((800,600))
background = pygame.image.load('game/image/camp_sprite.png').convert()
def get_image(sheet,frame_w,frame_h,width,height,scale) :
    background = pygame.Surface((width,height)).convert()
    background.blit(sheet,(0,0),((frame_w*width),(frame_h*height),width,height))
    background = pygame.transform.scale(background,(width*scale,height*scale))
    return background

ips_list= []
last_udp= pygame.time.get_ticks()
anim_cld = 60
ips=0
for y in range (12):
    ips_list.append(get_image(background,0,y,800,400,1))
    for x in range (5):
        ips_list.append(get_image(background,x,y,800,400,1))

#ips = get_image(background,0,0,800,400,1)

run = True
while run :
    
    current_time = pygame.time.get_ticks()
    if current_time-last_udp >= anim_cld :
        ips+=1
        last_udp = current_time
    if ips>=anim_cld:
        ips = 0
    
    #appliquer l'arrière plan
    screen.blit(ips_list[ips],(0,200))#blit : injecter une image à un endroit de la fenêtre
    #actualiser l'écran
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
print("Fenêtre fermée")
        
        