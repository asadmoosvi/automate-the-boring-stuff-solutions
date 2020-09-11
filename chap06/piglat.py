import sys

# also includes y, in addition to vowels
VOWELS = 'aeiouy'

def main() -> int:
    message = input('Enter the English message to translate into Pig Latin: ')
    words = message.split()

    pig_lat = []
    for word in words:
        word_prefix = ''
        while len(word) > 0 and not word[0].isalpha():
            word_prefix += word[0]
            word = word[1:]

        if len(word) == 0:
            pig_lat.append(word_prefix)
            continue

        word_postfix = ''
        while len(word) > 0 and not word[-1].isalpha():
            word_postfix += word[-1]
            word = word[:-1]

        if word[0].lower() in VOWELS:
            pig_lat.append(word_prefix + word + 'yay' + word_postfix)
        else:
            for vowel_start in range(len(word)):
                if word[vowel_start].lower() in VOWELS:
                    break
            word = word[vowel_start:] + word[:vowel_start]
            pig_lat.append(word_prefix + word + 'ay' + word_postfix)

    print('Translated to Pig Latin: ' + ' '.join(pig_lat))
    return 0

if __name__ == '__main__':
    sys.exit(main())
