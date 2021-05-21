'''
퀴즈) 똥피하기
[게임조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. fps는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70  * 70 - enemy.png
'''



import pygame
#######################################################################
# 기본 초기화 ( 반드시 해야하는것들 )

pygame.init() #초기화 (반드시필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #가로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("DDong_YN") #게임이름

#FPS
clock = pygame.time.Clock()
#######################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 캐릭터, 좌표, 폰트 , 속도  등 )

background = pygame.image.load("C:/Users/Administrator/Desktop/python workspace/pygame_basic/background.png")
character = pygame.image.load("C:/Users/Administrator/Desktop/python workspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
cahracter_height = character_size[1]
character_x_pos = (screen_width-character_width)/2
character_y_pos = screen_height-cahracter_height

to_x=0
to_y=0

character_speed = 0.6

enemy = pygame.image.load("C:/Users/Administrator/Desktop/python workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1]#캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) -(enemy_width/2) 
enemy_y_pos = screen_height 
enemy_y_pos = (screen_height  - enemy_height)/2


running = True 
while running :
    dt = clock.tick(30) 

    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False     
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            to_x=0
    
    character_x_pos += to_x*dt
    
    #가로 경계값 처리하기

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update()


pygame.quit()
