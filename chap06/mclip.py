#!/usr/bin/env python3
import sys, pyperclip

TEXT = {
    'agree': 'Yes, I agree. That sounds fine to me.',
    'busy': 'Sorry, can we do this later this week or next week?',
    'upsell': 'Would you consider making this a monthly donation?'
}

def main() -> int:
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} [keyphrase] copy phrase text')
        return 1

    keyphrase = sys.argv[1]
    keyphrase_text = TEXT.get(keyphrase.lower())

    if keyphrase_text:
        pyperclip.copy(TEXT[keyphrase.lower()])
        print(f'    -> Text for `{keyphrase}` copied into the clipboard')
    else:
        print(f'    -> There is no text for `{keyphrase}`')
        return 2

    return 0

if __name__ == '__main__':
    sys.exit(main())
