import glob, os

all_files = glob.glob("/Users/funami/Creative Cloud Files/**", recursive=True)

out_str = [
    '<',
    '>',
    '：',
    '\"',
    '/',
    '\\',
    '|',
    '?',
    '*',
    'CON',
    'PRN',
    'AUX',
    'NUL',
    'COM1',
    'COM2',
    'COM3',
    'COM4',
    'COM5',
    'COM6',
    'COM7',
    'COM8',
    'COM9',
    'LPT1',
    'LPT2',
    'LPT3',
    'LPT4',
    'LPT5',
    'LPT6',
    'LPT7',
    'LPT8',
    'LPT9'
]

for f in all_files:
    ff = os.path.basename(f)
    for s in out_str:
        if s in ff:
            print(f)
            print(ff)
