#! python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description='Compile files with inline compiling descriptions')

parser.add_argument('file', metavar='file name', type=str, help='File to be compiled')
parser.add_argument('target', metavar='target', nargs='?', type=str, help='Compile target, defauts to all', default='all')

args = parser.parse_args()


opts = {'current_file': args.file}


file = open(args.file)

line = file.readline().strip()
while(not line == '$$inlineMake$$'):
  line = file.readline().strip()

line = file.readline().strip()
while(not line == '$$inlineMake$$'):
  if line == '' or line[0] == '#':
    pass
  else:
    opt = line.split('#', 1)[0].split('=', 1)
    # print(opt)
    opts[opt[0].strip()] = opt[1].strip()

  line = file.readline().strip()

# print(opts)

cmd = opts[args.target].format(**opts)
print(cmd)

subprocess.call(cmd, shell=True) 