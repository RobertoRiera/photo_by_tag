import ChictopiaDownloader
import time


def tiempo():
    return int(round(time.time() * 1000))

tiempo_empezar = tiempo()
ChictopiaDownloader.ChictopiaDownloader(1, 2)
tiempo_final = tiempo()

print(tiempo_final-tiempo_empezar)
