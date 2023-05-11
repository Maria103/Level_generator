import pygame as pg
import time
from random import *
from sys import exit
from os import system

def get_level(new=False):
    if new:
        system('start level_generator_app.exe 15 30')
        disp.fill((0, 0, 0)) #очищаем экран от предыдущих рисунков
        font = pg.font.Font(None, 70)
        message = font.render('Загрузка...', True, (255, 0, 0))
        disp.blit(message, [0, 0])
        pg.display.update()
        time.sleep(3)
    f = open('..\\out\\new_level.txt', 'r')
    trash = f.readline().strip('\n')
    tmp = []
    for i in range(30):
        line = f.readline().strip('\n').split()
        tmp.append(list(map(int, line)))

    x = 1 * 40
    y = 15//2 * 40
    WALLS = []
    APPLES = []
    # for t in tmp: print(t)
    for i in range(15):
        for j in range(30):
            if tmp[i][j] == 1:
                WALLS.append([j * 40, i * 40])
            elif tmp[i][j] == 2:
                APPLES.append([j * 40, i * 40])
    # print('walls', WALLS)
    # print('apples', APPLES)
    shuffle(APPLES)
    # time.sleep(2)
    return x, y, APPLES[:5], WALLS

def game(new_level=True):

    x, y, APPLES, WALLS = get_level(new=new_level)
    
    #координаты первого яблока
    applex = APPLES[0][0]
    appley = APPLES[0][1]
    apples_cnt = len(APPLES)
    current_apple = 0

    apple = pg.image.load('..\images\\apple.png') #изображение яблока
    
    #необходимая функция, которая нужна нам для вывода текста на экран
    font = pg.font.Font(None, 40)
    
    #список, содержащий в себе список координат блоков змейки
    snake = [[x, y]]
    
    walls = []
    #загружаем изображения головы, смотрящей в разных направлениях
    snake_head_up = pg.image.load('..\images\headup.png')
    snake_head_down = pg.image.load('..\images\headdown.png')
    snake_head_right = pg.image.load('..\images\headright.png')
    snake_head_left = pg.image.load('..\images\headleft.png')
    
    snake_body = pg.image.load('..\images\snakebody.png') #изображение тела змеи
    
    # space = pg.image.load('..\images\space1.jpg') #изображение фона
    
    wall = pg.image.load('..\images\wall.png')

    direction = '' #изначальное направление змеи
    if [x+40, y] not in WALLS:
        direction = 'right'
    elif [x-40, y] not in WALLS:
        direction = 'left'
    elif [x, y-40] not in WALLS:
        direction = 'up'
    elif [x, y+40] not in WALLS:
        direction = 'down'
    #для отслеживания проигрыша
    game_over = False
    speed = 5
    clock = pg.time.Clock()
    while not game_over:
        #просмотр каждого дейтсвия, совершаемого пользователем в игре
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
                return
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_LEFT or event.key == pg.K_a) and direction != 'right':
                    direction = 'left'
                if (event.key == pg.K_RIGHT or event.key == pg.K_d) and direction != 'left':
                    direction = 'right'
                if (event.key == pg.K_UP or event.key == pg.K_w) and direction != 'down':
                    direction = 'up'
                if (event.key == pg.K_DOWN or event.key == pg.K_s) and direction != 'up':
                    direction = 'down'
        
        if direction == 'left':
            x -= 40
    
        if direction == 'right':
            x += 40
    
        if direction == 'up':
            y -= 40
    
        if direction == 'down' :
            y += 40
       
        #если вышел за границы - проиграл            
        if x >= 30*40 or x < 0 or y >= 15*40 or y < 0:
            game_over = True
            # print('я тууууут', x, y)
            message = font.render('Ты проиграл!', True, (255, 0, 0))
            disp.blit(message, [550, 250])
            pg.display.update()
            time.sleep(1)
            game(new_level=False)
            return
        
        #если голова змейки подвинулась - двигаем хвост змейки и остальное тело
        if snake[-1] != [x, y]:
            for i in range(0, len(snake)-1):
                snake[i] = snake[i+1]
            snake[-1] = [x, y]
        
        #если голова змейки на яблоке - увеличиваем змейку и меняем координаты яблока        
        if x == applex and y == appley:
            snake = [snake[0]] + snake
            # speed += 1
            while [applex, appley] in snake:
                current_apple += 1
                if current_apple == len(APPLES):
                    #выводим змейку для наглядности
                    for i in range(0, len(snake)):
                        #pg.draw.rect(disp, (0, 255, 0), [snake[i][0], snake[i][1], 40, 40])
                        disp.blit(snake_body, [snake[i][0], snake[i][1]]) #рисуем змею
                    
                    #рисуем голову
                    if direction == 'right':
                        disp.blit(snake_head_right, [snake[-1][0], snake[-1][1]])
                    if direction == 'left':
                        disp.blit(snake_head_left, [snake[-1][0], snake[-1][1]])
                    if direction == 'up':
                        disp.blit(snake_head_up, [snake[-1][0], snake[-1][1]]) 
                    if direction == 'down':
                        disp.blit(snake_head_down, [snake[-1][0], snake[-1][1]])
                    game_over = True
                    message = font.render('Уровень пройден!', True, (0, 255, 0))
                    disp.blit(message, [550, 250])
                    pg.display.update()
                    time.sleep(1)
                    game(new_level=True)
                    return
                applex = APPLES[current_apple][0]
                appley = APPLES[current_apple][1]
        
        #если голова змейки на стене - проиграл        
        if [x, y] in WALLS:
            game_over = True
            # print('вот он я', x, y)
            message = font.render('Ты проиграл!', True, (255, 0, 0))
            disp.blit(message, [550, 250])
            pg.display.update()
            time.sleep(1)
            game(new_level=False)
            return
        
        #если змейка врезалась в себя - проиграл
        if len(snake) > 2 and snake[-1] in snake[:-1]:
            game_over = True
            font = pg.font.Font(None, 40)
            message = font.render('Ты проиграл!', True, (255, 0, 0))
            disp.blit(message, [550, 250])
            pg.display.update()
            time.sleep(1)
            game(new_level=False)
            return
            
        #проверяем, что игра не закончилась, чтобы не делать лишних действий
        if not game_over:
            disp.fill((0, 0, 0)) #очищаем экран от предыдущих рисунков
            # disp.blit(space, [0, 0])

            #выводим змейку по блокам
            for i in range(0, len(snake)):
                #pg.draw.rect(disp, (0, 255, 0), [snake[i][0], snake[i][1], 40, 40])
                disp.blit(snake_body, [snake[i][0], snake[i][1]]) #рисуем змею
            
            #рисуем голову
            if direction == 'right':
                disp.blit(snake_head_right, [snake[-1][0], snake[-1][1]])
            if direction == 'left':
                disp.blit(snake_head_left, [snake[-1][0], snake[-1][1]])
            if direction == 'up':
                disp.blit(snake_head_up, [snake[-1][0], snake[-1][1]]) 
            if direction == 'down':
                disp.blit(snake_head_down, [snake[-1][0], snake[-1][1]])       
                
            #pg.draw.rect(disp, (255, 0, 0), [applex, appley, 40, 40]) #выводим яблоко
            
            #рисуем стены
            for w in WALLS:
                disp.blit(wall, w)
            disp.blit(apple, [applex, appley]) #рисуем яблоко
            
            message = font.render('Яблок собрано: ' + str(current_apple) + '/' + str(len(APPLES)), True, (255, 255, 255))
            disp.blit(message, [0, 0])
            pg.display.update() #показываем перерисованный экран
        
        clock.tick(speed) #FPS (количество кадров в секунду)

        
pg.init() #запускаем сам pygame 
disp = pg.display.set_mode((1200, 600)) #устанавливаем размеры игрового окна 
pg.display.set_caption('Змейка!') #название окна
game(new_level=True)  
pg.quit()
exit()