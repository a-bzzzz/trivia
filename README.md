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

Tietokantataulut ja niiden väliset yhteydet on alustavasti suunniteltu seuraavasti: [Tietokantakaavio](https://github.com/a-bzzzz/trivia/blob/main/documentation/db_structure.png)  
    
## Tilatieto ja muu info

Sovellus on suunnitteluvaiheessa.  
  
**HOX!**     *(optio)* -merkinnällä merkityt ominaisuudet eivät välttämättä ehdi valmistua peliin tämän kurssin aikana, mutta niitä voi lisätä peliin jatkossa mahdollisuuksien mukaan.
