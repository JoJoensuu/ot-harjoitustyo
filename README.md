# Strenght training app

Sovelluksen avulla käyttäjä voi luoda itselleen harjoituspäiviä, joihin voi tallentaa erilaisia harjoituksia.

Kuntosaliharjoitusten tapauksessa käyttäjä voi lisätä harjoitukseen sarjat, toistomäärät, palautumisajat, sekä tekstimuotoisia kommentteja.
Käyttäjä näkee kuntosaliikkeen kohdalla kyseisen liikkeen edellisten harjoitusten sarjapainot.

## Tehtävät

[Vaatimusmäärittely](https://github.com/JoJoensuu/ot-harjoitustyo/blob/master/python-strenght-training-app/Dokumentaatio/vaatimusmaarittely.md)

[Työajanseuranta](https://github.com/JoJoensuu/ot-harjoitustyo/blob/master/python-strenght-training-app/Dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/JoJoensuu/ot-harjoitustyo/blob/master/python-strenght-training-app/Dokumentaatio/changelog.md)

## Asennus

1. Asenne riippuvuudet komennolla:

```
poetry install
```
2. Suorita vaadittavat alustustoimenpiteet komennolla:

```
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```

### Testaus
Testit suoritetaan komennolla:

```
poetry run invoke test
```

### Testikattavuus
Testikattavuusraportin voi generoida komennolla:

```
poetry run invoke coverage-report
```
