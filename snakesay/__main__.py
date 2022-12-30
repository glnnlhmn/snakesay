import sys

from snakesay import snake

def main():
    snake.say(" ".join(sys.argv[1:]))

main()
