import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_decorator
def calc_square(num):
    result = []
    for number in num:
        result.append(number*number)
    return result

@time_decorator
def calc_cube(num):
    result = []
    for number in num:
        result.append(number*number*number)
    return result

def sq_without_dec(num):
    start = time.time()
    result = []
    for number in num:
        result.append(number*number)
    end = time.time()
    print("square func without time_decorator took " + str((end-start)*1000) + "mil sec")
    return result

def cu_without_dec(num):
    start = time.time()
    result = []
    for number in num:
        result.append(number*number*number)
    end = time.time()
    print("Cube func without time_decorator took " + str((end-start)*1000) + "mil sec")
    return result
    

array = range(1,90000)
sq = sq_without_dec(array)
cu = cu_without_dec(array)
square = calc_square(array)
cube = calc_cube(array)
