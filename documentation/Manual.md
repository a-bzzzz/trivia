## KÄYTTÖOHJEET


Vaihtoehtoiset käynnistysohjeet löytyvät täältä: [Startup Guide](https://github.com/a-bzzzz/trivia/blob/main/documentation/Startup-guide.md)

Sovelluksen kokeilun voit aloittaa tästä linkistä:  https://tsoha-trivia.fly.dev 

Sovelluksen käyttöohjeet peruskäyttäjälle (esim. ylläpitäjän toimintojen ohjeistus ei löydy tästä manuaalista):

### 1. Aloitussivu

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/1_home.png">

### 2. Sovellukseen kirjautuminen

Klikkaa linkkiä ```Log in – Kirjaudu```

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/2_login.png">

a) Voit kokeilla seuraavia valmiita käyttäjätunnuksia peliin tutustumista varten:

| Käyttäjätaso | Käyttäjätunnus	| Salasana |
| :--------------- | :--------------- | :--------------- |
| peruskäyttäjä	| hessu | hopo |
| ylläpitäjä | admin | salasana |

Kirjoita käyttäjätunnus kenttään ```Username – Käyttäjätunnus```

Kirjoita salasana kenttään ```Password – Salasana```

Klikkaa painiketta ```Log in – Kirjaudu```

Jos haluat lopettaa tässä vaiheessa, klikkaa painiketta ```Cancel – Lopeta```

b) Haluat varmaan luoda peliin myös omat käyttäjätunnuksesi ja salasanasi kirjautumista varten, joten käy ennen tätä vaihetta	rekisteröitymässä:
Klikkaa painiketta ```Register – Luo käyttäjätili```

### 3. Rekisteröityminen

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/3_register.png">

Kirjoita uusi käyttäjätunnuksesi kenttään ```Username – Tunnus```

Kirjoita salasana kenttään ```Password – Salasana```

Kirjoita sama salasana uudelleen kenttään ```Confirm password – Salasana uudestaan```

Klikkaa painiketta ```Create – Luo tunnus```

Voit palata takaisin aloitussivulle: klikkaa linkkiä ```Back – Takaisin```

### 4. Aloitusvalikko

Onnistuneen rekisteröitymisen tai kirjautumisen jälkeen siirryt takaisin aloitussivulle, jonne on ilmestynyt käyttäjäroolisi mukainen pelivalikko:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/4_start.png">

Ylläpitäjälle näkyy valikossa lisäksi linkki, jonka kautta pääsee lisäämään peliin kysymyksiä ja vastauksia.

Pääset kirjautumaan sovelluksesta klikkaamalla linkkiä ```Log out – Kirjaudu ulos```

Voit aloittaa uuden pelin klikkaamalla linkkiä ```Start new game – Aloita uusi peli``` (kohta 5.)

Jos sinulla on aiemmin aloitettuja pelejä, voit listata ne klikkaamalla ```Search previous game – Hae aiempi peli``` (kohta 6.)

Voit myös hakea aiemmat pelisi ja valita niistä jonkin peleistä poistettavaksi: ```Search and remove game – Hae ja poista peli``` (kohta 7.)

Pelitilastot saat klikkaamalla ```Get game statistics – Hae pelitilastot``` : 
1) omat parhaat pelisi (mikäli on pelattuja pelejä) 
2) kaikista peleistä parhaat suoritukset (ranking) 
3) oman parhaimman pelisi sijoituksen verrattuna edelliseen tuloslistaan (kohta 8.)

### 5. Pelivalikko

Aloittaaksesi uuden pelin sinun täytyy siirtyä pelivalikkoon:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/5_menu.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Pelataksesi uutta peliä klikkaamalla vaihtoehtoja valitse jokin kuudesta kysymyskategoriasta ja jokin 3 vaikeustasosta.

Aloita peli klikkaamalla painiketta ```Play – Pelaa```

