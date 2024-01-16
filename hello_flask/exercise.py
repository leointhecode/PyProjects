import time


def speed_calc_decorator(function):
    def inner():
        start_time = time.time()
        function()
        finish_time = time.time()
        final_time = finish_time - start_time
        return final_time
    return inner


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast = fast_function()
slow = slow_function()

print(f"fast function : {fast}")
print(f"slow function : {slow}")
