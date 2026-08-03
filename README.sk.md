# 32-bitový most Vocalizer Automotive pre NVDA

[English](README.md) | [Polski](README.pl.md) | Slovenčina

Projekt upravuje starší 32-bitový ovládač Nuance Vocalizer Automotive 5.5
tak, aby fungoval v 32-bitových aj 64-bitových verziách NVDA.

V 32-bitovom NVDA sa pôvodný ovládač Automotive načíta priamo. V 64-bitovom
NVDA ho most spúšťa vo vyhradenom 32-bitovom hostiteľovi syntetizátora pomocou
štandardného mosta kompatibility NVDA.

## Dôležité

Balík neobsahuje samostatné hlasové doplnky Vocalizer ani používateľský súbor
`vocalizer_license.ini`. Runtime stále vyžaduje platnú licenciu, ktorú treba
importovať samostatne.

Tento fork je udržiavaný nezávisle. Problémy hláste v tomto úložisku a žiadosti o podporu neposielajte dodávateľom ani správcom pôvodných komponentov. Pôvodný projekt Vocalizer Automotive 5.5 sa už oficiálne nevyvíja ani nepodporuje. Pôvodný autor doplnku nezodpovedá za tento nezávislý fork, zmeny v ňom ani technickú podporu.

## Inštalácia

1. Nainštalujte verejne dostupný súbor `.nvda-addon` zo stránky GitHub Releases alebo
   skopírujte tento balík do priečinka doplnkov NVDA.
2. Balík už obsahuje požadované runtime súbory Automotive.
3. Samostatne nainštalujte vlastné doplnky s hlasmi Vocalizer Automotive.
   Ich priečinky sa zvyčajne začínajú na `vocalizer-voice-`.
4. Spustite NVDA a otvorte:

   `Ponuka NVDA > Vocalizer Automotive > Zadať licenciu`

   Licencia sa skopíruje do:

   `%APPDATA%\nvda\vocalizer_license.ini`

5. Reštartujte NVDA a vyberte ovládač podľa architektúry NVDA:

   - 32-bitové NVDA: `vocalizerAutomotive`
   - 64-bitové NVDA: `vocalizerAutomotive32`

## Spracovanie zvuku

Toto vydanie používa klasický most kompatibility NVDA v 64-bitovom NVDA. V
32-bitovom NVDA Automotive používa natívnu priamu cestu. Sonic Pitch funguje
nezávisle pomocou vlastného hooku WavePlayer.

Toto vydanie nepoužíva cestu brokered audio NVDA. Ak potrebujete brokered audio
a natívne stíšenie zvuku, použite `v2.2.0` v 64-bitovom NVDA 2026.2 alebo
novšom.

## Varianty vydaní

- `v2.1.7`: klasický most pre 32-bitové NVDA a 64-bitové NVDA 2026.1 a novšie.
- `v2.2.0`: most brokered audio pre 64-bitové NVDA 2026.2 a novšie s priamou
  cestou pre 32-bitové NVDA.

Inštalujte naraz iba jeden variant doplnku.

## Automatické prepínanie jazyka

V ponuke sa nachádza položka **Nastavenia automatického prepínania jazyka**.
Dialóg vyhľadá nainštalované hlasy Automotive podľa metadát `.hdr` a uloží
vybrané priradenia hlasov do:

`%APPDATA%\nvda\vocalizer.ini`

## Kontrola prostredia

Spustite:

```powershell
.\tools\Check-VocalizerAutomotiveRuntime.ps1
```

Skript zobrazí požadované runtime súbory, nájdené hlasové doplnky a samostatný
licenčný súbor. Nesťahuje ani nepridáva licenciu.

## Zostavenie

Ak chcete vytvoriť kompletný doplnok:

```powershell
.\tools\Build-PublicAddon.ps1
```

Balík sa uloží do priečinka `dist` a bude obsahovať runtime súbory uložené
v úložisku. Skript vždy vynechá `vocalizer_license.ini`.

Univerzálna šablóna prekladov sa nachádza v súbore
`locale/vocalizer_automotive_driver.pot`.

Rozhranie doplnku obsahuje lokalizácie: `an`, `ar`, `da`, `de`, `el`, `es`,
`fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`, `ko`, `nb_NO`, `ne`, `nl`, `pl`,
`pt_BR`, `pt_PT`, `ru`, `sk`, `sl`, `tr` a `zh_CN`. HTML dokumentácia je
dostupná v angličtine, poľštine a slovenčine.

## Licencia

Zdrojový kód ovládača NVDA a mosta je distribuovaný pod licenciou GPL-2.0
podľa súborov [LICENSE](LICENSE) a [gpl.txt](gpl.txt). Priložené runtime
súbory sú samostatné runtime súbory priložené k tomuto forku. Hlasové doplnky
a používateľské licenčné súbory nie sú súčasťou balíka.
