import argparse
from typing import Optional, Sequence
import sys, os
import re

def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description='Mad Libs')
    parser.add_argument('filename', help='mad libs file')
    args = parser.parse_args(argv)

    if not os.path.exists(args.filename):
        print(f'==> error: file `{args.filename}` does not exist.')
        return 1

    with open(args.filename) as f:
        placeholder_regex = re.compile(
            r'ADJECTIVE|NOUN|ADVERB|VERB'
        )
        words = f.read().split()
        for i, word in enumerate(words):
            mo = placeholder_regex.search(word)
            if mo:
                user_input = input(f'Enter an {mo.group()}: ')
                words[i] = placeholder_regex.sub(user_input, word)

        output_file = args.filename + '.mlibs'
        with open(output_file, 'w') as out_f:
            out_f.write(' '.join(words) + '\n')
            print(f'==> text written to output file: `{output_file}`')
    return 0

if __name__ == '__main__':
    exit(main())
