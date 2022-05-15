# Käyttöohje

Lataa viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.
HUOM: Komennot tulee suorittaa python-strenght-training-app -kansiossa.

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

