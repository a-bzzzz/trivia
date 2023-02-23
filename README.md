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

### 3. palautus

Sovelluksesta on tehty peli perustoiminnoilla. Admin-käyttäjän toimintoja (pl. salasanavaihto) sekä statistiikkaa puuttuu (mutta mahdollisuuksien mukaan vielä tulossa).

#### Käytössä olevat toiminnot
- Käyttäjä voi rekisteröityä eli luoda peruskäyttäjän tunnukset
- Sovellus luo tietokantaan automaattisesti hallinnoijan eli admin-käyttäjän, jos ei ole vielä luotu
  - Admin-käyttäjän käyttäjätunnus on *admin* ja (aloitus)salasana on *salasana*
  - **Muista vaihtaa admin-käyttäjän salasana omaksi salasanaksesi!**
- Sovellukseen voi kirjautua, jos on käyttäjätunnukset -> käyttäjän tiedot tallentuvat tietokantaan
- Voi aloittaa uuden pelin -> uuden pelin tiedot tallentuvat tietokantaan
- Voi valita pelikategorian ja tason, jolle on lisätty kysymyksiä ja vastauksia - muilla valinnoilla peli päätyy tilailmoitukseen
- Peliin voi lisätä tietokannan kautta 16 kysymystä vastauksineen (ei aivan kaikista kategoria-taso-yhdistelmistä, mutta kannattaa käyttää kokeilemiseen kategoriaa 6 - satunnainen aihe)
- Voi hakea aiemmin luodut pelit listana, valita niistä yhden ja jatkaa sen pelaamista
- Voi listata aiemmat pelinsä myös pelin poistamista varten
  - Käytännössä peli poistetaan näkyvistä (visible = False), eikä se tule näkyviin hauissa, eli peli ei poistu tietokannasta
- Peli näyttää käyttäjän tunnuksen (nimen), pelinumeron, valitun kategorian ja vaikeustason, pelikerran, vastausmäärän ja pisteet
- Voi siirtyä kysymysosioon ja valita jonkin kolmesta vastausvaihtoehdoista
- Sovellus antaa palautetta siitä, onko vastaus oikein vai väärin
- Oikeasta vastauksesta saa pelitason mukaisen määrän pisteitä, jotka lisätään pelin pistesaldoon
- Jos kyseiseen peliin on vastaamattomia kysymyksiä, voi valita uuden kysymyksen - muuten voi aloittaa uuden pelin
- Samassa pelissä (samalla pelikerralla) ei voi vastata useammin samaan kysymykseen
- Näkymistä voi palata takaisin päin johonkin aiempaan vaiheeseen
- Sovelluksesta voi kirjautua ulos
- Käyttäjä voi vaihtaa oman salasanansa
- Admin-käyttäjä voi vaihtaa kaikkien käyttäjien salasanan
  - Adminin ei tarvitse tietää oikeaa salasanaa vaihtamiseen, vaan voi kirjoittaa ensimmäiseen salasanakenttään mitä tahansa, uusi salasana määräytyy toisen salasanakentän perusteella
- Admin-käyttäjä voi lisätä uusi kysymyksiä sekä niihin vastausvaihtoehtoja (3, joista yksi on oikea vastaus) suoraan sovelluksesta
  - Lisäykset päivittyvät tietokantatauluihin questions, answers ja questions_answers (aputaulu, joka linkittää kysymykseen sen vastausvaihtoehdot)
- Pelin tiedot kirjautuvat tietokannan tauluhin games ja games_questions
- Syötteet viedään tietokantaan parametreilla (estää SQL-injektion)
- Syötteet näytetään selaimen sivulla käyttämällä Jinja-sivupohjia (estää XSS-haavoittuvuuden)
- CSRF-token luodaan ohjelmassa ja se tarkistetaan soveltuvissa kohdissa
- Ympäristömuuttujat ovat käytössä (ei aitoja salasanoja GitHubissa, paitsi että admin-käyttäjän luomista varten on ns. aloitussalasana, joka tulisi vaihtaa varsinaiseen salasanaan)

**HUOMAA**, että peliä varten tarvittavat roolien (roles), kategorioiden (categories), tasojen (levels) sekä (alustavan) 16 kysymys-vastaus-setin (answers / questions / questions_answers) INSERT-komennot löytyvät ylempää kohdasta [Sovelluksen rakenne - Tietokanta - Vakioattribuutit](https://github.com/a-bzzzz/trivia/blob/main/README.md#vakioattribuutit) linkkien takaa löytyvistä tiedostoista.

#### Puuttuvat toiminnot
- Sovelluksesta ei voi muuttaa tai poistaa muita käyttäjän tietoja    *(optio)*  (pl. salasanan voi vaihtaa)
- Sovelluksesta ei voi muuttaa tai poistaa yksittäisen pelin tietoja, vastauskategoroita tai -luokkia    *(optio)*  (pl. käyttäjä voi poistaa oman pelinsä näkyvyyden, mutta ei voi poistaa tietokannasta)
- Sovelluksesta ei voi muuttaa tai poistaa kysymyksiä ja vastauksia    *(optio)*
- Pelaaja ei näe vielä statistiikkaa liittyen kaikkien pelaajien pelitilanteeseen (ranking)  *(optio)* , ja oman pistesaldon tarkistamiseen tarvitaan vielä lisätoiminto (kysymys-vastaus-sivulla omat pisteet ja muu omaan peliin liittyvä tilasto kyllä näkyy)
- Käyttäjän oikeuksien määrittely eri sivuille on alkuvaiheessa (koska käytössä on vasta rooli "peruskäyttäjä", mutta salasanan vaihdossa on jo huomioitu adminille laajemmat oikeudet)
- Käyttäjän syötteen oikeellisuutta ei mahdollisesti ole tarkistettu tarkkaan ihan kaikissa tapauksissa
- Käytettävyyteen ja saavutettavuuteen liittyviä seikkoja ei ole tarkistettu
- Ulkoasun suunnittelu on aivan alkuvaiheessa, CSS-tiedostosta on luotu pohja, valmista ulkoasukirjastoa ei ole käytössä
- Optiot - *(optio)* - eivät ole käytössä
  
**HUOMAA**, että *(optio)* -merkinnällä merkityt ominaisuudet eivät välttämättä ehdi valmistua peliin tämän kurssin aikana, mutta niitä toimintoja voi halutessaan itse lisätä peliin mukaan.
