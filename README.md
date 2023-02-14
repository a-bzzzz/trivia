# TRIVIA-tietovisa
HY, tsoha k2023

Sovelluksella voi pelata tietokilpailua eli vastata sovelluksen esittämiin kysymyksiin eri kysymysluokissa ja vaikeustasoissa.  

## Sovelluksen keskeiset toiminnot ja tiedot

### Käyttäjätasot

#### Vierailija    *(optio)*
Vierailija voi kokeilla pelin käyttämistä ilman käyttäjätunnusta ja salasanaa.  
Vierailijan peleistä ei tallennu pisteitä tai mitään pelaaja- tai tilastotietoja.  

#### Peruskäyttäjä (lyhyemmin: käyttäjä)
Käyttäjä voi luoda käyttäjätunnuksen ja salasanan, ns. pääsytiedot.   
Käyttäjä voi kirjautua sisään sovellukseen voimassa olevalla käyttäjätunnuksella ja salasanalla.  

#### Ylläpitäjä (admin)    *(optio)*
Peruskäyttäjän oikeuksien lisäksi ylläpitäjä voi muokata (lisätä/poistaa/muuttaa) käyttäjätietoja ja pelin tietoja, kuten kysymyksiä ja luokkia.  

### Pelaajatoiminnot (peruskäyttäjä)

Pelaamista, tai peliensä hallintaa, varten käyttäjä voi valita seuraavat vaihtoehdot:  
* Aloita **uusi peli** (ainoa vaihtoehto ensimmäisessä pelissä)  
  - pelaajan tulostilasto alkaa nollasta  
* **Jatka** aiemmin aloitettua peliä  
  - uudet pisteet lisätään aiempiin pisteisiin  
* **Poista** olemassa oleva peli  

Vastauksen jälkeen pelaaja saa palautetta siitä, oliko vastaus oikein vai väärin.   
Pelaaja kerää pisteitä oikeilla vastauksilla vaikeustason mukaan.   
Pelaaja voi seurata omaa tulossaldoa pelin aikana.  
Pelaaja näkee tuloslistalta (ranking) pistemääränsä verrattuna muiden pelaajien pisteisiin, eli sijoituksen pelissä.    *(optio)*  
Pelaaja voi lopettaa pelaamisen ja kirjautua ulos sovelluksesta.   

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

## Sovelluksen rakenne

### Tietokanta

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

### 2. palautus

Sovelluksesta on tehty pienin mahdollinen peli.

#### Käytössä olevat toiminnot
- Käyttäjä voi rekisteröityä eli luoda peruskäyttäjän tunnukset
- Sovellukseen voi kirjautua, jos on käyttäjätunnukset -> käyttäjän tiedot tallentuvat tietokantaan
- Voi aloittaa uuden pelin -> uuden pelin tiedot tallentuvat tietokantaan
- Voi valita pelikategorian ja tason, jolle on lisätty kysymyksiä ja vastauksia - muilla valinnoilla peli päätyy tilailmoitukseen
- Peliin voi lisätä tietokannan kautta 16 kysymystä vastauksineen (ei aivan kaikista kategoria-taso-yhdistelmistä, mutta kannattaa käyttää kokeilemiseen kategoriaa 6 - satunnainen aihe)
- Peli näyttää käyttäjän tunnuksen (nimen), pelinumeron, valitun kategorian ja vaikeustason, pelikerran, vastausmäärän ja pisteet
- Voi siirtyä kysymysosioon ja valita jonkin kolmesta vastausvaihtoehdoista
- Sovellus antaa palautetta siitä, onko vastaus oikein vai väärin
- Oikeasta vastauksesta saa pelitason mukaisen määrän pisteitä, jotka lisätään pelin pistesaldoon
- Jos kyseiseen peliin on vastaamattomia kysymyksiä, voi valita uuden kysymyksen - muuten voi aloittaa uuden pelin
- Samassa pelissä ei voi vastata useammin samaan kysymykseen
- Näkymistä voi palata takaisin päin johonkin aiempaan vaiheeseen
- Sovelluksesta voi kirjautua ulos
- Pelin tiedot kirjautuvat tietokannan tauluhin games ja games_questions
- Syötteet viedään tietokantaan parametreilla (estää SQL-injektion)
- Syötteet näytetään selaimen sivulla käyttämällä Jinja-sivupohjia (estää XSS-haavoittuvuuden)
- Ympäristömuuttujat ovat käytössä (ei salasanoja GitHubissa)

**HUOMAA**, että peliä varten tarvittavat roolien (roles), kategorioiden (categories), tasojen (levels) sekä (alustavan) 16 kysymys-vastaus-setin (answers / questions / questions_answers) INSERT-komennot löytyvät ylempää kohdasta Sovelluksen rakenne - Tietokanta - Vakioattribuutit linkkien takaa löytyvistä tiedostoista.

#### Puuttuvat toiminnot
- Ei voi jatkaa aiemmin luotua peliä
- Ei voi poistaa olemassa olevaa peliä
- Sovelluksesta ei voi muuttaa tai poistaa käyttäjän tietoja
- Sovelluksesta ei voi muuttaa tai poistaa pelin tietoja, vastauskategoroita tai -luokkia
- Sovelluksesta ei voi lisätä, muuttaa tai poistaa kysymyksiä ja vastauksia
- Käyttäjän oikeuksia eri sivuille ei ole määritelty
- Käyttäjän syötteen oikeellisuutta ei ole tarkistettu kaikissa tapauksissa
- CSRF-token on lisäämättä
- Käytettävyyteen ja saavutettavuuteen liittyviä seikkoja ei ole tarkistettu
- Ulkoasun suunnittelu on aivan alkuvaiheessa, CSS-tiedostosta on luotu pohja, valmista ulkoasukirjastoa ei ole käytössä
- Optiot - *(optio)* - eivät ole käytössä
  
**HUOMAA**, että *(optio)* -merkinnällä merkityt ominaisuudet eivät välttämättä ehdi valmistua peliin tämän kurssin aikana, mutta niitä voi lisätä peliin jatkossa mahdollisuuksien mukaan.
