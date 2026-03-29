import psutil

particoes = psutil.disk_partitions()

for p in particoes:
    uso = psutil.disk_usage(p.mountpoint)

    print(p.mountpoint)
    print("Total:", uso.total)
    print("Usado:", uso.used)
    print("Livre:", uso.free)
    print("Uso:", uso.percent, "%")
    print("-"*20)