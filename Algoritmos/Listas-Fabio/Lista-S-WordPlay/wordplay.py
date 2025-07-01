import os
from str_utils import avoids, is_abecedarian, to_lower, uses_all, uses_only
from hello_map import mapear, filtrar

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'br-sem-acentos.txt'
FULL_FILE_PATH = os.path.join(SCRIPT_DIR, FILE_NAME)

def main():
    palavras = load_palavras()

    menu = '''
|>>>> WordPLAY <<<<|
1 - Palavras com Tamanho N+ (9.1)
2 - Palavras sem Caracter Proibido (9.2)
3 - Palavras sem Letras Proibidas (9.3)
4 - Palavras somente com Letras Permitidas (9.4)
5 - Palavras com Letras Obrigatórias (9.5)
6 - Palavras com Letras em Ordem Alfabética (9.6)

0 - Sair
>>>> '''

    option = int(input(menu))

    while option != 0:
        if option == 1:
            show_words_by_size(palavras)
        elif option == 2:
            show_words_without_forbidden_char(palavras)
        elif option == 3:
            forbidden_letters = input('Letras Proibidas: ')
            show_words_without_forbidden_letters(palavras, forbidden_letters)
        elif option == 4:
            allowed_letter = input('Letras Permitidas: ')
            show_words_without_allowed_letter(palavras, allowed_letter)
        elif option == 5:
            mandatory_letters = input('Letras Obrigatórios: ')
            show_words_with_mandatory_letters(palavras, mandatory_letters)
        elif option == 6:
            show_abecedarian_words(palavras)

        input('>>> continue...')
        clear_screen()
        option = int(input(menu))

    print('Fim.')

def show_words_by_size(palavras):
    size = int(input('Qual tamanho min das palavras: '))
    palavras_filtradas = filtrar(palavras, lambda x: len(x) >= size)
    show_words(palavras_filtradas)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)

def show_words_without_forbidden_char(palavras):
    forbidden = input('Qual é a letra proibida? ')
    palavras_filtradas = filtrar(palavras, lambda word: forbidden not in word)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)


def show_words_without_forbidden_letters(palavras, forbidden_letters):
   palavras_filtradas = filtrar(palavras, lambda word: avoids(word, forbidden_letters))
   show_words(palavras_filtradas)
   counter = len(palavras)
   filter_counter = len(palavras_filtradas)
   footer(counter, filter_counter)

def show_words_with_allowed_letters(palavras, allowed_letters):
    palavras_filtradas = filtrar(palavras, lambda word: uses_all(word, allowed_letters))
    show_words(palavras_filtradas)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_words_without_allowed_letter(palavras, allowed_letters):
    palavras_filtradas = filtrar(palavras, lambda word: uses_only(word, allowed_letters))
    show_words(palavras_filtradas)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)
    

def show_words_with_mandatory_letters(palavras, mandatory_letters):
    palavras_filtradas = filtrar(palavras, lambda word: uses_all(word, mandatory_letters))
    show_words(palavras_filtradas)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)

def show_abecedarian_words(palavras):
    palavras_minusculas =  mapear(palavras, to_lower)
    palavras_filtradas = filtrar(palavras_minusculas, lambda word:  is_abecedarian(word))
    show_words(palavras_filtradas)
    counter = len(palavras)
    filter_counter = len(palavras_filtradas)
    footer(counter, filter_counter)

def footer(counter, filter_counter):
    print('------------')
    if counter > 0:
        percentage = filter_counter / counter * 100
        print(f'Total/Filtro: {filter_counter}/{counter} ({percentage:.3f}%)')
    else:
        print('Total/Filtro: 0/0 (0.000%)')

def show_words(word_list):
    for word in word_list:
        print(word)

def load_palavras():
    with open(FULL_FILE_PATH) as file:
        return mapear(file.readlines(), lambda x: x.strip())

if __name__ == '__main__':
    main()