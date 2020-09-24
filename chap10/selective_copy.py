import os, argparse, shutil
import sys
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(
        description='Walk through a directory tree looking for files of '
                    ' a certain extension then copy them elsewhere.'
    )
    parser.add_argument('ext', help='look for files of this extension')
    parser.add_argument('src', help='this is the tree where the files will be searched')
    parser.add_argument('dest', help='copy the found files to dest')
    args = parser.parse_args()

    src = os.path.abspath(args.src)
    dest = os.path.abspath(args.dest)

    if not os.path.exists(src):
        print(f'===> Error: `{src}` does not exist', file=sys.stderr)
        return 1

    # create dest directory
    print('===> Creating dest directory.')
    try:
        os.mkdir(dest)
        print(f'====> Destination directory `{dest}` successfully created.')
    except FileExistsError:
        print('====> Destination directory already exists. Aborting.')

    total_copied = 0
    for folder, subfolders, filenames in os.walk(src):
        # do not walk into dest directory
        if folder == dest:
            continue

        for filename in filenames:
            if Path(filename).suffix == args.ext:
                srcfile = os.path.join(folder, filename)
                print(f'===> Copying `{srcfile}` to {dest}...')
                shutil.copy(srcfile, dest)
                total_copied += 1

    print()
    if total_copied == 0:
        print(f':: No files found with the extension `{args.ext}`')

    print(f':: Total files copied: {total_copied}')
    return 0

if __name__ == '__main__':
    exit(main())
