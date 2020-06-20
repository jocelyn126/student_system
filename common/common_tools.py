"""
    常用工具箱
"""
import time

def get_int(message):
    while True:
        try:
            data = int(input(message))
            return data
        except:
            print("输入有误, 请重新输入.")


def generate_id(start_id):
    start_id += 1
    return start_id


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return result
    return wrapper
