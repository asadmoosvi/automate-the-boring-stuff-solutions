from pathlib import Path
import re
import shutil

def main() -> int:
    prefix = input('Enter file prefix: ')
    filenames = Path.cwd().glob(prefix + '*')
    filenames = sorted(filenames, key=str)
    file_matches = []
    for filename in filenames:
        mo = re.match(f'({prefix})(.*?)(\d+)(.*)', filename.name)
        if mo:
            file_matches.append(mo)

    invalid_file_idx = None
    for idx, match in enumerate(file_matches):
        file_no = int(match.group(3))
        if idx > 0:
            previous_file_no = int(file_matches[idx - 1].group(3))
            if file_no - previous_file_no != 1:
                invalid_file_idx = idx;
                break

    if invalid_file_idx is not None:
        new_file_no =  int(file_matches[invalid_file_idx - 1].group(3)) + 1
        for x in range(invalid_file_idx, len(file_matches)):
            old_filename = file_matches[x].group()
            print(f'renaming file from {old_filename} to ', end='')
            new_filename = (file_matches[x].group(1) + file_matches[x].group(2) +
                            f'{new_file_no:02d}' + file_matches[x].group(4))
            print(new_filename)
            shutil.move(old_filename, new_filename)
            new_file_no += 1

    return 0

if __name__ == '__main__':
    exit(main())
