import time

def main():

    config = [
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'red', 'l2b': 'red', 'wait': 1.5},
        {'l1a': 'green', 'l1b': 'green', 'l2a': 'red', 'l2b': 'red', 'wait': 5},
        {'l1a': 'yellow', 'l1b': 'yellow', 'l2a': 'red', 'l2b': 'red', 'wait': 2},
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'red', 'l2b': 'red', 'wait': 1.5},
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'green', 'l2b': 'green', 'wait': 5},
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'yellow', 'l2b': 'yellow', 'wait': 1.5}
    ]

    loops = 0

    while loops < 3:
        for i in config:
            l1a = i.get('l1a')
            l1b = i.get('l1b')
            l2a = i.get('l2a')
            l2b = i.get('l2b')
            
            print_light(l1a, l1b, l2a, l2b)  
            time.sleep(i.get('wait'))

        loops +=1

def print_light(l_1a, l_1b, l_2a, l_2b):
    print(f'light_1a: {l_1a}', ' ', f'light_2a: {l_2a}')
    print()
    print(f'light_2b: {l_2b}', ' ',f'light_1b: {l_1b}')
    print()


if __name__ == '__main__':
    main()
