import time

def main():

    config = [
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'red', 'l2b': 'red', 'wait': 1.5},
        {'l1a': 'green', 'l1b': 'green', 'l2a': 'red', 'l2b': 'red', 'wait': 5},
        {'l1a': 'yellow', 'l1b': 'yellow', 'l2a': 'red', 'l2b': 'red', 'wait': 2},
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'green', 'l2b': 'green', 'wait': 5},
        {'l1a': 'red', 'l1b': 'red', 'l2a': 'yellow', 'l2b': 'yellow', 'wait': 1.5}
    ]

    loops = 0

    while loops < 3:
        light_1 = change_light_color_to_green(light_1)
        light_3 = change_light_color_to_green(light_3)
        print_light(light_1, light_2, light_3, light_4)
        
        time.sleep(5)

        light_1 = change_light_color_to_yellow(light_1)
        light_3 = change_light_color_to_yellow(light_3)
        print_light(light_1, light_2, light_3, light_4)

        time.sleep(3)

        light_1 = change_light_to_red(light_1)
        light_3 = change_light_to_red(light_3)
        print_light(light_1, light_2, light_3, light_4)

        time.sleep(1.5)

        light_2 = change_light_color_to_green(light_2)
        light_4 = change_light_color_to_green(light_4)
        print_light(light_1, light_2, light_3, light_4)

        time.sleep(5)

        light_2 = change_light_color_to_yellow(light_2)
        light_4 = change_light_color_to_yellow(light_4)
        print_light(light_1, light_2, light_3, light_4)

        time.sleep(3)

        light_2 = change_light_to_red(light_2)
        light_4 = change_light_to_red(light_4)
        print_light(light_1, light_2, light_3, light_4)

        
        loops +=1
        time.sleep(1.5)

def print_light(l_1, l_2, l_3, l_4):
    print(f'light_2: {l_2}', ' ', f'light_3: {l_3}')
    print()
    print(f'light_1: {l_1}', ' ',f'light_4: {l_4}')
    print()

def change_light_color_to_green(light_color):
    if light_color == 'red':
        return 'green'
    else:
        return light_color
    
def change_light_color_to_yellow(light_color):
    if light_color == 'green':
        return 'yellow'
    else: 
        return light_color
    
def change_light_to_red(light_color):
    if light_color == 'yellow':
        return 'red'
    else:
        return light_color


    
    
if __name__ == '__main__':
    main()
