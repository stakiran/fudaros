# encoding: utf-8

import os
import sys

def abort(msg):
    print('Error!: {0}'.format(msg))
    exit(1)

def open_file_with_assoc(filepath):
    # - ブロッキングを防ぐために start 経由で開く
    # - 関連付けはファイルパスを指定するだけで開けるので
    #   プログラム名は指定しない
    os.system('start "" "{}"'.format(filepath))

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def file2str(filepath):
    ret = ''
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = f.read()
    return ret

def str2file(filepath, s):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.write(s)

def test():
    pass

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('--open', default=False, action='store_true',
        help='Open skippee.md with associated editor.')

    parser.add_argument('--skip', default=False, action='store_true',
        help='Do skip tasks. / Read from skippe.md and reflect tasks to timeline.md')

    parser.add_argument('--start', default=False, action='store_true',
        help='Start a day. / Read from timeline.md and reflect today tasks to today.md ')

    parser.add_argument('--test', default=False, action='store_true',
        help='[DEBUG] Do unittest.')

    args = parser.parse_args()
    return args

def ____main____():
    pass

if __name__ == "__main__":
    MYFULLPATH = os.path.abspath(sys.argv[0])
    MYDIR = os.path.dirname(MYFULLPATH)

    args = parse_arguments()
    if args.test:
        test()
        exit(0)
