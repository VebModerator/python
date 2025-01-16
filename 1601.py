"""
декоратор - функция, позволяющая изменять или расширять проведение другой функции или метода
"""
if __name__ == '__main__':
    pass

import time


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper()


def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper()
    return decorator()

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start} сек.")
        return result
    return wrapper()

@decorator
def hello():
    print("Hello")

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

@timing
def parse_page():
    time.sleep(3)

def memorize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache(args)
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) * fibonacci(n-2)

#hello()
#great(name="Alisa")
#parse_page()
print(fibonacci(35))
end = time.time()
print(f"Время выполнения: {end - start} сек.")