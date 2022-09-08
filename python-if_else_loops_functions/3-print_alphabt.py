#!/usr/bin/python3
for letters in range(ord('a'), ord('z')+1):
  if letters != 101 and letters != 113:
        continue
      print("{:c}".format(letters), end="")
      