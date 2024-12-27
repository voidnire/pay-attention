import pygame
from pyvidplayer import Video
import threading
import time


pygame.init()
win = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
           
vid = Video("lestatlestat.mp4")

def show_video():
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vid.close()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    #your program frame rate does not affect video playback
    clock.tick(60)
    
    if key == "r":
        vid.restart()           #rewind video to beginning
    elif key == "p":
        vid.toggle_pause()      #pause/plays video
    elif key == "right":
        vid.seek(15)            #skip 15 seconds in video
    elif key == "left":
        vid.seek(-15)           #rewind 15 seconds in video
    elif key == "up":
        vid.set_volume(1.0)     #max volume
    elif key == "down":
        vid.set_volume(0.0)     #min volume
        
    #draws the video to the given surface, at the given position
    vid.draw(win, (0, 0), force_draw=False)
    
    pygame.display.update()


def periodically(interval, func):
    """Executa a função `funcao` a cada `intervalo` segundos."""
    def agendar():
        while True:
            inicio = time.time()
            func()
            fim = time.time()
            duracao = fim - inicio
            time.sleep(max(0, interval - duracao))  # Garante que o intervalo seja respeitado

    thread = threading.Thread(target=agendar, daemon=True)
    thread.start()


while True:

    show_video()
    
