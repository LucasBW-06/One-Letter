def find_word(array): # função que faz a menor palavra lexicografica
    word = ''.join(sorted(min(i) for i in array)) # seleciona ao menor caractere de cada string de array, ordena lexicograficamente e concatena numa string única
    return word

num = int(input()) # recebe um número inteiro N
words = [input() for _ in range(num)] # recebe N strings

word = find_word(words) # recebe a menor palavra lexicográfica possível de ser formada utilizando um letra de cada palavra da lista

print(word)