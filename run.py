import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('6928022743.py')#2024-01-29 12:11:36.557440

scripts.append('6928022743.py')#2024-01-29 12:05:31.466855

scripts.append('6928022743.py')#2024-01-29 11:50:41.158199

scripts.append('6928022743.py')#2024-01-29 11:34:24.885417

scripts.append('6928022743.py')#2024-01-29 11:29:57.491288

scripts.append('6928022743.py')#2024-01-29 11:24:22.556485

scripts.append('6928022743.py')#2024-01-29 11:15:54.326249

scripts.append('6581896306.py')#2024-01-29 10:44:27.944713

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

