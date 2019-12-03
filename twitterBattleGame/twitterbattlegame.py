from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import threading
import sys
import pygame
import os


if len(sys.argv) == 3:
	search_strings = [sys.argv[1],sys.argv[2]]
else:
	print("Usage: twitterbattlegame.py [TREND1_STRING] [TREND2_STRING]")
	sys.exit(0)
	
	
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

access_token=""
access_token_secret=""

# This is the string to search in the twitter feed
# May be  a word, an #hashtag or a @username


twitterText = ""
text_x = 30
color = 1

dwarfGo = False
gladiatorGo = False
finish = False

# final animation
dwarfdirection = -1
dwarfmove = 0
gladiatordirection = -1
gladiatormove = 0

def startTwitter():
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=search_strings)
	

			
class StdOutListener(StreamListener):
		
	def on_data(self, data):
		global twitterText
		global first
		global text_x
		global color
		global dwarfGo
		global gladiatorGo
		data  = json.loads(data)
		twitterText = data['text'].lower()
		if search_strings[0] in twitterText:
			dwarfGo = True
		if search_strings[1] in twitterText:
			gladiatorGo = True
		return True

	def on_error(self, status):
		return False
		
def get_sprite(image, x, y, width, height):
	sprite = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
	sprite.blit(image, (0, 0), (x, y, width, height))
	return sprite
	
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
		
twitterThread = threading.Thread(target = startTwitter)
twitterThread.start()

pygame.init()

clock = pygame.time.Clock()
size = width, height = 1056, 672
screen = pygame.display.set_mode(size)

# fonts
font = pygame.font.Font('./assets/PressStart2P-Regular.ttf', 16)
fontTitles = pygame.font.Font('./assets/PressStart2P-Regular.ttf', 32)

# default text from twitter
text = font.render(twitterText.encode('utf-8'), True, (0,0,0)) 
textRect = text.get_rect()

# info texts
textTile = fontTitles.render("Twitter #hashtags battle!", True, (100,250,80))
textTileRect = textTile.get_rect()
textTileRect.center = (520,40)

hashtagText = fontTitles.render(sys.argv[1]+" VS "+sys.argv[2], True, (250,50,250))
hashtagTextRect = hashtagText.get_rect()
hashtagTextRect.center = (520,100)

  
# set background
background = pygame.image.load("./assets/bulkhead-wallsx3.png")
backgroundRect = background.get_rect()

# set dwarf sprites
dwarfSpritesSheet = pygame.image.load("./assets/Dwarf_Sprite_Sheet1.2v-4x.png")
dwarfSprites = []
dwarfSpritesNumber = 4
for i in range(dwarfSpritesNumber):
	dwarfSprites.append(get_sprite(dwarfSpritesSheet,150 * i,640,150,100))

dwarfRect = pygame.Rect(50,470,128,128)

dwarfSpritePos = 0

# set gladiator sprites

gladiatorSpritesSheet = pygame.image.load("./assets/Gladiator-Sprite Sheet-Left4x.png")
gladiatorSprites = []
gladiatorSpritesNumber = 5
for i in range(gladiatorSpritesNumber):
	gladiatorSprites.append(get_sprite(gladiatorSpritesSheet,128 * i,0,128,128))

gladiatorRect = pygame.Rect(874,430,128,128)

gladiatorSpritePos = 0


# set key

collectablesSpritesSheet = pygame.image.load("./assets/Dungeon Collectables4x.png")
keySprites = []
keySpritesNumber = 12
for i in range(keySpritesNumber):
	keySprites.append(get_sprite(collectablesSpritesSheet,64 * i,260,64,64))

keyRect = pygame.Rect(496,490,64,64)

keySpritePos = 0

# set box and money

box = pygame.image.load("./assets/box.png")
boxRect = box.get_rect()
boxRect.center = (523,510)

money = pygame.image.load("./assets/money.png")
moneyRect = money.get_rect()
moneyRect.center = (523,520)