#### 5.1. Pelaa

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/6_game.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Pelitiedot-taulukosta näet tähän peliin liittyvää tilastotietoa.

Lue kysymys huolellisesti ja valitse jokin vastausvaihtoehdoista klikkaamalla.

Vahvista vastauksesi klikkaamalla painiketta ```Answer – Vastaa```.

Vastauksen jälkeen saat palautetta vastauksestasi:

#### 5.2. Tarkista vastaus

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/7_check.png">

Tällä kertaa pelaaja onnistui valitsemaan oikean vastauksen :-)

Info-kentässä näkyy peliin liittyvä (teknistä) tietoa.

Hae seuraava kysymys klikkaamalla ```New question – Uusi kysymys```.

Ja jatka peli haluamasi verran, mutta korkeintaan niin kauan kuin pelissä riittää kysymyksiä valitulla kategoria-taso -yhdistelmällä.

Vastaamattomien kysymysten määrä näkyy kohdassa ```Amount of questions – Kysymysmäärä```

Tässä tapauksessa pelissä on enää yksi kysymys vastattavana.

Pelistä pääset pois aloitussivulle klikkaamalla linkkiä ```Back – Takaisin```

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/8_check_quit.png">

Nyt vastaus ei osunut aivan oikeaan :-(

Kun ko. pelistä loppuvat kysymykset, voit valita joko 
- palata pelivalikkoon (kohta 5.) klikkaamalla painiketta ```New game – Uusi peli``` tai
- käydä tarkistamassa juuri pelatun pelin lopputuloksen klikkaamalla ```Game result – Pelin tulos```
- 
Käydään katsomassa, miten peli meni:

#### 5.3. Tarkista pelin tilanne

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/9_game_info.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Juuri pelatun pelin tiedot näkyvät Pelitiedot-taulukosta.

Tältä sivulta pääset hakemaan samat pelitilastot kuin aloitusvalikon pelitilastot-linkistä, mutta täällä klikkaamalla painiketta ```Get – Hae```

Mennään nyt vaikka aloitusvalikon kautta hakemaan jotain aiemmin pelattua peliä (välillä on vaihdettu käyttäjää):

### 6. Hae aiempi peli

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/10_search.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Kirjautuneen pelaajan aloitetut pelit (joita ei ole poistettu) näkyvät Pelilista-taulukossa.

Jatkettavan pelin voi hakea valitsemalla pelinumeron valikosta otsikon ```Choose game number – Valitse pelinumero``` alta.

Peli käynnistyy klikkaamalla painiketta ```Start – Aloita```

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/11_continue.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Voit jatkaa pelaamista, kuten ohjeistettu kohdasta 5.1. Pelaa eteenpäin.

### 7. Hae ja poista peli

Pelin voi hakea samalla tavalla kuin edellisessä kohdassa 6. Hae aiempi peli, mutta sen poistamista varten klikkaamalla aloitusvalikossa hae ja poista -linkkiä:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/12_search_remove.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Kirjautuneen pelaajan aloitetut pelit (joita ei ole poistettu) näkyvät Pelilista-taulukossa.

Poistettavan pelin voi hakea valitsemalla pelinumeron valikosta otsikon ```Choose game number – Valitse pelinumero``` alta.

Pelin poistaminen aloitetaan klikkaamalla painiketta ```Delete – Poista```.

Sovellus varmistaa haluatko todella poistaa ko. pelin:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/13_warning.png">

Jos et halua poistaa, vaan palata takaisin, klikkaa linkkiä ```Back – Takaisin```.

Jos haluat poistaa pelin, klikkaa painiketta ```Delete – Poista```.

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/14_delete_confirm.png">

Sovellus vahvistaa onnistuneen pelin poistamisen. Tai vaihtoehtoisesti antaa virheilmoituksen, jos poisto ei onnistu.

Pääset etenemään, takaisin aloitusvalikkoon, klikkaamalla linkkiä ```Back – Takaisin```.

### 8. Pelitilastot

Kaikki pelitilastot voi hakea klikkaamalla aloitusvalikon linkkiä ```Get game statistics – Hae pelitilastot```.

Pelitilastot -sivu voi näyttää seuraavanlaiselta:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/15_stats.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (alin linkki).

Ylemmästä taulukosta näkee kirjautuneen pelaajan parhaat pelit (enintään 25 peliä), jos pelaajalla on pelattuja pelejä, joiden pistemäärä on enemmän kuin nolla. Jos pelejä ei ole, sovellus ilmoittaa siitä.

Alemmassa taulukossa on listattu enintään 25 sovellukseen tallentunutta parhainta peliä (joissa on pistemäärä vähintään 1) laskevassa paremmuusjärjestyksessä. 

Paremmuusjärjestyksen määräävät seuraavat kriteerit tässä järjestyksessä:
1) suurin pistemäärä (points)
2) suurin vaikeustaso (level)
3) vähiten pelikertoja (sessions)
4) vähiten annettuja vastauksia (answers)

