import psutil, time

old = psutil.net_io_counters()

while True:
    time.sleep(1)
    new = psutil.net_io_counters()

    down = new.bytes_recv - old.bytes_recv
    up = new.bytes_sent - old.bytes_recv

    print("Download:", down/1024, "KB/s")
    print("Upload:", up/1024, "KB/s")

    old = new
    