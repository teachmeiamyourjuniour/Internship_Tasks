# 18.The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowel = {'A','E','I','O','U'}
    kevin = 0
    stuart = 0
    lenth = len(string)
    for i in range(0,lenth):
        if string[i] in vowel:
            kevin += lenth - i
        if string[i] not in vowel:
            stuart += lenth - i
    
    if kevin > stuart:
        print('Kevin ' + str(kevin))
    elif kevin == stuart:
        print('Draw')
    elif kevin < stuart:
        print('Stuart ' + str(stuart))

if __name__ == '__main__':
    s = input()
    minion_game(s)
