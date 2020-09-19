from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

search = kinopoisk.search('Догвилль')

for item in search:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
