# Realizar un codigo de python que simule un reloj
# formato 24 horas
# que empiece en 00:00 hasta 23:59 y se reinicie
# pero que implemente time.sleep(X) para que se actualice
# cada segundo o mas acelarado.

import time

hora = 0
minuto = 0

while True:
        print(f"{hora:02d}:{minuto:02d}")
        time.sleep(0.01)
        minuto += 1
        if minuto == 60:
            minuto = 0
            hora += 1
        if hora == 24:
            hora = 0


