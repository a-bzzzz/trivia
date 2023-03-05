# TRIVIA-tietovisa
HY, tsoha k2023

Sovelluksella voi pelata tietokilpailua eli vastata sovelluksen esittämiin kysymyksiin eri kysymysluokissa ja vaikeustasoissa.

## SISÄLLYS

[Sovelluksen keskeiset toiminnot ja tiedot](https://github.com/a-bzzzz/trivia/blob/main/README.md#sovelluksen-keskeiset-toiminnot-ja-tiedot)

- [Käyttäjätasot](https://github.com/a-bzzzz/trivia/blob/main/README.md#k%C3%A4ytt%C3%A4j%C3%A4tasot)

- [Pelitoiminnot](https://github.com/a-bzzzz/trivia/blob/main/README.md#pelitoiminnot-perusk%C3%A4ytt%C3%A4j%C3%A4)

- [Käyttäjätietojen hallinnointi](https://github.com/a-bzzzz/trivia/blob/main/README.md#k%C3%A4ytt%C3%A4j%C3%A4tietojen-hallinnointi)

- [Pelitietojen hallinnointi](https://github.com/a-bzzzz/trivia/blob/main/README.md#pelitietojen-hallinnointi)

- [Kysymysluokat ja pelitasot](https://github.com/a-bzzzz/trivia/blob/main/README.md#kysymysluokat-ja-pelitasot)


[Ohjeet](https://github.com/a-bzzzz/trivia/blob/main/README.md#ohjeet)

- [Sovelluksen käynnistys](https://github.com/a-bzzzz/trivia/blob/main/README.md#sovelluksen-k%C3%A4ynnistys)

- [Käyttöohjeet](https://github.com/a-bzzzz/trivia/blob/main/README.md#k%C3%A4ytt%C3%B6ohjeet)


[Sovelluksen rakenne](https://github.com/a-bzzzz/trivia/blob/main/README.md#sovelluksen-rakenne)

- [Sovelluslogiikka](https://github.com/a-bzzzz/trivia/blob/main/README.md#sovelluslogiikka)

- [Käyttöliittymä (GUI)](https://github.com/a-bzzzz/trivia/blob/main/README.md#k%C3%A4ytt%C3%B6liittym%C3%A4-gui)

- [Tietokanta](https://github.com/a-bzzzz/trivia/blob/main/README.md#tietokanta)


[Tilatieto ja muu info](https://github.com/a-bzzzz/trivia/blob/main/README.md#tilatieto-ja-muu-info)

- [Loppupalautus](https://github.com/a-bzzzz/trivia/blob/main/README.md#kohti-loppupalautusta)


## Sovelluksen keskeiset toiminnot ja tiedot

### Käyttäjätasot

#### Vierailija    *(optio)*
Vierailija voi kokeilla pelin käyttämistä ilman käyttäjätunnusta ja salasanaa.  
Vierailijan peleistä ei tallennu pisteitä tai mitään pelaaja- tai tilastotietoja.  

#### Peruskäyttäjä (lyhyemmin: käyttäjä)
Käyttäjä voi luoda käyttäjätunnuksen ja salasanan, ns. pääsytiedot. Tämä on ns. perustaso, jonka jokainen käyttäjä voi saavuttaa rekisteröitymällä.
Käyttäjä voi kirjautua sisään sovellukseen voimassa olevalla käyttäjätunnuksella ja salasanalla.  

#### Ylläpitäjä (admin)
Peruskäyttäjän oikeuksien lisäksi ylläpitäjä voi lisätä peliin uusia kysymyksiä ja vastauksia. 
Admin-käyttäjä pääsee vaihtamaan kaikkien käyttäjien salasanoja.
Admin voisi mahdollisesti myös muokata (lisätä/poistaa/muuttaa) käyttäjätietoja, sekä pelin tietoja, kuten kysymyksiä ja luokkia.     *(optio)* 
Peliin luodaan (julkaistavaan sovellukseen on luotu) ensimmäisellä pelikerralla admin-käyttäjä, jolle
```
käyttäjätunnus : admin 
salasana       : salasana
```
**Muista vaihtaa admin-käyttäjän salasana omaksi salasanaksesi, jos luot näistä elementeistä oman pelisi!**

#### Superuser *(optio)*
Superkäyttäjä voisi saada peruskäyttäjän oikeuksien lisäksi joitakin erityisoikeuksia pelin kehittelyssä, mutta ei oikeuksia toisten käyttäjien tietojen käsittelyyn, kuten admin-user. Esim. kun peruskäyttäjä saa kerättyä tietyn määrän pelipisteitä, hänen käyttäjätasonsa nousee superuser-tasolle. Silloin hän saisi mahdollisuuden lisätä peliin uusia kysymyksiä ja vastauksia, sekä ansaita lisää pisteitä, jos ne lisäykset kehittävät peliä.

### Pelitoiminnot (peruskäyttäjä)

Pelaamista, tai peliensä hallintaa, varten käyttäjä voi valita seuraavat vaihtoehdot:  
* Aloita **uusi peli** (ainoa vaihtoehto ensimmäisessä pelissä)  
  - pelaajan tulostilasto alkaa nollasta  
* **Jatka** aiemmin aloitettua peliä  
  - uudet pisteet lisätään aiempiin pisteisiin  
* **Poista** olemassa oleva peli
* **Hae** omia aiempia pelejä joko pelaamista tai poistamista varten
* **Tarkista** pelin kysymysten loputtua päättyneen pelin piste- ja muut tiedot
* **Hae pelitilasto**, jossa näkyy omat parhaat pelit, kaikki parhaat pelit (ranking/tuloslista) sekä oman parhaan pelin sijoitus kaikkien pelien joukossa (pl. pelit, joiden pistesaldo on nolla, tai mahdollisesti pelin jossain pelin kehitysvaiheessa jopa negatiivinen)  

Vastauksen jälkeen pelaaja saa palautetta siitä, oliko vastaus oikein vai väärin.   
Pelaaja kerää pisteitä oikeilla vastauksilla vaikeustason mukaan.   
Pelaaja voi seurata omaa tulossaldoa pelin aikana.  
Pelaaja voi lopettaa pelaamisen ja kirjautua ulos sovelluksesta.

### Käyttäjätietojen hallinnointi

Peruskäyttäjä voi vaihtaa oman salasanansa.

Admin-käyttäjä voi vaihtaa kaikkien käyttäjien salasanan, ilman että tarvitsee tietää voimassaolevaa salasanaa (admin voi kirjoittaa 1. salasanakenttään mitä tahansa, uusi salasana määräytyy 2. salasanakentän mukaan).

### Pelitietojen hallinnointi

Admin-käyttäjä voi lisätä peliin uusia kysymyksiä ja vastausvaihtoehtoja.
Admin-käyttäjälle voisi lisätä muitakin pelin muokkaus- ja kehitysmahdollisuuksia (esim. lisätä ja poistaa kategorioita).

### Kysymysluokat ja pelitasot

Uutta peliä varten pelaaja voi valita:   
* kysymyskategorian   
  1 - tiede/maantiede   
  2 - historia    
  3 - urheilu/vapaa-aika/ruoka   
  4 - musiikki/taide/kirjallisuus   
  5 - elokuvat/TV/viihde   
  6 - satunnainen aihe   
* vaikeustason   
  1 - helppo   
  2 - keskitaso   
  3 - vaikea   

## Ohjeet

### Sovelluksen käynnistys

Pelin voi aloittaa kopioimalla seuraavan linkin (sivuosoitteen) selaimen URL-kenttään:
```
tsoha-trivia.fly.dev
```
Jos saat sivulta virheilmoituksen, kokeile ladata sivu uudelleen. Huomioithan, että sovellus on ladattu ulkoisen palveluntarjoajan palvelimelle, joten mahdollinen häiriö saattaa aiheutua myös ulkoisista syistä - siis yritä myöhemmin uudelleen!

Täällä tarkemmin käynnistysohjeita mm. omaksi kopioidulle sovellukselle: [Startup Guide](https://github.com/a-bzzzz/trivia/blob/main/documentation/Startup-guide.md)

### Käyttöohjeet

Sovelluksen käyttöohjeet peruskäyttäjälle: [Manual](https://github.com/a-bzzzz/trivia/blob/main/documentation/Manual.md)

## Sovelluksen rakenne

### Sovelluslogiikka

Sovelluksen logiikka on koodattu Python-ohjelmointikielellä. Sovelluskansion juuresta löytyvät Python-tiedostot:
- app.py                : käynnistystiedosto, jossa määritelty alustavasti Flask ja ympäristömuuttujat
- db.py                 : tietokantayhteyden osoite sekä tarvittavat kirjastot
- games.py              : pelitoimintojen kannalta oleelliset funktiot
- questions_answers.py  : kysymysten ja vastausten käsittelyyn liittyvät funktiot
- routes.py             : lomakkeiden käsittelyssä ja pelin navigoinnissa tarvittavat funktiot
- users.py              : käyttäjätietojen käsittelyssä tarvittavat funktiot

### Käyttöliittymä (GUI)

Sovellukseen on rakennettu graafinen käyttöliittymä HTML-tiedostoista, joissa on hyödynnetty Pythoniin kuuluvan Flask-kirjaston Jinja-sivupohjia. Lisäksi sovellus on viety Fly.io -palvelun tuotantoympäristöön. Niinpä sovelluksen voi käynnistää CLI:ssä (komentoriviltä) molemmilla tavoilla, mutta db.py -tiedostoon tarvitaan eri osoitemääritykset (kommentoi ulos tai poista väärä rivi):
```
         komento     db.py:  riviteksti          
Fly.io : fly open    ->  5:  app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)
Flask  : flask run   ->  6:  app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
```

#### Käyttöliittymän rakenne
HTML-lomakkeet ja navigointi: [GUI-navigointi-kaavio](https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-navi_chart.png)

### Tietokanta

Harjoitustyötä varten tietokanta on toteutettu Docker-containerin postgresql-kuvalla, mutta voit toki asentaa itsellesi PostgreSQL-tietokannan muillakin tavoin sovelluksen käyttöä varten. Tietokantayhteydet kuitenkin määritellään ja käynnistetään eri tavoin riippuen siitä käynnistääkö sovelluksen Flaskilla vai Fly.io:lla.

#### Tietokannan rakenne
Tietokantataulut ja niiden väliset yhteydet: [Tietokantakaavio](https://github.com/a-bzzzz/trivia/blob/main/documentation/db_structure.png)

#### Vakioattribuutit
Tietokannan käyttöä varten tarvittavat INSERT-kommennot löytyvät näistä tiedostoista:
* Tietokantataulujen luominen: 					                        [schema.sql](https://github.com/a-bzzzz/trivia/blob/main/schema.sql)
* Käyttäjäroolien lisäys: 					                            [roles.sql](https://github.com/a-bzzzz/trivia/blob/main/roles.sql)
* Kysymysluokkien (kategorioiden) lisäys: 			                [categories.sql](https://github.com/a-bzzzz/trivia/blob/main/categories.sql)
* Pelin vaikeustasojen lisäys: 					                        [levels.sql](https://github.com/a-bzzzz/trivia/blob/main/levels.sql)
* Muutaman kysymys-vastaussetin lisäys (suoraan tietokantaan): 	[questions.sql](https://github.com/a-bzzzz/trivia/blob/main/questions.sql)
    
## Tilatieto ja muu info

### Loppupalautus

Peliin on lisätty perustoiminnot sekä muutama optioksi aiottu ominaisuus.
Pelin toimintojen sekä koodin laadun lisäksi myös ulkoasua on päivitetty. 

#### Käytössä olevat toiminnot
- Käyttäjä voi rekisteröityä eli luoda peruskäyttäjän tunnukset
- Sovellus luo tietokantaan automaattisesti hallinnoijan eli admin-käyttäjän
- Sovellukseen voi kirjautua, jos on käyttäjätunnukset -> käyttäjän tiedot tallentuvat tietokantaan
- Voi aloittaa uuden pelin -> uuden pelin tiedot tallentuvat tietokantaan
- Voi valita pelikategorian ja tason, jolle on lisätty kysymyksiä ja vastauksia - muilla valinnoilla peli päätyy tilailmoitukseen
- Peliin voi lisätä tietokannan kautta 16 valmiiksi annettua kysymystä vastauksineen (ei aivan kaikista kategoria-taso-yhdistelmistä, mutta kannattaa käyttää kokeilemiseen kategoriaa 6 - satunnainen aihe)
- Voi hakea aiemmin luodut pelit listana, valita niistä yhden ja jatkaa sen pelaamista
- Voi listata aiemmat pelinsä myös pelin poistamista varten
  - Käytännössä peli poistetaan näkyvistä (visible = False), eikä se tule näkyviin hauissa, eli peli ei poistu tietokannasta
- Peli näyttää käyttäjän tunnuksen (nimen), pelinumeron, valitun kategorian ja vaikeustason, pelikerran, vastausmäärän ja pisteet
- Voi siirtyä kysymysosioon ja valita jonkin kolmesta vastausvaihtoehdoista
- Sovellus antaa palautetta siitä, onko vastaus oikein vai väärin
- Oikeasta vastauksesta saa pelitason mukaisen määrän pisteitä, jotka lisätään pelin pistesaldoon
- Jos kyseiseen peliin on vastaamattomia kysymyksiä, voi valita uuden kysymyksen - muuten voi aloittaa uuden pelin
- Samassa pelissä (samalla pelikerralla) ei voi vastata useammin samaan kysymykseen
- Näkymistä voi palata takaisin päin johonkin aiempaan vaiheeseen, tai joissakin tapauksissa aloitussivulle
- Pelaaja näkee kysymys-vastaus-sivulla omat pisteensä sekä muun omaan peliin liittyvän tilaston
- Pelaaja näkee statistiikkaa liittyen omiin parhaimpiin peleihinsä
- Pelaaja näkee statistiikkaa liittyen kaikkien pelaajien pelitilanteeseen (ranking/pelitilasto)
- Sovelluksesta voi kirjautua ulos
- Käyttäjä voi vaihtaa oman salasanansa
- Käyttäjän oikeuksia on määritelty tasojen peruskäyttäjä ja admin mukaisesti
  - Salasanan vaihdossa on jo huomioitu adminille laajemmat oikeudet
  - Admin-käyttäjä pääsee kysymysten ja vastausten lisäyssivulle, mutta muilla ei ole sinne pääsyä
  - Admin-käyttäjä voi lisätä uusi kysymyksiä sekä niihin vastausvaihtoehtoja (3, joista yksi on oikea vastaus) suoraan sovelluksesta
  - Lisäykset päivittyvät tietokantatauluihin questions, answers ja questions_answers (aputaulu, joka linkittää kysymykseen sen vastausvaihtoehdot)
  - Admin-käyttäjä voi vaihtaa kaikkien käyttäjien salasanan
  - Adminin ei tarvitse tietää oikeaa salasanaa vaihtamiseen, vaan voi kirjoittaa ensimmäiseen salasanakenttään mitä tahansa, uusi salasana määräytyy toisen salasanakentän perusteella
- Pelin tiedot kirjautuvat tietokannan tauluhin games ja games_questions
- Syötteet viedään tietokantaan parametreilla (estää SQL-injektion)
- Syötteet näytetään selaimen sivulla käyttämällä Jinja-sivupohjia (estää XSS-haavoittuvuuden)
- CSRF-token luodaan ohjelmassa ja se tarkistetaan soveltuvissa kohdissa
- Ympäristömuuttujat ovat käytössä (ei aitoja salasanoja GitHubissa, paitsi että admin-käyttäjän luomista varten on ns. aloitussalasana, joka tulisi vaihtaa varsinaiseen salasanaan)
- Ulkoasun yhtenäinen tyyli on luotu muokkaamalla soveltuvasti valmista CSS-pohjaa, yhdistämällä siihen oma layout.html -tiedosto sekä rakentamalla HTML-lomakkeille elementtejä mahdollisimman yhtenäisesti
  - static-kansiosta löytyy myös pari vaihtoehtoista CSS-tyylitiedostoa, jotka ovat harjoitelmia aiheesta

**HUOMAA**: Peliä varten tarvittavat roolien (roles), kategorioiden (categories), tasojen (levels) sekä (alustavan) 16 kysymys-vastaus-setin (answers / questions / questions_answers) INSERT-komennot löytyvät ylempää kohdasta [Sovelluksen rakenne - Tietokanta - Vakioattribuutit](https://github.com/a-bzzzz/trivia/blob/main/README.md#vakioattribuutit) linkkien takaa löytyvistä tiedostoista.

#### Puuttuvat toiminnot *(optio)*
- Sovelluksesta ei voi muuttaa tai poistaa käyttäjän tietoja (pl. salasanan voi vaihtaa)
- Sovelluksesta ei voi muuttaa tai poistaa yksittäisen pelin tietoja, vastauskategoroita tai -luokkia (pl. käyttäjä voi poistaa oman pelinsä näkyvyyden, mutta ei voi poistaa tietokannasta)
- Sovelluksesta ei voi muuttaa tai poistaa kysymyksiä ja vastauksia
- Saavutettavuuteen liittyviä seikkoja ei ole päästy tarkistamaan soveltuvan työkalun puuttuessa
  
**MUISTUTUS**: *(optio)* -merkintä tarkoittaa sitä, että ne ominaisuudet eivät valmistu (valmistuneet) peliin ko. kurssin aikana, mutta niitä toimintoja voi halutessaan itse lisätä peliin mukaan - tai muuten jatkokehittää peliä omien mieltymysten mukaan.
