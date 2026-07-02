import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cheesecode("hello,"+ sys.argv[1])