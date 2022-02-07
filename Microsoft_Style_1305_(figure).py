# Importing pygame module to access its functions and importing time to access time delay
import pygame,time
# Variable created to produce a window using display and set_mode with dimensions 300 X 300
screen = pygame.display.set_mode([300,300])
# RGBs of colors used (black...)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
# Filling screen with white color
screen.fill(white)
# Creating head of figure
pygame.draw.circle(screen,black,[145,120],25,50)
# Creating nose of the figure
pygame.draw.polygon(screen,black,[(120,120),(100,120),(100,115),(120,115)])
# Creating arc to start the creation of the body 
pygame.draw.arc(screen,black,[126,145,40,40],0.05,3.1415,30)
# Creating the actual body extending from arc
pygame.draw.polygon(screen,black,[(126,160),(126,220),(165,220),(165,165)])
# Creating the figure's eye
pygame.draw.circle(screen,white,[139,113],4.99)
# Creating the figure's mouth
pygame.draw.arc(screen,white,[114,129,26,11],4.718,0,2)
# Creating the legs of the figure
pygame.draw.arc(screen,black,[160,213,20,70],-1,-4.1,5)
pygame.draw.arc(screen,black,[113,213,20,70],1,4.1,5)
# Creating the arms of the figure
pygame.draw.arc(screen,black,[115,160,20,120],1,3.0,5)
pygame.draw.arc(screen,black,[159,160,20,40],-1,3.0,5)
# Creating the hands of the figure
pygame.draw.circle(screen,black,[115,200],8)
pygame.draw.circle(screen,black,[175,200],8)
# Creating the feet of the figure
pygame.draw.arc(screen,black,[134,273,70,20],1,1.56,5)
pygame.draw.arc(screen,black,[67,270,75,34],1,1.571,5)
# Hat of the figure
pygame.draw.rect(screen,red,[134,25,23,70])
pygame.draw.rect(screen,red,[110,75,70,23])
# Updating the window to display the image
pygame.display.update()
# Time delay to keep the image up long enough for observation
pygame.time.delay(5000)


