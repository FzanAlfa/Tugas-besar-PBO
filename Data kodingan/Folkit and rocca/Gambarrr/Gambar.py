import pygame

#Ukuran Window
width = 1100
height = 836
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption ("Morphling")
#icon = pygame.image.load ('Codingan Morphling/Gambarrr/pterodactyl.png')
#pygame.display.set_icon(icon)

#Background How to Play
background_how_to = pygame.image.load('Codingan Morphling/Gambarrr/Background/howtoplay.jpg')
background_how_to = pygame.transform.scale(background_how_to,(950,836))

#Background Credits
background_credits = pygame.image.load('Codingan Morphling/Gambarrr/Background/credits_bg.png')
background_credits = pygame.transform.scale(background_credits,(950,836))

#Gambar Karakter
Gambar_rakun_Awal         =  pygame.image.load('Codingan Morphling/Gambarrr/rakun_idle.png')
Gambar_rakun_Nunduk       = [pygame.image.load(f'Codingan Morphling/Gambarrr/rakun/rakun Nunduk/Proses Nunduk{i+1}.png')         for i in range (0,10) ]
Gambar_rakun_Lari         = [pygame.image.load(f'Codingan Morphling/Gambarrr/rakun/rakun Lari/Run ({i+1}).png')                  for i in range (0,12) ]
Gambar_rakun_Melompat     = [pygame.image.load(f"Codingan Morphling/Gambarrr/rakun/rakun Lompat/Jump ({i+1}).png")               for i in range(0,12) ]


Gambar_rakun_Nunduk_evo   = [pygame.image.load(f'Codingan Morphling/Gambarrr/rakun/Evolusi/rakun Nunduk/Proses Nunduk{i+1}.png') for i in range (0,10) ]
Gambar_rakun_Lari_evo     = [pygame.image.load(f'Codingan Morphling/Gambarrr/rakun/Evolusi/rakun Lari/Run ({i+1}).png')          for i in range (0,12) ]
Gambar_rakun_Melompat_evo = [pygame.image.load(f'Codingan Morphling/Gambarrr/rakun/Evolusi/rakun Lompat/Jump ({i+1}).png')       for i in range (0,12)]

Gambar_rubah_Awal         =  pygame.image.load('Codingan Morphling/Gambarrr/rubah_idle.png')
Gambar_rubah_Nunduk       = [pygame.image.load(f'Codingan Morphling/Gambarrr/rubah/rubah nunduk/Proses Nunduk{i+1}.png')         for i in range (0,4) ]
Gambar_rubah_Lari         = [pygame.image.load(f'Codingan Morphling/Gambarrr/rubah/rubah lari/Run ({i+1}).png')                  for i in range (0,4) ]
Gambar_rubah_Melompat     = [pygame.image.load(f"Codingan Morphling/Gambarrr/rubah/rubah lompat/Jump ({i+1}).png")               for i in range(0,4) ]


#Gambar Obstacle
Batu  = pygame.image.load(f'Codingan Morphling/Gambarrr/Obstacle/Crystal.png')
Batu = pygame.transform.scale(Batu,(90,90))
pohon = pygame.image.load('Codingan Morphling/Gambarrr/Obstacle/kaktus1.png')
pohon = pygame.transform.scale(pohon, (90, 130))
bird = pygame.image.load(f'Codingan Morphling/Gambarrr/Obstacle/burung.png') 
bird = pygame.transform.scale(bird, (70, 70))
pohonbesar = pygame.image.load('Codingan Morphling/Gambarrr/Obstacle/pohon.png')
pohonbesar = pygame.transform.scale(pohonbesar, (140, 120))
powerup = pygame.image.load('Codingan Morphling/Gambarrr/Powerup/powerup.png')
powerup = pygame.transform.scale(powerup, (70, 70))

#Background Menu Game
background_menu = pygame.image.load('Codingan Morphling/Gambarrr/Background/menu_start1.png')
background_menu = pygame.transform.scale(background_menu,(950,836)) 

#Background memilih karakter   
background_select = pygame.image.load('Codingan Morphling/Gambarrr/Background/character_select.jpg')
background_select = pygame.transform.scale(background_select,(950,836))

#Background rakun
background = pygame.image.load('Codingan Morphling/Gambarrr/background.png')
background = pygame.transform.scale(background,(width,height))

