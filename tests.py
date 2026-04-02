import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_a:
        #        print("a")
        #    if event.key == pygame.K_w:
        #        print("w")
        #    if event.key == pygame.K_s:
        #        print("s")
        #    if event.key == pygame.K_d:
        #        print("d")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        print("a")
    if keys[pygame.K_d]:
        print("d")
    if keys[pygame.K_w]:
        print("w")
    if keys[pygame.K_s]:
        print("s")

    screen.fill((0, 0, 0))
    pygame.display.flip()