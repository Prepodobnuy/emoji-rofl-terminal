from time import sleep

from toemoji import spaceToEmoji
from configreader import Config


def main():
    
    config = Config()
    timedelay = config.TimeDelay()
    textfilename = config.TextName()

    while True:
        file = open(textfilename)
        text = file.read()
        file.close()

        print(spaceToEmoji(text))

        sleep(timedelay)

if __name__ == '__main__':
    main()