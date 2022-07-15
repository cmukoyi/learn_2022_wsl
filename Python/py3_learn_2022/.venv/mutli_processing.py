

from  multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
        

def main():
    print(cpu_count())
    a = Process(target=counter,args=(1,))
    b = Process(target=counter,args=(1,))
    c = Process(target=counter,args=(1,))
    d = Process(target=counter,args=(1,))
    e = Process(target=counter,args=(1,))
    f = Process(target=counter,args=(1,))
    g = Process(target=counter,args=(1,))
    h = Process(target=counter,args=(0,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()


    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    
    print("finished in ", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
