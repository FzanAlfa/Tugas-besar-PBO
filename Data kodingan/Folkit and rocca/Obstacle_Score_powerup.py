import pygame
import random
from abc import ABC, abstractmethod
from Gambar  import *
from Tombol   import *
from Gambar import *
from Karakter import *

class Rintangan(ABC):
    
    def update(self):
        self.rect.x -= speed

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def buat_rintangan(self):
        pass

    @abstractmethod
    def ganti_rintangan ():
        pass

class Obstacle(Rintangan):
    def update(self):
        if evo == True: 
            self.rect.x -= speed
            if self.rect.x <- self.rect.width:
                obstacles.pop()
        else:
            self.rect.x -= speed
            if self.rect.x <-self.rect.width:
                obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def buat_rintangan (self):
        for rintangan in obstacles:
            global nyawa,evo,cd_mati
            rintangan.draw(screen)
            rintangan.update()
            if Karakter_1.posisi_rect.colliderect(rintangan.rect) and evo == False and nyawa <= 1 and cd_mati == False: #bagian yang menyatakan player akan mati
                dead_sound = pygame.mixer.Sound('Folkit and rocca/Music/Mati.ogg') 
                dead_sound.play()
                pygame.time.wait(1000)
                start(Score.hitung_score(self))
            elif Karakter_1.posisi_rect.colliderect(rintangan.rect) and evo == False and nyawa >= 1 and cd_mati == False: #bagian yang menyatakan player akan mati
                cd_mati = True
                nyawa -= 1
                dead_sound = pygame.mixer.Sound('Folkit and rocca/Music/Mati.ogg') 
                dead_sound.play()
            elif Karakter_1.posisi_rect.colliderect(rintangan.rect) and evo == True:
                destroy = pygame.mixer.Sound('Folkit and rocca/Music/Hancur.ogg') 
                destroy.play()

    @staticmethod
    def ganti_rintangan ():
        if obstacles == []:
            x = random.randint(0,3)
            if x == 0:
                obstacles.append(Pohon(pohon))
            elif x == 1:
                x = random.randint(0,1)
                obstacles.append(Batu_(Batu))
            elif x == 2:
                obstacles.append(Bird(bird))
            elif x == 3:
                obstacles.append(PohonBesar(pohonbesar))

