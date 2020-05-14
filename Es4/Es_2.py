import threading
import random
import requests
import time
class Customer:
    def __init__(self,ID):
        self.ID=ID
        self.timer=random.randrange(1,10)#numero random tra 1 e 10

class Desk(threading.Thread):#MyThread diventa Desk perchè alla fine ogni desk è un thread
    availableDesk=[1,2,3,4,5]
    counter={#per contare quanti customer vengono serviti ad ogni desk, analisi
        "Desk 1":0,
        "Desk 2":0,
        "Desk 3":0,
        "Desk 4":0,
        "Desk 5":0,
    }
    def __init__(self, customer,semaphore):
        threading.Thread.__init__(self) #Setup thread
        self.customer = customer
        self.threadSemaphore=semaphore
    def run(self):
        self.threadSemaphore.acquire()
        desk=Desk.availableDesk.pop()
        Desk.counter[f"Desk {desk}"]+=1
        print(f'Customer {self.customer.ID} at desk {desk}')
        time.sleep(self.customer.timer)
        Desk.availableDesk.append(desk)
        self.threadSemaphore.release()

if __name__=="__main__":
    n_customers=30
    customers=[]
    for x in range(1,n_customers):
        customers.append(Customer(x))
    threadSemaphore=threading.Semaphore(len(Desk.availableDesk))

    threads=[]
    for customer in customers:
        threads.append(Desk(customer,threadSemaphore))
    start=time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    stop=time.time()
    total_time=stop-start
    avg_time=total_time/n_customers

    print(f'Total time: {total_time} seconds\n Average time per client: {avg_time} seconds\n Customers per desk: {Desk.counter} ')
