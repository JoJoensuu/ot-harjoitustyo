# Käyttöohje

Lataa viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Konfigurointi

Tiedostot luodaan automaattisesti data-hakemistoon, jos niitä ei siellä vielä ole.

## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:
```
poetry install
```
Jonka jälkeen suorita alustustoimenpiteet komennolla:
```
poetry run invoke build
```
Nyt ohjelman voi käynnistää komennolla:
```
poetry run invoke start
```

