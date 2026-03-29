limite = float(input("Limite (%): "))

import psutil, time
while True:
    uso = psutil.virtual_memory().percent

    print("Uso atual:", uso, "%")

    if uso > limite:
        print("ALERTA!")

        time.sleep(2)