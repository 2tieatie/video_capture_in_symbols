import pygame
import sys
import textwrap

pygame.init()
sc = pygame.display.set_mode((1280, 720))
en = {97: 'A', 98: 'B', 99: 'C', 100: 'D', 101: 'E', 102: 'F', 103: 'G', 104: 'H', 105: 'I', 106: 'J', 107: 'K', 108: 'L', 109: 'M', 110: 'N', 111: 'O', 112: 'P', 113: 'Q', 114: 'R', 115: 'S', 116: 'T', 117: 'U', 118: 'V', 119: 'W', 120: 'X', 121: 'Y', 122: 'Z', 32: ' '}
ru = {97: 'Ф', 98: 'И', 99: 'С', 100: 'В', 101: 'У', 102: 'А', 103: 'П', 104: 'Р', 105: 'Ш', 106: 'О', 107: 'Л', 108: 'Д', 109: 'Ь', 110: 'Т', 111: 'Щ', 112: 'З', 113: 'Й', 114: 'К', 115: 'Ы', 116: 'Е', 117: 'Г', 118: 'М', 119: 'Ц', 120: 'Ч', 121: 'Н', 122: 'Я', 96: 'Ё', 91: 'Х', 93: 'Ъ', 59: 'Ж', 39: 'Э', 44: 'Б', 46: 'Ю', 32: ' '}
ua = {97: 'Ф', 98: 'И', 99: 'С', 100: 'В', 101: 'У', 102: 'А', 103: 'П', 104: 'Р', 105: 'Ш', 106: 'О', 107: 'Л', 108: 'Д', 109: 'Ь', 110: 'Т', 111: 'Щ', 112: 'З', 113: 'Й', 114: 'К', 115: 'І', 116: 'Е', 117: 'Г', 118: 'М', 119: 'Ц', 120: 'Ч', 121: 'Н', 122: 'Я', 91: 'Х', 93: 'Ї', 59: 'Ж', 39: 'Є', 44: 'Б', 46: 'Ю', 32: ' '}
text_to_type = "тест текста для тайпинга, печати и всего остального"
text_to_type = text_to_type.lower()
symb = '1234567890-=!@#$%^&*()_+`~[]{};\'\"\\?/.>,<'
width = 40
text = []
font_size = 50
text_font = pygame.font.SysFont('bahnschrift', font_size)
main_index = 0
bg_color = (50, 50, 200)
clock = pygame.time.Clock()
sec_main_index = 0

for i in text_to_type:
    for j in symb:
        if i == j:
            text_to_type = text_to_type.replace(j, ' ')

text_to_type = ' '.join(text_to_type.split())

for line in textwrap.wrap(text_to_type, width=width):
    text.append(line)


writed_text = text.copy()


for index, i in enumerate(writed_text):
    for index_1, i1 in enumerate(writed_text[index]):
        writed_text[index] = len(writed_text[index]) * ' '


def events():
    global main_index, writed_text, width, bg_color, sec_main_index
    back = True
    back_list = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for let in ru.keys():
                if event.key == let and sec_main_index < len(text):
                    if ru[let].lower() == text[sec_main_index][main_index]:
                        writed_text[sec_main_index] = text[sec_main_index][0:main_index + 1] + (len(text[sec_main_index]) - len(text[sec_main_index][0:main_index + 1])) * ' '
                        if writed_text[sec_main_index] == text[sec_main_index]:
                            main_index = 0
                            sec_main_index += 1
                        main_index += 1
                        print(writed_text)
                    else:
                        if bg_color != (170, 170, 200):
                            bg_color = (70, 170, 200)
                elif event.key == 8 and back and main_index >= 1:
                    for i in writed_text[sec_main_index]:
                        back_list.append(i)
                    print(back_list)
                    back_list[main_index] = ' '
                    main_index -= 1
                    writed_text[sec_main_index] = ''.join(back_list)
                    back = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 8:
                back = True


def draw_text(text: list, font, color: tuple):
    for index, i in enumerate(text):
        text_1 = font.render(i, True, color, None)
        sc.blit(text_1, (120, 150 + index * font_size))


while True:
    events()
    clock.tick(60)
    if bg_color != (50, 50, 200):
        bg_color = (50, bg_color[1] - 150 // 120, 200)
    sc.fill(bg_color)
    text_1 = text_font.render(f'{main_index}/{len(text_to_type)}', True, (230, 200, 0), None)
    sc.blit(text_1, (360, 100))
    draw_text(text, text_font, (170, 170, 170))
    draw_text(writed_text, text_font, (200, 50, 100))
    pygame.display.update()
