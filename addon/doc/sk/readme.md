# Ovládač Vocalizer Automotive 5.5

Tento doplnok upravuje starší 32-bitový ovládač Nuance Vocalizer Automotive 5.5 pre 32-bitové aj 64-bitové verzie NVDA.

V 32-bitovom NVDA sa pôvodný ovládač Automotive načíta priamo. V 64-bitovom NVDA ho most spúšťa vo vyhradenom 32-bitovom hostiteľovi syntetizátora. Spôsob odovzdávania zvuku reči závisí od nainštalovaného variantu: štandardného alebo brokered audio.

## Inštalácia

1. Nainštalujte doplnok.
2. Samostatne nainštalujte doplnky s hlasmi.
3. V ponuke **Ponuka NVDA > Vocalizer Automotive** zadajte licenciu a nastavte automatické prepínanie jazyka.
4. Reštartujte NVDA a vyberte `vocalizerAutomotive` v 32-bitovom NVDA alebo `vocalizerAutomotive32` v 64-bitovom NVDA.

Licenčný súbor nie je súčasťou balíka a musí sa importovať z vlastnej licencovanej kópie.

## Spracovanie zvuku

V 64-bitovom NVDA 2026.2 a novšom variant brokered audio odovzdáva zvuk reči cez hlavný proces NVDA. V 32-bitovom NVDA používa Automotive natívnu priamu cestu. Sonic Pitch zostáva kompatibilný s cestou brokered audio.

Tento variant podporuje natívne stíšenie zvuku NVDA. Skratka `Shift+NVDA+D` prepína režimy stíšenia zvuku dostupné v NVDA. Na 64-bitovej brokered ceste spravuje a ukladá vybraný režim NVDA. Štandardný variant túto cestu nepoužíva.

## Dostupné varianty

- **Štandardný variant:** používa klasický most kompatibility v 64-bitovom NVDA 2026.1 a novšom a natívnu priamu cestu v 32-bitovom NVDA.
- **Variant brokered audio:** odovzdáva zvuk reči cez hlavný proces NVDA v 64-bitovom NVDA 2026.2 a novšom a používa natívnu priamu cestu v 32-bitovom NVDA.

Naraz inštalujte iba jeden variant.

## Automatické prepínanie jazyka

Dialóg nastavení vyhľadá nainštalované hlasy podľa ich metadát `.hdr` a uloží vybrané priradenia do súboru `%APPDATA%\nvda\vocalizer.ini`.

## Preklady

Rozhranie doplnku obsahuje lokalizácie `an`, `ar`, `da`, `de`, `el`, `es`, `fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`, `ko`, `nb_NO`, `ne`, `nl`, `pl`, `pt_BR`, `pt_PT`, `ru`, `sk`, `sl`, `tr` a `zh_CN`. HTML dokumentácia je dostupná v angličtine, poľštine a slovenčine.
