import time

def slow_print(text, delay=0.05):
    for i in text:
        print(i, end='')
        time.sleep(delay)

slow_print("Hello, world!")
