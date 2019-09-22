import threading

def create_threads(list, function)

    threads = []
    
    for ip_address in list:
        th = threading.Thread(target = function, args = (ip_address,))
        th.start()
        threads.append(th)
    
    for th in threads:
        th.join()