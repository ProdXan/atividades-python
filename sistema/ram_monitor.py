import psutil
import time

while True:
    mem = psutil.virtual_memory()

    print('Total:', mem.total / (1024**2), "MB")
    print('Usado:', mem.used / (1024**2),  "MB")
    print('Luvre:', mem.available / (1024**2), "MB")
    print('Uso:', mem.percent, "%")

    print("-" * 30)
    time.sleep(2)