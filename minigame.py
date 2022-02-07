import pygame
# Initializing pygame
pygame.init()
# Colors used
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0) 
# Display
window = pygame.display.set_mode((400,400))
# Fill window with color and update
window.fill(white)
pygame.display.update()
# Create a 'Button' class to create a button later on. Create a new font for the button text
new_font = pygame.font.SysFont("dejavuserif",28)
class Button:
	def __init__(self,text_on_button):
		self.text_on_button = new_font.render(text_on_button,True,white)
		self.size = self.text_on_button.get_size()
		self.surface = pygame.Surface(self.size)
		self.surface.blit(self.text_on_button,(0,0)) 
				
# Variables to store circle y-position for later modification
circles_y_pos = 420 
# Creating 3 circles
pygame.draw.circle(window,red,(400//4,circles_y_pos),20)
pygame.draw.circle(window, blue,(400//4+400//4+400//4+5,circles_y_pos),20)
pygame.draw.circle(window, black,(400//4+400//4+5,circles_y_pos),20)
pygame.display.update()
while True:
	circles_y_pos -= 1
	window.fill(white)
	pygame.draw.circle(window,red,(400//4,circles_y_pos),20)
	pygame.draw.circle(window, blue,(400//4+400//4+400//4+5,circles_y_pos),20)
	pygame.draw.circle(window, black,(400//4+400//4+5,circles_y_pos),20)
	pygame.display.update()	
	pygame.time.delay(2)
	if circles_y_pos < -20:
		break	

# Make company text name appear on screen after the balls pass
font = pygame.font.SysFont("dejavuserif",35)
rendered_font = font.render("Ball Studios",True,black)
window.blit(rendered_font,(400//3-35,400//3-10))
pygame.display.update()
# Creating a face under the company text name
pygame.draw.circle(window,black,(400/2,400//3+140),40)
pygame.draw.circle(window,white,(400/2,400//3+140),35)
pygame.draw.circle(window,red,(400/2+15,400//3+130),10)
pygame.draw.circle(window,white,(400/2+15,400//3+130),5)
pygame.draw.circle(window,black,(400/2+15,400//3+130),2)
pygame.draw.circle(window,red,(400/2-15,400//3+130),10)
pygame.draw.circle(window,white,(400/2-15,400//3+130),5)
pygame.draw.circle(window,black,(400/2-15,400//3+130),2)
pygame.draw.line(window,black,(400/2-15,400//3+160),(400/2+15,400//3+160),2)
pygame.display.update()

# Loading the start window
window.fill(black)
pygame.time.delay(3000)
pygame.display.update()
new_rendered_text = font.render("Loading...",True,white)
window.blit(new_rendered_text,(400//3-8,400//3+10))
pygame.time.delay(3000)	
pygame.display.update()
pygame.time.delay(5000)
# Start screen
window.fill(white)
pygame.draw.rect(window,red,(0,400/2+60,400,200))
pygame.display.update()
# Creating game title screen
font_for_game_title = pygame.font.SysFont("dejavuserif",30)
game_title = font_for_game_title.render("Ball Rush (Beta Version)",True, black)
window.blit(game_title, (400//3-120,400//3-75))
pygame.display.update()
# Creating a 'Button' object
button = Button("START")
# Blitting button on window
window.blit(button.surface,(150,150))
pygame.display.update()
# Flag to exit while loop
Flag = True
while Flag:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			window.fill(white)
			pygame.draw.rect(window,red,(0,400/2+60,400,200))
			# storing the x and y pos of our black ball in two variables
			x = 20
			y = 400/2+40
			pygame.draw.circle(window,black,(x,y),20)
			pygame.draw.line(window,black,(370,160),(370,400/2+60),6)
			pygame.draw.polygon(window,black,[(330,160),(330,200),(370,200),(370,160)])
			pygame.draw.polygon(window,white,[(335,165),(335,195),(368,195),(368,165)])
			pygame.display.update()
			Flag = False
		
		if event.type == pygame.QUIT:
			pygame.quit()

# Creating a clock to slow down ball movement
clock = pygame.time.Clock()				
# Keep window open, with a postcondition loop with flag
window_flag = True
while window_flag:
	clock.tick(900)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	
	# Create list of keys for ball movement
	key_list = pygame.key.get_pressed()
	
	# Actions per key press	
	if key_list[pygame.K_LEFT]:
		x -= 1
		if x >= 22: 
			window.fill(white)
			pygame.draw.rect(window,red,(0,400/2+60,400,200))
			pygame.draw.circle(window,black,(x,y),20)
			pygame.draw.line(window,black,(370,160),(370,400/2+60),6)
			pygame.draw.polygon(window,black,[(330,160),(330,200),(370,200),(370,160)])
			pygame.draw.polygon(window,white,[(335,165),(335,195),(368,195),(368,165)])
			pygame.display.update()
		
		else:
			x += 1
		
		


	if key_list[pygame.K_RIGHT]:
		x += 1
		window.fill(white)
		pygame.draw.rect(window,red,(0,400/2+60,400,200))
		pygame.draw.circle(window,black,(x,y),20)
		pygame.draw.line(window,black,(370,160),(370,400/2+60),6)
		pygame.draw.polygon(window,black,[(330,160),(330,200),(370,200),(370,160)])
		pygame.draw.polygon(window,white,[(335,165),(335,195),(368,195),(368,165)])
		pygame.display.update()
		
		if x >= 349:
			text_to_be_rendered = font.render("You Win!",True,black)
			window.fill(white)
			window.blit(text_to_be_rendered, (400//3-15,400//3-10))
			pygame.display.update()
			pygame.time.delay(1000)
			window_flag = False
			
	
	if key_list[pygame.K_UP]:
		flag1 = True
		while flag1:
			clock.tick(900)
			y -= 1
			window.fill(white)
			pygame.draw.rect(window,red,(0,400/2+60,400,200))
			pygame.draw.circle(window,black,(x,y),20)
			pygame.draw.line(window,black,(370,160),(370,400/2+60),6)
			pygame.draw.polygon(window,black,[(330,160),(330,200),(370,200),(370,160)])
			pygame.draw.polygon(window,white,[(335,165),(335,195),(368,195),(368,165)])
			pygame.display.update()
			
			if y == 100:
				while True:
					clock.tick(900)
					y += 1
					window.fill(white)
					pygame.draw.rect(window,red,(0,400/2+60,400,200))
					pygame.draw.circle(window,black,(x,y),20)
					pygame.draw.line(window,black,(370,160),(370,400/2+60),6)
					pygame.draw.polygon(window,black,[(330,160),(330,200),(370,200),(370,160)])
					pygame.draw.polygon(window,white,[(335,165),(335,195),(368,195),(368,165)])
					pygame.display.update()
					if y == 400/2+40:
						flag1 = False
						break
	
		
		
