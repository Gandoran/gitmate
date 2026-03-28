import time

fotogrammi = ['[=    ]', '[ =   ]', '[  =  ]', '[   = ]', '[    =]']

def print_bar(stop_event, testo):
    count = 0
    while not stop_event.is_set():
        k = count % 5
        print(f"\r{testo}... {fotogrammi[k]}", end="", flush=True)
        time.sleep(0.1)
        count += 1
    print("\r" + " " * 50 + "\r", end="", flush=True)