import pygame
pygame.init()
import random
import json
import time

win = pygame.display.set_mode((750, 700))
pygame.display.set_caption("Crash")
pygame.display.set_icon(pygame.image.load('b_e/ims/icon.png'))
condition4 = True
condition3 = True
condition2 = True
condition = True

def load_data():

    with open('b_e/data/data.json', "r") as f:
        data = json.load(f)

    return data

def death_screen(score):

    data = load_data()

    win = pygame.display.set_mode((750, 700))

    global condition2
    global condition
    global condition3

    highest_score = str(data['highest'])

    up = 353
    down = 450

    while condition3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condition3 = False
                condition2 = False
                condition = False

        keys = pygame.key.get_pressed()

        win.blit(pygame.image.load('b_e/ims/bg2.png'), (0, 0))

        color = (0, 0, 0)

        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 45)
        win.blit(font.render('You lose!', False, color), (265, 230))
        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 100)
        win.blit(font.render('Oh no...', False, color), (240, 160))
        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 75)
        win.blit(font.render('Try Again', False, color), (220, 350))
        win.blit(font.render('Back Home', False, color), (220, 450))
        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 30)
        win.blit(font.render('Your score was: {}'.format(str(score)), False, color), (20, 670))
        
        mouse_pos = pygame.mouse.get_pos()

        if (mouse_pos[0] > 220 and mouse_pos[0] < 220 + 6 * 50) and (mouse_pos[1] > 350 and mouse_pos[1] < 400):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                start()
        elif (mouse_pos[0] > 220 and mouse_pos[0] < 220 + 6 * 50) and (mouse_pos[1] > 450 and mouse_pos[1] < 500):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound('b_e/audio/off.wav').play()
                start_screen()
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

