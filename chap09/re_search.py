import re, sys, argparse, os
from typing import Optional, Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='search a folder for files that match a regex'
    )
    parser.add_argument(
        'folder', help='folder that contains the files to be searched'
    )
    parser.add_argument('regex', help='regex to match')
    args = parser.parse_args()

    if not os.path.exists(args.folder):
        print(f'==> error: folder `{args.folder}` does not exist')
        return 1

    regex = re.compile(args.regex)
    file_matches = []
    for item in os.listdir(args.folder):
        if os.path.isfile(item):
            with open(item) as f:
                file_lines = [line.rstrip() for line in f.readlines()]
                for i, line in enumerate(file_lines):
                    mo = regex.search(line)
                    if mo:
                        file_matches.append({
                            'filename': item,
                            'line_no': i + 1,
                            'line': line
                        })

    if file_matches:
        print(f'{len(file_matches)} Matches found'.center(80))
        print('-' * 80)
        for match in file_matches:
            print(f"{match['filename']}:{match['line_no']}:{match['line']}")
    else:
        print('No matches found.')

    return 0

if __name__ == '__main__':
    exit(main())
