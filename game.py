import pygame
import time
import random
pygame.font.init()

# screen
WIDTH , HEIGHT = 1000 , 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
# backgroud
BG = pygame.transform.scale(pygame.image.load("tapeta.png"),(WIDTH,HEIGHT))
# player
# player_width = 100
# player_height = 100
# player = pygame.transform.scale(pygame.image.load("loup.png"),(player_width,player_height))
PLAYER_VEL = 3
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans",50)

# draw func
def draw_screen(player, elapsed_time,stars):
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f"Time:{round(elapsed_time)}s",1, "white")
    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN,"red",player)
    for star in stars:
        pygame.draw.rect(WIN ,"white",star)
    pygame.display.update()

def main():
    run = True
    # speed of the loop from imported "time"
    clock = pygame.time.Clock()
    # player obj
    player = pygame.Rect(475,700,30,30)
    # start time 
    start_time = time.time()
    elapsed_time = 0
    # game loop
    # enemy "star"
    star_add_increment = 2000
    star_count = 0 
    stars = []
    hit = False
    while run:
        
        # clock init = speed of the game
        star_count += clock.tick(60)
        # game clock
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0 ,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH,STAR_HEIGHT)
            stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        # game loop
        for event in pygame.event.get():
            # game quits script
            if event.type == pygame.QUIT:
                run = False
                break
        # keys 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 3 :
            player.x -= 10
        if keys[pygame.K_RIGHT]and player.x - PLAYER_VEL <= 960 :
            player.x += 10
        # if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 3:
        #     player.y -= 10
        # if keys[pygame.K_DOWN] and player.y - PLAYER_VEL <= 760:
        #     player.y += 10
        # star movement
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        # screen drawing with drawing of other elements
        if hit:
            lost_msg = FONT.render("You lost" , 1, "white")
            WIN.blit(lost_msg,(WIDTH/2 - lost_msg.get_width()/2, HEIGHT/2 - lost_msg.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw_screen(player, elapsed_time,stars)

   
    pygame.quit()

if __name__ == "__main__":
    main()