def start():

    global condition
    global condition2
    global condition3

    data = load_data()

    right = 350
    left = 280
    x2 = random.choice([right, left])

    x = random.choice([right, left])
    y = -25
    
    count = 0

    class cars:
        car1 = pygame.image.load('b_e/ims/car1.png')
        car2 = pygame.image.load('b_e/ims/car2.png')
        car3 = pygame.image.load('b_e/ims/car3.png')

    car1 = cars.car1
    car2 = cars.car2
    car3 = cars.car3

    car_list = [car1, car2, car3]

    car = random.choice(car_list)
    
    score_y = 49
    score_x = 332
    py = 600


    options_y = -3
    options_y2 = -28
    options_y3 = 0

    handle_y = 0

    scoreboard_y = -40

    background_y = -700

    ef = pygame.mixer.Sound('b_e/audio/start.wav')
    ef.play()
    
    pause = False
    button = False

    by = -37
    sy = 50

    while condition:

        def save():
            if data['highest'] < int(count):
                data['highest'] = count
            
                with open('b_e/data/data.json', "w") as f:
                    json.dump(data, f)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save()

                condition = False
                condition2 = False
                condition3 = False
        
        if button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if py > 470:
            py -= 10

        if score_y < 114:
            if not pause:
                score_y += 1
        if scoreboard_y < 25:
            if not pause:
                scoreboard_y += 1
    
        if options_y <= 25:
            if not pause:
                options_y += 1
        if options_y2 <= 0:
            if not pause:
                options_y2 += 1
        if options_y3 <= 28:
            if not pause:
                options_y3 += 1
        
        crash = pygame.mixer.Sound(random.choice(['b_e/audio/crash2.wav', 'b_e/audio/crash3.wav', 'b_e/audio/crash4.wav']))
        loss = pygame.mixer.Sound('b_e/audio/loss.wav')

        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 50)

        score = font.render(str(count), True, (0, 0, 0))

        if count > 250:
            speed = 10
        elif count >= 200:
            speed = 10
        elif count >= 150:
            speed = 10
        elif count >= 100:
            speed = 10
        elif count >= 80:
            speed = 9
        elif count >= 60:
            speed = 8
        elif count >= 40:
            speed = 7
        elif count >= 20:
            speed = 6
        elif count >= 10:
            speed = 5
        else:
            speed = 4
            
        timer = pygame.time.get_ticks()

        timer = timer // 1000

        road = pygame.image.load('b_e/ims/road1-min.png')

        win.blit(road, (0, background_y))
        if not pause:
            background_y += speed-speed/2

        if background_y >= 2:
            background_y -= random.randint(700, 800)

        scoreboard = pygame.image.load("b_e/ims/scoreboard.png").convert_alpha()
        scoreboard = pygame.transform.scale(scoreboard, (300, 200))
        
        pygame.draw.rect(win, (0, 0, 0), (624, 0, 7, 85))

        if not pause:
            tspeed = speed * 10 + random.randrange(11)
        else:
            tspeed = speed * 10 + 3

        if len(str(tspeed))>=3:
            sc = pygame.transform.scale(scoreboard, (214, 190))
        else:
            sc = pygame.transform.scale(scoreboard, (200, 190))
        
        if by < 28:
            if not pause:
                by += 1
        if sy <= 114:
            if not pause:
                sy += 1
        
        win.blit(sc, (534, by))

        spd = pygame.font.Font('b_e/fonts/pixeboy.ttf', 50)
        spd = spd.render(str(tspeed) + "KM/H", True, (0, 0, 0))
        win.blit(spd, (564, sy))

        lenght = len(str(count))

        if lenght > 1:
            if lenght == 2 and score_x != 325:
                score_x -= 7

            elif lenght == 3 and score_x != 318:
                score_x -= 7

            elif lenght == 4 and score_x != 315:
                score_x -= 7

            elif lenght == 5 and score_x != 310:
                score_x -= 7

            elif lenght == 6 and score_x != 305:
                score_x -= 7

            elif lenght == 7 and score_x != 300:
                score_x -= 7

            elif lenght == 8 and score_x != 295:
                score_x -= 7

        if speed == 4:
            num = 59

        elif speed == 5:
            num = 60

        elif speed == 6:
            num = 57
        
        elif speed == 7:
            num = 54

        elif speed == 8:
            num = 55
        
        elif speed == 9:
            num = 54

        elif speed == 10:
            num = 55

        if y == py - (num + speed):
            is_True = True
        else:
            is_True = False

        if x == right:
            is_right = True
            is_left = False
        if x == left:
            is_left = True
            is_right = False

        if x2 == right:
            is_right2 = True
            is_left2 = False
        if x2 == left:
            is_left2 = True
            is_right2 = False

        win.blit(pygame.image.load('b_e/ims/player.png'), (x, py))

        keys = pygame.key.get_pressed()

        movements = list()

        for i in range(700):
            if i > 406:
                if i < 534:
                    movements.append(i)
        if not pause:
            if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                x = left
                if (y in movements):
                    if is_right:
                        if x2 == left:
                            count += 1
                            crash.play()
                            y += 5000
                    
            if (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
                x = right
                if (y in movements):
                    if is_left:
                        if x2 == right:
                            count += 1
                            crash.play()
                            y += 5000

        if not pause:
            y += speed
            win.blit(pygame.image.load(random.choice(['b_e/ims/fire.png', 'b_e/ims/fire2.png', 'b_e/ims/fire3.png'])), (x + 24, py + 63))
    
        if ((((is_right and is_right2) or (is_left and is_left2)) and is_True)):
            count += 1
            crash.play()
            y += 5000

        win.blit(car, (x2, y))

        if y > 700:
            if y > 1000:
                car = random.choice(car_list)
                x2 = random.choice([right, left])
                y = -25
            else:
                save()
                loss.play()
                death_screen(score = count)
                condition = False
                condition2 = False
                scoreboard_y = -500
                score_y = -500
                options_y = -500
                options_y2 = -500
                options_y3 = -500
                handle_y = -500
        
        pygame.draw.rect(win, (0, 0, 0), (53, options_y2, 5, 25))
        pygame.draw.rect(win, (217, 214, 162), (33, options_y3, 46, 44))
        options = pygame.image.load('b_e/ims/options.png')
        options = pygame.transform.scale(options, (50, 50))
        win.blit(options, (30, options_y))
        
        mouse_pos = pygame.mouse.get_pos()
        
        movs_x = list()
        movs_y = list()

        for i in range(85):
            if i > 30:
                movs_x.append(i)

        for i in range(75):
            if i > 25:
                movs_y.append(i)
                
        if mouse_pos[0] in movs_x and mouse_pos[1] in movs_y:
            button = True
            if pygame.mouse.get_pressed()[0]:
                if pause:
                    pause = False
                elif not pause:
                    pause = True
                time.sleep(0.2)
        else:
            button = False

        pygame.draw.rect(win, (0, 0, 0), (260, handle_y, 10, 100))
        pygame.draw.rect(win, (0, 0, 0), (420, handle_y, 10, 100))

        win.blit(scoreboard, (200, scoreboard_y))
        win.blit(score, (score_x + 3, score_y))

        if pause:
            
            pygame.draw.rect(win, (0, 0, 0), (0, 330, 750, 20))

            pygame.draw.rect(win, (217, 214, 164), (50, 190, 650, 310), border_radius=30)

            font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 100)
            win.blit(font.render('Game Paused', True, (0, 0, 0)), (125, 210))

            start_x = 250
            start_y = 310
            start_width = 220
            start_height = 60

            pygame.draw.rect(win, (0, 255, 0), (start_x, start_y, start_width, start_height), border_radius= 10)
            pygame.draw.rect(win, (255, 0, 0), (250, 400, 220, 60), border_radius= 10)
            
            font2 = pygame.font.Font('b_e/fonts/pixeboy.ttf', 62)
            win.blit(font2.render('start', True, (0, 0, 0)), (285, 322))
            win.blit(font2.render('quit', True, (0, 0, 0)), (302, 412))

            button1y = list()
            button1x = list()
            button2y = list()
            button2x = list()

            for i in range(370):
                if i > 310:
                    button1y.append(i)
            for i in range(472):
                if i > 250:
                    button1x.append(i)

            for i in range(460):
                if i > 400:
                    button2y.append(i)
            for i in range(472):
                if i > 250:
                    button2x.append(i)

            if mouse_pos[0] in button1x and mouse_pos[1] in button1y:
                button = True
                if pygame.mouse.get_pressed()[0]:
                    pause = False
            if mouse_pos[0] in button2x and mouse_pos[1] in button2y:
                button = True
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.Sound('b_e/audio/off.wav').play()
                    save()
                    start_screen()

        pygame.display.update()

