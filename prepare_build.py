# coding: utf-8

import os
from decimal import *
from time import *
import re

out_file = open(os.path.join('output', 'bg.s'), "r")
string = out_file.read()
out_file.close()

max_frames = 100
num_frames = len(os.listdir(os.path.join('input'))) - 3 # Remove gitkeep, . and ..
start_bank = 2

j = 1
start = 0

pos = 0

limits = []
while pos < num_frames:
  limits.append(pos)
  s = string.split("_frame"+str(start + pos), 1)
  distance = max_frames
  prev_sign = False
  while True:
    if distance + pos > num_frames:
      s = s[1]
      break
    s2 = s[1].split(".globl _frame"+str(start + pos + distance), 1)
    s3 = s2[0]
    count = len(re.findall(r"0x[0-9a-fA-F][0-9a-fA-F]", s3))
    if count < 15799:
      if prev_sign:
        s = s3
        break
      distance += 1
    elif count > 15800:
      distance -= 1
      prev_sign = True
    else:
      s = s3
      break

  out_file = open(os.path.join("project", "background", "frames"+str(j)+".s"), "w")
  out_file.write(".area _CODE_"+str(j+1)+"\n\n.globl _frame"+str(start + pos)+s)
  pos += distance
  out_file.close()
  j += 1

j = start_bank
s = "unsigned long use_frame_bank(unsigned char frame) {\n"
s += "\tswitch(frame)\n\t{\n"
for l in limits:
  s+="\t\tcase "+str(l)+": return "+str(j)+";\n"
  j+=1
s+="\t\tdefault: return 1;\n\t}\n"
s+="}\n"

out_file = open(os.path.join("project", "frame_banks.h"), "w")
out_file.write(s)
out_file.close()


# def generaNomi1(n):
#   s = "{"
#   s+="frame0"
#   for i in range(1, n+1):
#     s+=",frame"+str(i)
#   return s+"}"

def build_frames(n):
  s = "extern unsigned char frame0[];\n"
  for i in range(1, n+1):
    s += "extern unsigned char frame"+str(i)+"[];\n"
  return s
def build_indexes(n):
  s = ".area _CODE_30\n\n.globl _frame0\n"
  for i in range(1, n+1):
    s += ".globl _frame"+str(i)+"\n"

  s+="\n\n.globl _frames\n.dw _frames\n_frames:\n"
  for i in range(n+1):
    if (i % 4) == 0:
      s+="\n.dw #_frame"+str(i)
    else:
      s += ",#_frame"+str(i)

  return s

def build_makefile(n):
  s1 = ""
  s2 = ""
  s1 += "..\\gbdk\\bin\\lcc -Wa-l -Wf-ba0 -c -o saveslot1.o saves/saveslot1.c\n"
  s1 += "..\\gbdk\\bin\\lcc -Wa-l -Wf-bo1 -c -o bg.o background/bg.s\n"
  
  s2 += "..\\gbdk\\bin\\lcc -Wl-yt3 -Wl-yo32 -Wl-ya4 -o video.gb indexes.o main.o saveslot1.o rle_lib.o bg.o"
  for i in range(len(n)):
    s1 += "..\\gbdk\\bin\\lcc -Wa-l -Wf-bo"+str(i+2)+" -c -o frames"+str(i+1)+".o background/frames"+str(i+1)+".s\n"
    s2 += " frames"+str(i+1)+".o"

  s1 += "..\\gbdk\\bin\\lcc -Wa-l -Wf-bo30 -c -o indexes.o background/indexes.s\n"
  s1 += "..\\gbdk\\bin\\lcc -Wa-l -c -o rle_lib.o gbdk-lib-extension/rle_lib.c\n"
  s1 += "..\\gbdk\\bin\\lcc -Wa-l -c -o main.o main.c"
  s2 += "\n\ndel *.o\ndel *.lst\n\n"
  return s1 + "\n\n" + s2

out_file = open(os.path.join("project", "background", "frames.h"), "w")
out_file.write(build_frames(num_frames))
out_file.close()

out_file = open(os.path.join("project", "background", "indexes.s"), "w")
out_file.write(build_indexes(num_frames))
out_file.close()

out_file = open(os.path.join("project", "makefile.bat"), "w")
out_file.write(build_makefile(limits))
out_file.close()
