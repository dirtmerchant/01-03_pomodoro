from datetime import datetime, timedelta


def main():
    print_header()
    current_time()


def print_header():
    print('-----------------------')
    print('    Pomodoro Timer')
    print('-----------------------')


def current_time():
    now = datetime.today()
    print('The time is {}'.format(now))
    now_plus_25m = now + timedelta(minutes=25)
    print('Twenty-five minutes from now will be {}'.format(now_plus_25m))


if __name__ == '__main__':
    main()