def start_screen():

    data = load_data()

    win = pygame.display.set_mode((750, 700))

    y = 300

    global condition2
    global condition
    global condition3

    speed = -1
    
    x = 350

    highest_score = str(data['highest'])

    if len(highest_score) == 1:
        x += 7
    else:
        for i in range(len(highest_score)):
            x -= i*3

    sound = pygame.mixer.Sound('b_e/audio/welcome.wav')
    if data['music']:
        sound.play(-1)

    a_x = 62
    a_y = 26
    
    settings = False

    while condition2:
        
        get_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condition2 = False
                condition = False
                condition3 = False

        color = (0, 0, 0)

        win.blit(pygame.image.load('b_e/ims/bg.png'), (0, 0))
        win.blit(pygame.image.load('b_e/ims/trophy.png'), (310, 500))

        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 50)
        text = font.render('Highest score', True, color)
        win.blit(text, (235, 400))

        text = font.render(highest_score, True, color)
        win.blit(text, (x, 450))

        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 75)
        text = font.render("click here to start", True, color)
        if (get_time//400) % 2 == 1:
            win.blit(text, (79, y))
        
        mouse_pos = pygame.mouse.get_pos()
        
        x_list = list()
        y_list = list()

        for i in range(683):
            if i > 79:
                x_list.append(i)
        for i in range(346):
            if i > 296:
                y_list.append(i)

        if data['music'] is True:
            volume = pygame.image.load('b_e/ims/volume.png')
        else:
            volume = pygame.image.load('b_e/ims/mute.png')
        
        volume = pygame.transform.scale(volume, (26, 26))
        
        setting_icon = pygame.image.load('b_e/ims/settings.png')
        setting_icon = pygame.transform.scale(setting_icon, (42, 42))
        arrow = pygame.image.load('b_e/ims/play.png')
        arrow = pygame.transform.scale(arrow, (15, 15))
        if settings is True:
            arrow = pygame.transform.rotate(arrow, -90)
        
        win.blit(setting_icon, (10, 10))

        if settings:
            win.blit(volume, (15, 85))
        
        v_x = list()
        v_y = list()
        
        for i in range(36):
            if i >= 15:
                v_x.append(i)
        for i in range(112):
            if i >= 85:
                v_y.append(i)

        font = pygame.font.Font('b_e/fonts/pixeboy.ttf', 20)
        win.blit(font.render(str("V" + data['version']), True, color), (10, 680))
        
        s_x = list()
        s_y = list()

        for i in range(50):
            if i > 10:
                s_x.append(i)
                s_y.append(i)

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if mouse_pos[0] in x_list and mouse_pos[1] in y_list:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                sound.stop()
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                start()
                condition4 = False
                condition2 = False
                a_y = -500

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            sound.stop()
            start()
            condition4 = False
            condition2 = False
            a_y = -500

        if mouse_pos[0] in s_x and mouse_pos[1] in s_y:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            if pygame.mouse.get_pressed()[0]:
                
                time.sleep(0.2)

                if settings is False:
                    settings = True
                    a_x, a_y = 20, 65
                else:
                    settings = False
                    a_x = 62
                    a_y = 26

        if mouse_pos[0] in v_x and mouse_pos[1] in v_y:
            if settings:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                if pygame.mouse.get_pressed()[0]:
                    
                    time.sleep(0.2)
                    
                    music = data['music']

                    if music is True:

                        data['music'] = False

                        with open('b_e/data/data.json', "w") as f:
                            json.dump(data, f)

                        sound.stop()
                        pygame.mixer.Sound('b_e/audio/off.wav').play()
                    else:

                        data['music'] = True

                        with open('b_e/data/data.json', "w") as f:
                            json.dump(data, f)
                        pygame.mixer.Sound('b_e/audio/on.wav').play()
                        sound.play(-1)

        win.blit(arrow, (a_x, a_y))
        
        pygame.display.update()

start_screen()

pygame.quit()
