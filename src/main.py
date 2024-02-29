import eel

import human_detetor
import eel_callbacks


def main():
    eel.init('src/web')
    eel.start('index.html', size=(960, 720))
    # human_detetor.get_humans()


if __name__ == '__main__':
    main()