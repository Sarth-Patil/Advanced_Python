import multiprocessing
import os


def calc_square(numbers, result):
    for index, n in enumerate(numbers):
        result[index] = n*n

if __name__ == "__main__":
    print("ID of main process: {}".format(os.getpid())) 

    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result))

    p.start()

    print("ID of process p1: {}".format(p.pid)) 

    p.join()

    #print(result)
    print(result[:])