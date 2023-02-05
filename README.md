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

Tietokantataulut ja niiden väliset yhteydet: [Tietokantakaavio](https://github.com/a-bzzzz/trivia/blob/main/documentation/db_structure.png)  
    
## Tilatieto ja muu info

### 2. palautus

Sovelluksesta on tehty pienin mahdollinen peli.

#### Käytössä olevat toiminnot
- Käyttäjä voi rekisteröityä eli luoda peruskäyttäjän tunnukset
- Sovellukseen voi kirjautua, jos on käyttäjätunnukset -> käyttäjän tiedot tallentuvat tietokantaan
- Voi aloittaa uuden pelin -> uuden pelin tiedot tallentuvat tietokantaan
- Voi valita vain pelikategorian 1 ja tason 1, muilla valinnoilla peli päätyy virhetilanteeseen
- Pelissä on siis vasta yksi kysymys (kategoriassa 1, tasolla 1)
- Peli näyttää käyttäjän tunnuksen (nimen), valitun kategorian ja tason
- Voi siirtyä kysymysosioon ja valita jonkin kolmesta vastausvaihtoehdoista
- Sovellus antaa palautetta siitä, onko vastaus oikein vai väärin
- Näkymistä voi (enimmäkseen) palata takaisin päin johonkin aiempaan vaiheeseen
- Sovelluksesta voi kirjautua ulos
- Syötteet viedään tietokantaan parametreilla (estää SQL-injektion)
- Syötteet näytetään selaimen sivulla käyttämällä Jinja-sivupohjia (estää XSS-haavoittuvuuden)
- Ympäristömuuttujat ovat käytössä (ei salasanoja GitHubissa)
**HUOMAA**, että [schema.sql](https://github.com/a-bzzzz/trivia/blob/main/schema.sql) -tiedostosta löytyvät peliä varten tarvittavat roolien (roles), kategorioiden (categories), tasojen (levels) ja ensimmäisen kysymys-vastaus-setin (answers / questions / questions_answers) INSERT-komennot

#### Puuttuvat toiminnot
- Ei voi jatkaa aiemmin luotua peliä
- Ei voi poistaa olemassa olevaa peliä
- Ei voi valita kategorioita 2-6 eikä tasoja 2-3 (toki mahdollista sitten, kun peliin on tallennettu lisää kysymyksiä ja vastauksia eri kategorioihin ja eri tasoille)
- Ei voi valita uutta kysymystä -> peli ei huomioi, mihin kysymyksiin on jo vastattu
- Ei saa pistettä oikeasta vastauksesta -> ei voi seurata pelin tulossaldoa
- Kaikkia virhetilanteita ei ole vielä otettu kiinni
- Sovelluksesta ei voi muuttaa tai poistaa käyttäjän tietoja
- Sovelluksesta ei voi muuttaa tai poistaa pelin tietoja, vastauskategoroita tai -luokkia
- Sovelluksesta ei voi lisätä, muuttaa tai poistaa kysymyksiä ja vastauksia
- Käyttäjän oikeuksia eri sivuille ei ole määritelty
- Käyttäjän syötteen oikeellisuutta ei ole tarkistettu kaikissa tapauksissa
- CSRF-token on lisäämättä
- Käytettävyyteen ja saavutettavuuteen liittyviä seikkoja ei ole tarkistettu
- Ulkoasun suunnittelu aivan alkuvaiheessa, CSS-tiedostosta on luotu pohja, valmista ulkoasukirjastoa ei ole käytössä
- Optiot - *(optio)* - eivät ole käytössä
  
**HUOMAA**, että *(optio)* -merkinnällä merkityt ominaisuudet eivät välttämättä ehdi valmistua peliin tämän kurssin aikana, mutta niitä voi lisätä peliin jatkossa mahdollisuuksien mukaan.
