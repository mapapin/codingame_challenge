import sys
import math
w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
w0 = 0
h0 = 0
# game loop
while True:
    bomb_dir = input()

    if bomb_dir == "U":
        h = y0
        y0 = int((y0 + h0) / 2)

    if bomb_dir == "D":
        h0 = y0
        y0 = int((y0 + h) / 2)

    if bomb_dir == "L":
        w = x0
        x0 = int((x0 + w0) / 2)

    if bomb_dir == "R":
        w0 = x0
        x0 = int((x0 + h) / 2)

    if bomb_dir == "UR":
        h = y0
        w0 = x0
        y0 = int((y0 + h0) / 2)
        x0 = int((x0 + w) / 2)

    if bomb_dir == "UL":
        h = y0
        w = x0
        y0 = int((y0 + h0) / 2)
        x0 = int((x0 + w0) / 2)

    if bomb_dir == "DR":
        h0 = y0
        w0 = x0
        y0 = int((y0 + h) / 2)
        x0 = int((x0 + w) / 2)

    if bomb_dir == "DL":
        h0 = y0
        w = x0
        y0 = int((y0 + h) / 2)
        x0 = int((x0 + w0) / 2)

    print(str(x0) + " " + str(y0))
