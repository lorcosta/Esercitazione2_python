import threading
import time
import requests

class MyThread(threading.Thread):
    def __init__(self, threadID,website):
        threading.Thread.__init__(self) #Setup thread
        self.threadID = threadID
        self.website=website
    def run(self):
        r=requests.get(self.website)


#Websites list
website_list= ["http://yahoo.com",
               "http://google.com",
               "http://amazon.com",
               "http://ibm.com",
               "http://apple.com",
               "https://www.microsoft.com",
               "https://www.youtube.com/",
               "https://www.polito.it/",
               "http://www.wikipedia.org",
               "https://www.reddit.com/",
               "https://www.adobe.com/",
               "https://wordpress.org/",
               "https://github.com/",
               "https://www.google.com/maps/"]

if __name__ == '__main__':
    start = time.time()
    for site in website_list:
        r=requests.get(site)
    stop=time.time()
    execution_time=stop-start
    print(f"Tempo di esecuzione sequenziale: {execution_time} secondi")

    start=time.time()
    threads=[]
    for threadID,website in enumerate(website_list):
        threads.append(MyThread(threadID,website))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    stop=time.time()
    execution=stop-start
    print(f"Tempo di esecuzione con threading: {execution} secondi")