class Pohon(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 500
class PohonBesar(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 530
class Batu_(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 540
class Bird(Obstacle):
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(380,450)

########################################################################################################

class Powerup : 
    def __init__(self):
        self.image = powerup
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 350

    def power (self): 
        self.draw(screen)
        self.update()
     
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.rect.x -= speed
########################################################################################################
class Score:
    def hitung_score(self):
        global poin, speed
        poin += 1
        if poin % 150 == 0:
            speed += 0.5

        text = font.render("Score: " + str(poin), True, (225, 225, 225))
        textRect = text.get_rect()
        textRect.x = 10
        textRect.y = 35
        screen.blit(text, textRect)
        return poin

    def high_score():
        high_score = 0
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        return high_score

    def save_high_score(new_high_score):
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()

########################################################################################################

def how_to_play():
    running = True
    while running: 
        pygame.display.set_mode((950,836))

        screen.blit(background_how_to,(0,0))

        if end_button.draw():
            start(0)
        pygame.display.update()

def credits():
    running = True
    while running: 
        pygame.display.set_mode((950,836))
        #screen.fill((255,255,255))
        screen.blit(background_credits,(0,0))

        if end_button.draw():
            start(0)

        pygame.display.update()

def pilih_karakter():
    running = True
    while running:
        #screen.fill((225,225,255))
        screen.blit(background_select,(0,0))
        if dino_game.draw():
            pygame.mixer.music.load('Folkit and rocca/Music/Background.ogg') 
            pygame.mixer.music.play(-1)
            game_rakun()
        if beruang_game.draw():
            pygame.mixer.music.load('Folkit and rocca/Music/Background.ogg') 
            pygame.mixer.music.play(-1)
            rubah()
        if end_button.draw():
            start(0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()



##############################################################################################
def game_rakun():
    pygame.display.set_mode((width,height))
    global poin, speed ,obstacles,Karakter_1,evo, nyawa, cd_mati, time_cd_mati
    evo = False
    Karakter_1 = Rakun()
    running = True 
    i = 0
    obstacles = []
    poin = 0
    speed = 15
    clock = pygame.time.Clock()
    score = Score()
    obstacle = Obstacle()
    power_up = Powerup()
    time_evolusi  = 200
    cd_mati = False
    time_cd_mati = 60
    nyawa = 3
    tampilkan_powerup = False
    
    while running: 
        screen.blit(background, (i,0))
        screen.blit(background, (width+i,0))
        if i <= -width:
            screen.blit(background, (width+i,0))
            i = 0
        i -= speed #agar jalannya terlhat maju

        #Menampilkan user dan mengatur gerakannya 
        Karakter_1.draw(screen)
        user_input = pygame.key.get_pressed()
        nyawa_text = font.render('nyawa: ' + str(nyawa), True, (255, 255, 255))
        nyawa_text_rect = nyawa_text.get_rect()
        nyawa_text_rect.x = 10
        nyawa_text_rect.y = 60
        screen.blit(nyawa_text, nyawa_text_rect)

        if poin % 500 == 0 or tampilkan_powerup == True  or user_input[pygame.K_f]:
            if evo == False:
                tampilkan_powerup = True
                power_up.power()
            if Karakter_1.posisi_rect.colliderect(power_up.rect):
                sound_powerup = pygame.mixer.Sound('Folkit and rocca/Music/item.ogg') 
                sound_powerup.play()
                tampilkan_powerup = False
                evo = True
                power_up.rect.x = width
        if evo == True:
            time_evolusi -= 1
            if time_evolusi <= 0:
                evo = False
                time_evolusi = 200
        if cd_mati == True:
            time_cd_mati -= 1
            if time_cd_mati <= 0:
                cd_mati = False
                time_cd_mati = 60
        Karakter_1.update(user_input,evo)
        Obstacle.ganti_rintangan()
        obstacle.buat_rintangan()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            
        clock.tick(25)
        score.hitung_score()
        pygame.display.update()

##############################################################################################
def rubah():
    pygame.display.set_mode((width,height))
    global poin, speed ,obstacles,Karakter_1,evo, cd_mati, nyawa, time_evolusi
    evo = False
    Karakter_1 = Rubah()
    running = True
    time_evolusi  = 0
    i = 0
    obstacles = []
    poin = 0
    speed = 15
    clock = pygame.time.Clock()
    score = Score()
    obstacle = Obstacle()
    power_up = Powerup()
    cd_mati = False
    time_cd_mati = 60
    nyawa = 3
    tampilkan_powerup = False
    
    while running: 
        #screen.fill((255,255,255))
        screen.blit(background, (i,0))
        screen.blit(background, (width+i,0))
        if i <= -width:
            screen.blit(background, (width+i,0))
            i = 0
        i -= speed

        #Menampilkan user dan mengatur gerakannya 
        Karakter_1.draw(screen)
        user_input = pygame.key.get_pressed()

        nyawa_text = font.render('nyawa: ' + str(nyawa), True, (255, 255, 255))
        nyawa_text_rect = nyawa_text.get_rect()
        nyawa_text_rect.x = 10
        nyawa_text_rect.y = 10
        screen.blit(nyawa_text, nyawa_text_rect)

        if poin % 500 == 0 or tampilkan_powerup == True  or user_input[pygame.K_f]:
            if evo == False:
                tampilkan_powerup = True
                power_up.power()
            if Karakter_1.posisi_rect.colliderect(power_up.rect):
                tampilkan_powerup = False
                evo = True
                sound_powerup = pygame.mixer.Sound('Folkit and rocca/Music/item.ogg') 
                sound_powerup.play()
                if nyawa < 3:
                    nyawa += 1
                evo = False
                power_up.rect.x = width
        if cd_mati == True:
            time_cd_mati -= 1
            if time_cd_mati <= 0:
                cd_mati = False
                time_cd_mati = 60
            
        Karakter_1.update(user_input)
        Obstacle.ganti_rintangan()
        obstacle.buat_rintangan()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        clock.tick(25)
        score.hitung_score()
        pygame.display.update()
 


def start (nilai):
    pygame.mixer.music.load('Folkit and rocca/Music/Menu.ogg') 
    pygame.mixer.music.play()
    if nilai == 0: 
        running = True
        while running: 
            pygame.display.set_mode((950,836))
            screen.blit(background_menu,(0,0))
            if start_button.draw():
                pilih_karakter()
            if button_how_to.draw():
                how_to_play()
            if button_credits.draw():
                credits()
            if end_button.draw():
                running = False
                pygame.quit()
                exit()
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (470, height // 2 - 50)
            screen.blit(high_score, high_scoreRect)
            if nilai > Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
    elif evo == True:
        pass
    elif cd_mati == True:
        pass
    else: 
        running = True
        while running: 
            pygame.display.set_mode((950,836))
            screen.blit(gameover,(0,0))
            if button_gameover.draw():
                pilih_karakter()
            if button_gameover_exit.draw():
                nilai(0)
               #running = True
               #pygame.quit()
               #exit()
            score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (470, 250+ 20)
            screen.blit(score, scoreRect)
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (470, 250 )
            screen.blit(high_score, high_scoreRect)
            if nilai >Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
           #for event in pygame.event.get():
           #    if event.type == pygame.QUIT:
           #        running = False
           #        pygame.quit()
           #        exit()
