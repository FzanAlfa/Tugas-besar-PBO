import pygame

from Gambar import *

class Button: 
    def __init__(self, x , y ,image , scale):
        self.__width = image.get_width()
        self.__height = image.get_height()
        self.__x = x
        self.__y = y
        self.__x_s = x
        self.__y_s = y
        self.image = pygame.transform.scale(image, (int(self.__width * scale) , int(self.__height * scale)))
        self.rect = self.image.get_rect(center=(self.__x, self.__y))
        self.clicked = False
        self.__count=0

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.__count<3:
                self.__x+=1
                self.__y+=1
                self.rect = self.image.get_rect(center=(self.__x, self.__y))
                self.__count+=1
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.__x = self.__x_s
            self.__y = self.__y_s
            self.rect = self.image.get_rect(center=(self.__x_s, self.__y_s))
            self.__count = 0

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x , self.rect.y))
        return action


#PILIHAN KARAKTER
#Gambar Dino di pilihan karakter
game_dino = pygame.image.load('Codingan Morphling/Gambarrr/rakun_idle.png')
#game_dino = pygame.transform.scale(game_dino,(150,150))
dino_game = Button(715,560,game_dino,1.15)

#Gambar beruang di pilihan karakter
game_beruang = pygame.image.load('Codingan Morphling/Gambarrr/rubah_idle.png')
beruang_game = Button(200,560,game_beruang,1.5)

#Tombol Start
button_start = pygame.image.load('Codingan Morphling/Gambarrr/tombol/button_start.png')
start_button = Button(480,450,button_start,0.8)

#Tombol How to play
how_to = pygame.image.load('Codingan Morphling/Gambarrr/tombol/howtoplay_button.png')
button_how_to = Button(480,530,how_to,0.15)

#Tombol Credits
credits = pygame.image.load('Codingan Morphling/Gambarrr/tombol/CREDITS.png')
button_credits = Button(480,610,credits,0.18)

#Tombol Exit
button_end = pygame.image.load('Codingan Morphling/Gambarrr/tombol/exitt.png')
end_button = Button(480,690,button_end,0.8)

#PILIHAN KETIKA GAME OVER
#Tombol Play Again
gameover_button = pygame.image.load('Codingan Morphling/Gambarrr/tombol/PlayAgain.png')
button_gameover = Button(480,600,gameover_button,0.18)

#Tombol Exit
gameover_button_exit = pygame.image.load('Codingan Morphling/Gambarrr/tombol/button_exit.png')
button_gameover_exit = Button(480,680,gameover_button_exit,0.18)

#Gambar Dino mati
gameover = pygame.image.load('Codingan Morphling/Gambarrr/Background/gameover.png')
gameover = pygame.transform.scale(gameover,(950,836))




