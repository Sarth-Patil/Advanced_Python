import multiprocessing

def msg(q):
    q.put(['hello'])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=msg, args=(q,))
    p2 = multiprocessing.Process(target=msg, args=(q,))
    p1.start()
    print(q.get())
    q.put(['hello from p1'])
    p1.join()
    p2.start()
    print(q.get())
    q.put(['hello from p2'])
    print(q.get())
    p2.join()