Lopussa näkyy oma ranking-tuloksesi eli parhaimman pelisi sijoitus kaikkien parhaimpien pelien joukossa.

### 9. Salasanan vaihto

Voit vaihtaa oman salasanasi klikkaamalla aloitusvalikon linkkiä ```Change password – Vaihda salasana```.

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/16_change_password.png">

Voit kirjautua ulos (ylin linkki) tai palata takaisin aloitussivulle (```Back – Takaisin``` -painike).

Kirjoita ylimpään kenttään käyttäjätunnuksesi.

Kirjoita keskimmäiseen kenttään nyt voimassaoleva salasanasi.

Kirjoita alimpaan kenttään uusi salasanasi.

Klikkaa ```Change - Vaihda``` -painiketta.

Onnistunut salasanan vaihto näkyy seuraavasti:

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/17_pwd_change_success.png">

Pääset tämän jälkeen etenemään pelissä, takasin aloitusvalikkoon, klikkaamalla ```Back – Takaisin``` -painiketta.

### 10. TÄRKEÄÄ: Virheilmoituksista

Jos saat seuraavanlaisen ilmoituksen, lue viesti, palaa takaisin ja yritä tarvittaessa uudelleen.

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/18_error.png">

Virheilmoitus voi tulla myös selaimesta, esim. Internal Server Error.

Mahdollisesti toiminto on onnistunut virheilmoituksesta huolimatta (sivu ei vain ole latautunut oikein palvelimelta), joten sivun uudelleen lataaminen (selaimen refresh-painike tai näppäimistön F5-näppäin, resend-painike tjs.) yleensä riittää.

<img src="https://github.com/a-bzzzz/trivia/blob/main/documentation/GUI-pics/19_resend.png">

#### Ilmoitustyypit:

- ERROR – VIRHE : Käyttäjän syötteen aiheuttama virhetilanne, joka on korjattavissa oikeanlaisella syötteellä/toiminnalla.
- FAILED – HÄIRIÖ : Järjestelmässä tapahtunut virhetilanne, jota voi yrittää korjata kokeilemalla samaa toimintoa uudelleen. Verkkosovelluksen palvelimen priorisoinnista johtuen voi joutua samoja sivuja lataamaan uudelleen. Suurin osa häiriöilmoituksista poistuu, jos jaksaa kloonata sovelluksen omalle koneelleen ja käynnistää sovelluksen virtuaaliympäristössä Flask:lla.
- GUIDE – OHJE : Ei varsinainen virhetilanne, vaan tilanne, josta sovellus ilmoittaa käyttäjälle. Esim. kun kaikki tiettyyn pelikategoriaan ja tasoon liittyvät kysymykset on käyty läpi ja käyttäjä voi jatkaa pelaamista valitsemalla uuden kategorian ja tason.


### VIELÄ TÄRKEÄMPÄÄ: Ole armollinen ja nauti pelistä :-)
