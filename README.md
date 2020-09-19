# <p align="center">KinoPoiskAPI
<p align="center">Модуль Python для взаимодействия с нефициальным <a href="https://kinopoiskapiunofficial.tech/">API КиноПоиска</a>.

## Начало работы
Модуль протестирован на Python3.8 и Python3.7. Для установки модуля есть два пути:
* Установка через подмодуль Git:
```
$ git submodule add https://github.com/Ulbwaa/KinoPoiskAPI
```

* Установка через клонирование репозитория в Ваш проект:
```
$ git clone https://github.com/Ulbwaa/KinoPoiskAPI
```

Рекомендуется использовать первый способ. 

## Получение токена KinopoiskAPI
Для получения токена необходима регистрация на сайте 
<a href="https://kinopoiskapiunofficial.tech/signup">kinopoiskapiunofficial.tech</a>. 
После регистрации перейдите в настройки своего <a href="https://kinopoiskapiunofficial.tech/user">профиля</a> и сохраните токен. 
<p align="center">
    <img src="https://i.imgur.com/QkXRQ9t.png" alt="Регистрация">
</p>

## Инициализация скрипта
```python
from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

print(kinopoisk.about, kinopoisk.version)
```

```
>>> KinoPoiskAPI 1.0-release
```

## Получение информации о фильме по ID КиноПоиска
```python
from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

tenet = kinopoisk.get_film(1236063)

print(tenet.ru_name, tenet.year)
print(", ".join(tenet.genres))
print(", ".join(tenet.countries))
print(tenet.tagline)
```

```
>>> Довод 2020
>>> боевик, фантастика
>>> Великобритания, США
>>> Время уходит
```

### Возвращаемые параметры функцией KP.get_film
* ID фильма на КиноПоиске - `self.kp_id`
* Название фильма на языке оригинала - `self.name`
* Название фильма на русском языке - `self.ru_name`
* Год премьеры фильма - `self.year` (В случае получения сериала возвращается год выхода первой серии) 
* Продолжительность фильма - `self.duration`
* "Слоган" фильма - `self.tagline` (В случае отсутствия слогана на русском языке возвращается слоган на языке оригинала)
* Описание фильма - `self.description`
* Список с жанрами - `self.genres`
* Список с странами - `self.countries`
* Возврастное ограничение - `self.age_rating`
* Оценка на КиноПоиске - `self.kp_rate`
* Оценка на IMDb - `self.imdb_rate`
* Ссылка на фильм на КиноПоиске - `self.kp_url`
* Полная дата премьеры - `self.premiere` (В случае отсутствия возвращается параметр `self.year`)
* Ссылка на изображение постера - `self.poster`
* Уменьшенное изображение постера - `self.poster_preview`

## Поиск фильма на КиноПоиске по ключевому слову
```python
from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

search = kinopoisk.search('Догвилль')

for item in search:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
```

```
>>> Догвилль 2003
>>> триллер, драма, детектив
>>> Дания, Нидерланды, Швеция
>>> ...
```

### Возвращаемые параметры функцией KP.search
KP.search возвращает список элементов, которые имеют следующие параметры:
* ID фильма на КиноПоиске - `self.kp_id`
* Название фильма на языке оригинала - `self.name`
* Название фильма на русском языке - `self.ru_name`
* Год премьеры фильма - `self.year` (В случае получения сериала возвращается год выхода первой серии) 
* Продолжительность фильма - `self.duration`
* Список с жанрами - `self.genres`
* Список с странами - `self.countries`
* Оценка на КиноПоиске - `self.kp_rate`
* Ссылка на фильм на КиноПоиске - `self.kp_url`
* Ссылка на изображение постера - `self.poster`
* Уменьшенное изображение постера - `self.poster_preview`

## Получение Топ-500 КиноПоиска
```python
from kinopoisk_api import KP

kinopoisk = KP(token='Push your token here')

top500 = kinopoisk.top500()

for item in top500:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
```

### Возвращаемые параметры функцией KP.top500
KP.top500 возвращает список элементов, которые имеют следующие параметры:
* ID фильма на КиноПоиске - `self.kp_id`
* Название фильма на языке оригинала - `self.name`
* Название фильма на русском языке - `self.ru_name`
* Год премьеры фильма - `self.year` (В случае получения сериала возвращается год выхода первой серии) 
* Продолжительность фильма - `self.duration`
* Список с жанрами - `self.genres`
* Список с странами - `self.countries`
* Оценка на КиноПоиске - `self.kp_rate`
* Ссылка на фильм на КиноПоиске - `self.kp_url`
* Ссылка на изображение постера - `self.poster`
* Уменьшенное изображение постера - `self.poster_preview`
