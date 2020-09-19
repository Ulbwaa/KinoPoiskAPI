from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

top500 = kinopoisk.top500()

for item in top500:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
