import time as t
import datetime

def main():
    print_header()
    # current_time()
    start_pomodoro_timer()


def print_header():
    print('-----------------------')
    print('    Pomodoro Timer')
    print('-----------------------')


# def current_time():
#     now = datetime.today()
#     print('The time is {}'.format(now))
#     now_plus_25m = now + timedelta(minutes=25)
#     print('Twenty-five minutes from now will be {}'.format(now_plus_25m))


def start_pomodoro_timer():
    while True:
        cmd = input('Start a new [p]omodoro task, [b]reak, [c]ustom time, or e[x]it?')
        if cmd == 'p':
            print('Time to work')
            t.sleep(25)
        elif cmd == 'b':
            print('Time for a break')
            t.sleep(5)
        elif cmd == 'c':
            custom_time = int(input('Enter a custom time interval (0-99)'))
            t.sleep(custom_time)
        elif cmd == 'x':
            print('Exiting')
            break


if __name__ == '__main__':
    main()
