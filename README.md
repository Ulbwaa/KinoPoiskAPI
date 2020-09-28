<div align="center">
  <h1>KinoPoiskAPI</h1>
  <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoiskapiunofficial.tech/">API КиноПоиска</a></p>

  <img align="center" src="https://img.shields.io/github/repo-size/Ulbwaa/KinoPoiskAPI" alt="GitHub repo size">
  <img align="center" src="https://img.shields.io/github/stars/Ulbwaa/KinoPoiskAPI" alt="GitHub Repo stars">
  <img align="center" src="https://img.shields.io/github/watchers/Ulbwaa/KinoPoiskAPI" alt="GitHub watchers">
  <img align="center" src="https://img.shields.io/github/last-commit/Ulbwaa/KinoPoiskAPI" alt="GitHub last commit">
  <img align="center" src="https://img.shields.io/codacy/grade/7733fc868fbc4da180e781d90cb30694" alt="Codacy grade">
  <img align="center" src="https://img.shields.io/github/languages/top/Ulbwaa/KinoPoiskAPI" alt="GitHub top language">
  <img align="center" src="https://img.shields.io/website?down_message=Down&label=Kinopoisk%20Api%20Unofficial&up_message=Up&url=https%3A%2F%2Fkinopoiskapiunofficial.tech%2F" alt="API Uptime">
</div>

## Навигация

* [Начало работы](#начало-работы)
  * [Установка зависимостей](#установка-зависимостей)
  * [Получение токена KinopoiskAPI](#получение-токена-kinopoiskapi)
  * [Инициализация скрипта](#инициализация-скрипта)
* [Получение информации о фильме по ID КиноПоиска](#получение-информации-о-фильме-по-id-кинопоиска)
  * [Возвращаемые параметры функцией KP.get_film](#возвращаемые-параметры-функцией-kpget_film)
* [Поиск фильма на КиноПоиске по ключевому слову](#поиск-фильма-на-кинопоиске-по-ключевому-слову)
  * [Возвращаемые параметры функцией KP.search](#возвращаемые-параметры-функцией-kpsearch)
* [Получение Топ-500 КиноПоиска](#получение-топ-500-кинопоиска)
  * [Возвращаемые параметры функцией KP.top500](#возвращаемые-параметры-функцией-kptop500)

## Начало работы
Для работы Вам нужно установить или скачать модуль. Установить модуль можно двумя способами:
* Установка в качестве подмодуля:
```
$ git submodule add https://github.com/Ulbwaa/KinoPoiskAPI
```

* Клонирование репозитория в Ваш проект:
```
$ git clone https://github.com/Ulbwaa/KinoPoiskAPI
```

> Для удобной работы рекомендуется использовать первый способ.

### Установка зависимостей
```
$ pip install -r requirements.txt
```

### Получение токена KinopoiskAPI
Для получения токена необходима регистрация на сайте
<a href="https://kinopoiskapiunofficial.tech/signup">kinopoiskapiunofficial.tech</a>.
После регистрации перейдите в настройки своего <a href="https://kinopoiskapiunofficial.tech/user">профиля</a> и сохраните токен.

<img align="center" src="https://i.imgur.com/QkXRQ9t.png" alt="Регистрация">

### Инициализация скрипта
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

### Возвращаемые параметры функцией `KP.get_film`
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

> Для получения информации в формате dict используйте `self.__dict__`

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

### Возвращаемые параметры функцией `KP.search`
`KP.search` возвращает список элементов, которые имеют следующие параметры:
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

> Для получения информации в формате dict используйте `self.__dict__`

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

### Возвращаемые параметры функцией `KP.top500`
`KP.top500` возвращает список элементов, которые имеют следующие параметры:
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

> Для получения информации в формате dict используйте `self.__dict__`
