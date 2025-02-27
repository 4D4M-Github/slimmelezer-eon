# SlimmeLezer telepítés – ESPHome

### Készült Slimmelezer.E.ON - [4D4M](https://prohardver.hu/tag/4d4m.html)

1. ESPHome platform szerinti telepítés esetén a [mindig aktuális útmutató](https://esphome.io/guides/getting_started_hassio) alapján létre kell hozni a slimmelezer konfiguráció fogadására alkalmas "üres" eszközt.

2. Az így kapott yaml fájlunk tartalmát az igényeinknek megfelelő, itt felsorolt valamelyik yaml fájl szerint ki kell egészíteni:
   
#### slimmelezer_alap.yaml:
  Alapvető információkat továbbít a magyar mérők jelenlegi (2023.10.03) beállítása szerint, hálózatra termelő napelemes
  rendszer nélküli mérőkhöz ajánlott, ahol nincs hálózatba betáplálás és nem fontosak a meddő teljesítmények és energiák.
   
#### slimmelezer_napelemes_2023.yaml:
  2024 előtt telepített (felprogramozott) mérők által küldött adatok feldolgozására alkalmas alapbeállítás. Tartalmazza az 
  összes napelemes rendszer mellett releváns mérési adatot, a meddő teljesítmények és energiákat is beleértve.
  Ezen kívül tartalmaz egy sciptet is, ami egy egyszerű pillanatnyi egyenleget von a betáplált és vételezett teljesítményre
  vonatkozóan.
  
#### slimmelezer_napelemes_2024.yaml:
  2024 után telepített (felprogramozott) mérők által küldött adatok feldolgozására alkalmas alapbeállítás. Tartalmazza az 
  összes napelemes rendszer mellett releváns mérési adatot, a meddő teljesítmények és energiákat is beleértve.
  Ezen kívül tartalmaz egy sciptet is, ami egy egyszerű pillanatnyi egyenleget von a betáplált és vételezett teljesítményre
  vonatkozóan.

  <ins>Mérők az újabb konfigurációval:</ins>  
   • Wasion aMeter100  
   • Wasion aMeter300  
   • Sagemcom MA110M  
   • Sagemcom MA309M  
   • Sanxing SX601 S12U26  
   • Sanxing SX631 S34U28  
   • Holley DDSD285 (2024-től)  
   • Holley DTSD545 (2024-től)  
  
  Azon mérési adatokat tartalmazó sorok elé, amiket nem szeretnénk, hogy továbbítson a slimmelezer a HomeAssistant felé,
  célszerűen egy # jelet téve inaktiválhatjuk a fordító számára, így azok nem fognak megjelenni a HomeAssistantban entitásként.
  Értelemszerűen, ha valamit szeretnénk még megjeleníteni a meglévő példa yaml fájlokhoz képest, akkor azoknál ki kell
  törölni a # jelet a sorok elől, ügyelve a szóközökkel való megfelelő pozícionálás megőrzésére.
  
  Magyarországi mérők sajátosságai miatt a következő paraméterek megadása kötelező a konfigurációs fájlban, különben nem lesz
  képes feldolgozni és továbbítani a mérők által küldött telegram üzenetet: (alapból tartalmazza mindegyik példa yaml fájl)
   
```yaml
dsmr:
  id: dsmr_instance
  crc_check: false
  max_telegram_length: 3000
```

#### megjegyzés: 
Az itt elérhető csomag tartalmazza még slimmelezerre direktben(OTA, USB) feltölthető firmware-ek lefordított binárisait is, viszont ezek használata nem javasolt, mert frissítések alkalmával elveszhet a meglévő konfiguráció:
[Slimmelezer.E.ON-4D4M.rar](https://drive.google.com/file/d/10OlD0Aoxti3LFLMXj2cScBJ9jfaaUWNJ/view)
