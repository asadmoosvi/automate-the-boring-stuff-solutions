import os, argparse
import humanize
import sys

def main() -> int:
    parser = argparse.ArgumentParser(
        description='List large files (over 100MB)'
    )
    parser.add_argument(
        'dir', help='recursively search this dir for large files'
    )
    args = parser.parse_args()

    if not os.path.exists(args.dir):
        print(f'==> dir `{args.dir}` does not exist.')
        return 1

    print('Large Files (over 100MB)'.center(40))
    print('-' * 40)
    large_files_count = 0
    for folder, subfolders, filenames in os.walk(args.dir):
        for filename in filenames:
            filename = os.path.join(folder, filename)
            try:
                file_size = os.path.getsize(filename)
                if file_size > 100 * 1024 * 1024:
                    print(
                        f'{filename}'
                        f' ({humanize.naturalsize(file_size)})'
                    )
                    large_files_count += 1
            except FileNotFoundError:
                # do not complain on broken symlinks, etc
                pass

    if large_files_count == 0:
        print('...'.center(40))
    print(f'\nTotal: {large_files_count}')

    return 0

if __name__ == '__main__':
    exit(main())
