import pygame
from abc import ABC, abstractmethod
from Gambar import *

class Karakter (ABC):
    posisi_vertikal = 75
    posisi_horizontal = 75

    @abstractmethod
    def draw (self,screen):
        pass
    
    @abstractmethod
    def bergerak (self):
        pass

    @abstractmethod
    def update (self,user_input):
        pass

    
class Rakun (Karakter):
    def __init__(self):
        self.__berat_rakun = 11
        self.__koordinat_vertikal = 490 #semakin tinggi angkanya  semakin kebawah posisinya

        self.__image_awal  = Gambar_rakun_Awal
        self.__rakun_lari   = Gambar_rakun_Lari
        self.__rakun_lompat = Gambar_rakun_Melompat
        self.__rakun_nunduk = Gambar_rakun_Nunduk

        self.posisi_rect   = self.__image_awal.get_rect()
        self.posisi_rect.y = self.posisi_vertikal
        self.posisi_rect.x = self.posisi_horizontal
        self.batas_lompatan    = self.__berat_rakun

        self.__index  = 0
        self.__lompat = False 
        self.__nunduk = False
        self.__lari   = True
    
        if self.__index == 12:
            self.__index = 0

    def melompat (self):
        if self.__lompat is True:
            self.__image_awal = self.__rakun_lompat[self.__index % 12]
            self.posisi_rect.y -= self.batas_lompatan * 5.5
            self.batas_lompatan -= 1
            if self.batas_lompatan  <- self.__berat_rakun:
                self.__lompat =  False
                self.batas_lompatan =  self.__berat_rakun
                self.posisi_rect.y = self.__koordinat_vertikal
            self.__index += 1
            

    def menunduk (self):
        if self.__nunduk is True:
            self.batas_lompatan = 11
            self.__image_awal  = self.__rakun_nunduk[self.__index % 10]
            self.posisi_rect.y = self.__koordinat_vertikal + 40
            self.__index      += 1
    
    def bergerak(self):
        if self.__lari is True:
            self.posisi_rect.y = self.__koordinat_vertikal
            self.__image_awal = self.__rakun_lari[self.__index % 12]
            self.__index += 1
    
    def melompat_evo (self):
        if self.__lompat is True:
            self.__image_awal = self.__rakun_lompat_evo[self.__index % 12]
            self.posisi_rect.y -= self.batas_lompatan * 5
            self.batas_lompatan -= 1
            if self.posisi_rect.y >= 360:
                self.posisi_rect.y = 360
            if self.batas_lompatan < -self.__berat_rakun:
                self.__lompat = False
                self.batas_lompatan = self.__berat_rakun
                self.posisi_rect.y = self.__koordinat_vertikal
            self.__index += 1

    def menunduk_evo (self):
        if self.__nunduk is True:
            self.batas_lompatan = 11
            self.__image_awal  = self.__rakun_nunduk_evo[self.__index % 10]
            self.posisi_rect.y = self.__koordinat_vertikal + 50
            self.__index      += 1

    def bergerak_evo(self):
        if self.__lari is True:
            self.posisi_rect.y = self.__koordinat_vertikal
            self.__image_awal = self.__rakun_lari_evo[self.__index % 12]
            self.__index += 1

    def update (self, user_input, evo):
        if evo == False:
            self.__berat_rakun = 11
            self.__koordinat_vertikal =  490

            if self.__index >= 12:
                self.__index =0
    
            if self.__lompat   is True:
                self.melompat()
            elif self.__nunduk is True:
                self.menunduk()
            elif self.__lari   is True:
                self.bergerak()

        elif evo == True:
            self.__berat_rakun = 11
            self.__koordinat_vertikal = 400
            self.__rakun_lari_evo   = Gambar_rakun_Lari_evo
            self.__rakun_lompat_evo = Gambar_rakun_Melompat_evo
            self.__rakun_nunduk_evo = Gambar_rakun_Nunduk_evo

            if self.__index >= 12:
                self.__index =0
    
            if self.__lompat   is True:
                self.melompat_evo()
            elif self.__nunduk is True:
                self.menunduk_evo()
            elif self.__lari   is True:
                self.bergerak_evo()

        if (self.__lompat is False and user_input[pygame.K_UP] ) or (self.__lompat is False and user_input[pygame.K_SPACE]) :
                jump_sound = pygame.mixer.Sound('Folkit and rocca/Music/Jump.ogg') 
                jump_sound.play()
                self.__lompat = True
                self.__nunduk = False
                self.__lari = False
        elif (self.__nunduk is False and user_input[pygame.K_DOWN]):
            jump_sound = pygame.mixer.Sound('Folkit and rocca/Music/Jump.ogg') 
            jump_sound.play()
            self.__lompat = False
            self.__nunduk = True
            self.__lari = False
        elif not (self.__lompat or user_input[pygame.K_DOWN]):
                self.__nunduk = False
                self.__lari = True
                self.__lompat = False

    def draw (self,screen):
        screen.blit(self.__image_awal, self.posisi_rect)

