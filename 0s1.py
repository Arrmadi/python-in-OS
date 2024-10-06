from multiprocessing import Process  
import os  

def f(name):
    print(f'process: {os.getpid()}, parent: {os.getppid()}, hello {name}')

if __name__ == "__main__":
    print(f'main process: {os.getpid()}')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    print(f'Child Process ID: {p.pid}')
