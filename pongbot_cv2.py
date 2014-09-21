from pbl import screen_grab
from multiprocessing import Process

import cv2
import numpy as np
#from matplotlib import pyplot as plt

import autopy as ap

def find_paddle(frame_gray, fname, ball_pos):
	template_paddle=cv2.imread('bmp/paddle0.bmp',0)
        wp,hp= template_paddle.shape[::-1]

	rpaddle = cv2.matchTemplate(frame_gray, template_paddle, cv2.TM_SQDIFF_NORMED)
        threshold = 0.8
        loc = np.where(rpaddle >= threshold)
        lloc=np.asarray(loc)
        leftmost=lloc.max(axis=0)

        paddle_pos= (leftmost[0] + wp/2, leftmost[1] + hp/2)

        if paddle_pos[1]>ball_pos[1]:
                ap.key.toggle('m', True)
                ap.key.toggle('k', False)
        elif paddle_pos[1]<ball_pos[1]:
                ap.key.toggle('m', False)
                ap.key.toggle('k',True)


def pong_play(frame):
	frame_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	template_ball=cv2.imread('bmp/ball0.bmp',0)
	w,h= template_ball.shape[::-1]

	rball = cv2.matchTemplate(frame_gray,template_ball,cv2.TM_SQDIFF_NORMED)
	min_val_ball, max_val_ball, min_loc_ball, max_loc_ball = cv2.minMaxLoc(rball)
	top_left_ball=min_loc_ball #for tm_sqdiffs
	#bottom_right_ball=(top_left_ball[0] + w, top_left_ball[1] + h)

	ball_pos= (top_left_ball[0] + w/2, top_left_ball[1] + h/2)
	
	try:
		find_paddle(frame_gray, "bmp/paddle0.bmp", ball_pos)
	except IndexError:
		try:
			find_paddle(frame_gray, "bmp/paddle1.bmp", ball_pos)
		except IndexError:
			try:
				find_paddle(frame_gray, "bmp/paddle2.bmp", ball_pos)
			except IndexError:
				pass
		

if __name__=="__main__":
	sg=screen_grab()
	sg.get_screen_area(pong_play,10)
