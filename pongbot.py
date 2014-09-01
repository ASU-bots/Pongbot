"""
Module for botting pong.

"""

import time
import autopy as ap

def get_tl_br():
	"""Instructs the user to place their mouse in the top left and bottom right corners of the game screen, 
	then uses the mouse position to determine the boudaries.
	
	Returns:
		corners(list): a list of two (x,y) tuples
	"""
	corners=[]
	try:
		input('move mouse to top left corner, then press enter.')
	except SyntaxError, NameError:
		pass
	corners.append(ap.mouse.get_pos())
	try:
		input('move mouse to bottom right corner, then press enter.')
	except SyntaxError, NameError:
		pass
	corners.append(ap.mouse.get_pos())
	return corners

def get_left_paddle(pad_bmp, scr):
	"""
	Searches for the bitmap of the paddle on the screen.
	
	Returns:
		p((int,int)): tuple for the position of the found bitmap
	"""
	paddles=scr.find_every_bitmap(pad_bmp,0)

	l=10000
	p=None
	for paddle in paddles:
		if paddle[0]<l:
			l=paddle[0]
			p=paddle

	return p

def get_ball(ball_bmp, scr):
	"""
	Searches for the bitmap of the ball on the screen.
	
	Returns:
		p((int,int)): tuple for the position of the found bitmap
	"""
	ball=scr.find_bitmap(ball_bmp,0)
	return ball

if __name__== '__main__':
	c=get_tl_br()
	paddle=ap.bitmap.Bitmap.open("images/pallet.bmp")
	ball=ap.bitmap.Bitmap.open("images/ball.bmp")
	while True:
		scr= ap.bitmap.capture_screen(((c[0][0],c[0][1]),(c[1][0],c[1][1])))
		b=get_ball(ball,scr)
		p=get_left_paddle(paddle,scr)
		#if ball and paddle were found, move to match vertical positions
		try:
			if b[1]>(p[1]+16):
				ap.key.toggle('d',True)
				ap.key.toggle('e',False)
			else:
				ap.key.toggle('d',False)
				ap.key.toggle('e',True)
		except TypeError:
			pass
