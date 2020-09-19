from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

tenet = kinopoisk.get_film(1236063)

print(tenet.ru_name, tenet.year)
print(", ".join(tenet.genres))
print(", ".join(tenet.countries))
print(tenet.tagline)