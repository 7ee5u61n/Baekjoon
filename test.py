upperVowel = ['A', 'I', 'Y', 'E', 'O', 'U']
upperConsonant = ['B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F']
lowerVowel = ['a', 'i', 'y', 'e', 'o', 'u']
lowerConsonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

while True:
    try:
        s = str(input())    
        for i in range(len(s)):
            if s[i].isupper():
                if s[i] in upperVowel:
                    print(upperVowel[(upperVowel.index(s[i])+3)%6], end='')
                else:
                    print(upperConsonant[(upperConsonant.index(s[i])+10)%20], end='')
            elif s[i].islower():
                if s[i] in lowerVowel:
                    print(lowerVowel[(lowerVowel.index(s[i])+3)%6], end='')
                else:
                    print(lowerConsonant[(lowerConsonant.index(s[i])+10)%20], end='')

            else:
                print(s[i], end='')
        print()
    except EOFError:
        break