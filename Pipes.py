import multiprocessing

def msg(conn):
    conn.send(['hello'])
    conn.close()

if __name__ == '__main__':
    s_conn, e_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=msg, args=(s_conn,))
    p2 = multiprocessing.Process(target=msg, args=(e_conn,))
    
    p1.start()
    p2.start()
    print(s_conn.recv())
    e_conn.send(['hello from p1'])
    print(s_conn.recv())
    e_conn.send(['hello from p2'])
    print(s_conn.recv())
    p1.join()
    p2.join()
