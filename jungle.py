import pygame
import sys
import os

pygame.init()

# Configurações da tela
largura_tela = 300
altura_tela = 300
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Personagem Andando")

# Cores
branco = (255, 255, 255)

# Personagem
personagem_largura = 50
personagem_altura = 50
personagem_x = largura_tela // 2 - personagem_largura // 2
personagem_y = altura_tela - personagem_altura - 10
personagem_velocidade = 5

# Carregando imagens da animação
caminho_imagens = os.path.join(os.path.dirname(__file__), 'sprite_extra')
imagens_andando_esquerda = [pygame.image.load(os.path.join(caminho_imagens, 'walk_0.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_1.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_2.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_3.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_4.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_5.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_6.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_7.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_8.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_9.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'walk_10.png'))]

imagens_andando_direita = [pygame.transform.flip(img, True, False) for img in imagens_andando_esquerda]

# Carregando imagens da animação de fogo
imagens_fogo = [pygame.image.load(os.path.join(caminho_imagens, f'fogo_{i}.png')) for i in range(14)]

# Carregando imagens da animação de morte
imagens_morte = [pygame.image.load(os.path.join(caminho_imagens, f'die_{i}.png')) for i in range(16)]

# Imagem inicial
indice_animacao = 0
personagem_direcao = 'direita'
personagem_img = imagens_andando_direita[indice_animacao]

# Loop principal
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Verifica se o botão esquerdo do mouse foi pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # Inicia a animação de fogo
            for i in range(len(imagens_fogo)):
                personagem_img = imagens_fogo[i]
                tela.fill(branco)
                tela.blit(personagem_img, (personagem_x, personagem_y))
                pygame.display.flip()
                pygame.time.delay(50)  # Atraso entre os frames para uma animação mais visível


        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:
            # Inicia a animação de fogo
            for i in range(len(imagens_morte)):
                personagem_img = imagens_morte[i]
                tela.fill(branco)
                tela.blit(personagem_img, (personagem_x, personagem_y))
                pygame.display.flip()
                pygame.time.delay(50)  # Atraso entre os frames para uma animação mais visível


    # Captura das teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimento para a esquerda
    if teclas[pygame.K_LEFT] and personagem_x > 0:
        personagem_x -= personagem_velocidade
        personagem_direcao = 'esquerda'
        indice_animacao = (indice_animacao + 1) % len(imagens_andando_esquerda)
        personagem_img = imagens_andando_esquerda[indice_animacao]

    # Movimento para a direita
    if teclas[pygame.K_RIGHT] and personagem_x < largura_tela - personagem_largura:
        personagem_x += personagem_velocidade
        personagem_direcao = 'direita'
        indice_animacao = (indice_animacao + 1) % len(imagens_andando_direita)
        personagem_img = imagens_andando_direita[indice_animacao]

    # Atualização da tela
    tela.fill(branco)
    tela.blit(personagem_img, (personagem_x, personagem_y))
    pygame.display.flip()

    # Controle de taxa de atualização
    clock.tick(30)