class Rubah(Karakter):
    def __init__(self):
        self.__berat_rubah = 11
        self.__koordinat_vertikal = 490 #semakin tinggi     semakin kebawah posisinya

        self.__image_awal  = Gambar_rubah_Awal
        self.__rubah_lari   = Gambar_rubah_Lari
        self.__rubah_lompat = Gambar_rubah_Melompat
        self.__rubah_nunduk = Gambar_rubah_Nunduk

        self.posisi_rect   = self.__image_awal.get_rect()
        self.posisi_rect.x = self.posisi_vertikal
        self.posisi_rect.y = self.posisi_horizontal
        self.batas_lompatan    = self.__berat_rubah

        self.__index  = 0
        self.__lompat = False 
        self.__nunduk = False
        self.__lari   = True
    
        if self.__index == 12:
            self.__index = 0

    def melompat (self):
        if self.__lompat is True:
            self.__image_awal = self.__rubah_lompat[self.__index % 4]
            self.posisi_rect.y -= self.batas_lompatan * 5.5
            self.batas_lompatan -= 1
            if self.batas_lompatan  <- self.__berat_rubah:
                self.__lompat =  False
                self.batas_lompatan =  self.__berat_rubah
                self.posisi_rect.y = self.__koordinat_vertikal
            self.__index += 1
            
    def menunduk (self):
        if self.__nunduk is True:
            self.batas_lompatan = 11
            self.__image_awal       = self.__rubah_nunduk[self.__index % 4]
            self.posisi_rect.y = self.__koordinat_vertikal + 30
            self.__index      += 1
    
    def bergerak(self):
        if self.__lari is True:
            self.posisi_rect.y = self.__koordinat_vertikal
            self.__image_awal = self.__rubah_lari[self.__index % 4]
            self.__index += 1

    def update (self, user_input):
            self.__berat_rubah = 11
            self.__koordinat_vertikal =  490

            if self.__index >= 12:
                self.__index =0
    
            if self.__lompat   is True:
                self.melompat()
            elif self.__nunduk is True:
                self.menunduk()
            elif self.__lari   is True:
                self.bergerak()
        
            if (self.__lompat is False and user_input[pygame.K_UP] ) or (self.__lompat is False and user_input[pygame.K_SPACE]) :
                jump_sound = pygame.mixer.Sound('Folkit and rocca/Music/Jump.ogg') 
                jump_sound.play()
                self.__lompat = True
                self.__nunduk = False
                self.__lari = False
            elif (self.__nunduk is False and user_input[pygame.K_DOWN]):
                jump_sound = pygame.mixer.Sound('Folkit and rocca/Music/Jump.ogg') 
                jump_sound.play()
                self.__lompat = False
                self.__nunduk = True
                self.__lari = False
            elif not (self.__lompat or user_input[pygame.K_DOWN]):
                self.__nunduk = False
                self.__lari = True
                self.__lompat = False

    def draw (self,screen):
        screen.blit(self.__image_awal, self.posisi_rect)