while 1:
	clock.tick(24)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			os._exit(1)
		if event.type == pygame.KEYDOWN:
			# key control (for testing)
			if event.key == pygame.K_LEFT:
				dwarfRect = dwarfRect.move(-10,0)
				dwarfSpritePos -= 1
				if dwarfSpritePos < 0:
					dwarfSpritePos = dwarfSpritesNumber - 1
			if event.key == pygame.K_RIGHT:
				dwarfRect = dwarfRect.move(10,0)
				dwarfSpritePos += 1
				if dwarfSpritePos > dwarfSpritesNumber -1:
					dwarfSpritePos = 0
			if event.key == pygame.K_a:
				gladiatorRect = gladiatorRect.move(-10,0)
				gladiatorSpritePos -= 1
				if gladiatorSpritePos < 0:
					gladiatorSpritePos = gladiatorSpritesNumber - 1
			if event.key == pygame.K_s:
				gladiatorRect = gladiatorRect.move(10,0)
				gladiatorSpritePos += 1
				if gladiatorSpritePos > gladiatorSpritesNumber -1:
					gladiatorSpritePos = 0
	
	# draw background
	screen.blit(background, backgroundRect)
	
	# automated sprites movement
	if dwarfGo == True and finish == False:
		#print("ENTRAAAAA")
		dwarfGo = False
		dwarfRect = dwarfRect.move(10,0)
		dwarfSpritePos += 1
		if dwarfSpritePos > dwarfSpritesNumber -1:
			dwarfSpritePos = 0
		# render text
		text = font.render(str(twitterText.encode('utf-8'))[:60]+"...", True, (255,0,0)) 
		textRect = text.get_rect()
		textRect.x = 20
		textRect.y = dwarfRect.y - 200

	if gladiatorGo == True and finish == False:
		gladiatorGo = False
		gladiatorRect = gladiatorRect.move(-10,0)
		gladiatorSpritePos -= 1
		if gladiatorSpritePos < 0:
			gladiatorSpritePos = gladiatorSpritesNumber - 1
		# render text
		text = font.render(str(twitterText.encode('utf-8'))[:60]+"...", True, (0,0,255)) 
		textRect = text.get_rect()
		textRect.x = 20
		textRect.y = gladiatorRect.y - 100 
	
	# draw tweet
	if finish == False:
		screen.blit(text,textRect)
	
	# draw texts
	screen.blit(textTile,textTileRect)
	screen.blit(hashtagText,hashtagTextRect)
	
	
	# draw box
	screen.blit(box,boxRect)
	
	# game ending
	if dwarfRect.right > keyRect.left:
		# draw money and box
		finish = True
		screen.blit(money,moneyRect)
		dwarfRect = dwarfRect.move(0,dwarfdirection)
		if dwarfmove > 10:
			dwarfdirection = dwarfdirection * -1
			dwarfmove = 0
		dwarfmove += 1
		winText = fontTitles.render(sys.argv[1]+" WINS!!", True, (0,0,255)) 
		winTextRect = winText.get_rect()
		winTextRect.center = (520,200)
		screen.blit(winText,winTextRect)
		
	if gladiatorRect.left < keyRect.right:
		# draw money and box
		finish = True
		screen.blit(money,moneyRect)
		gladiatorRect = gladiatorRect.move(0,gladiatordirection)
		if gladiatormove > 10:
			gladiatordirection = gladiatordirection * -1
			gladiatormove = 0
		gladiatormove += 1
		winText = fontTitles.render(sys.argv[2]+" WINS!!", True, (0,0,255)) 
		winTextRect = winText.get_rect()
		winTextRect.center = (520,200)
		screen.blit(winText,winTextRect)
	
	
	# draw key
	if finish == False:
		screen.blit(keySprites[keySpritePos],keyRect)
		keySpritePos += 1
		if keySpritePos > keySpritesNumber -1:
			keySpritePos = 0
	
	# draw dwarf
	screen.blit(dwarfSprites[dwarfSpritePos],dwarfRect)
	
	# draw gladiator
	screen.blit(gladiatorSprites[gladiatorSpritePos],gladiatorRect)
	
	pygame.display.flip()


