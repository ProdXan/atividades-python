import psutil
while True:
    print('CPU Total:', psutil.cpu_percent(interval=1))
    print('Por núcleo:', psutil.cpu_percent(interval=1, percpu=True))