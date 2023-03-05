## KÄYNNISTYSOHJEET

### 1. Sovellus omalla koneella, käynnistys CLI:ssä ```Flask```illa

#### Tiedostot
Kloonaa trivia-repositorio koneellesi ( [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) ).

Siirry repositorion juurikansioon ja luo sinne ```.env``` -tiedosto, jolle seuraavanlaiset määritykset (lisää oman tietokantasi osoite ja salainen avain):
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
#### Virtuaaliympäristö
Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komentoriviltä:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```

#### Tietokanta
```PostgreSQL```-tietokanta tulee olla käytössä (asennettuna) jollakin tavalla, 
esim. HY:n fuksiläppäreille seuraavan ohjeen mukaisesti (tsoha-kurssin ohjeet): 
https://github.com/hy-tsoha/local-pg tai Docker-containerina:  [How to deploy postgresql as a docker container](https://www.howtogeek.com/devops/how-to-deploy-postgresql-as-a-docker-container/) 

Ota käyttöön trivia-sovelluksen tietokantaskeema:
```
$ psql < schema.sql
```
Lisää tietokantaan seuraavat:
```
$ psql < roles.sql
```
```
$ psql < categories.sql
```
```
$ psql < levels.sql
```
```
$ psql < questions.sql
```

Käynnistys komentoriviltä:
```
$ flask run
```
Oman sovelluksen ensimmäisellä käynnistyskerralla sovellus luo tietokantaan ```admin```-käyttäjän aloitussalasanalla ```salasana```. 

**Muista vaihtaa omaan sovellukseesi oma salasanasi admin-käyttäjälle!**

### 2. Sovellus omalla koneella ja viety itse tuotantoon Fly.io -palvelussa

Ensin suoritetaan samat vaiheet kuin 1. vaihtoehdossa käynnistyskomentoon asti: perusta tietokanta, kopio tiedostot.

Kun sovellusympäristö on valmiina omalla koneella, suoritetaan tuotantoon vieminen (tsoha-kurssin ohjeet): [Sovellus tuotantoon](https://hy-tsoha.github.io/materiaali/osa-3/#sovellus-tuotantoon) 

Fly.io -palvelu: [Fly.io](https://fly.io/)

Käynnistys komentoriviltä:
```
$ fly open
```

### 3. Käynnistys ```Fly.io``` -palvelusta ilman asennusta omalle koneelle

Avaa selaimeesi välilehti. Suositeltava selain tietokoneella: ```Firefox```

Voit kokeilla pelaamista myös mobiililaitteella.

Pelin voi aloittaa kopioimalla seuraavan linkin (sivuosoitteen) selaimen URL-kenttään:
```
tsoha-trivia.fly.dev
```
Jos saat sivulta virheilmoituksen, kokeile ladata sivu uudelleen. 

Huomioithan, että sovellus on ladattu ulkoisen palveluntarjoajan palvelimelle, joten mahdollinen häiriö saattaa aiheutua myös ulkoisista syistä - siis yritä myöhemmin uudelleen!
