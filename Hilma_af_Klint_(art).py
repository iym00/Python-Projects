# Importing pygame module to access its functions and importing time to access time delay
import pygame,time
# Variable created to produce a window using display and set_mode with dimensions 300 X 300
screen = pygame.display.set_mode([300,300])
# RGBs of colors used (orangish-red, black, white, light-blue, yellow, and pink)
white = (210,207,200)
black = [28,28,28]
orangish_red_color = [173,54,34]
light_blue = [64,129,183]
yellow = [250,181,45]
pink = [217,135,124]
# Filling the window with the orangish-red color
screen.fill(orangish_red_color)
# Drawing tiny pink arc in the centre using arc function
pygame.draw.arc(screen,pink,[96,120,87,63],4.7,1.57,75)
# Drawing a yellow arc around the smaller pink arc
pygame.draw.arc(screen,yellow,[89,91.5,120,120],4.718,1.57,32)
# Drawing a black arc facing the pink arc
pygame.draw.arc(screen,black,[89,91.5,120,120],-4.718,-1.57,60)
# Drawing large circle which will contain smaller circles and arcs
pygame.draw.circle(screen,white,(150,150),80,25)
# Making half of the large white circle blue
pygame.draw.arc(screen,light_blue,[70,70.9,160,163],4.7,1.5699,27)
# Updating the window to display the image
pygame.display.update()
# Time delay to keep the image up long enough for observation
pygame.time.delay(5000)
