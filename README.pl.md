# Most 32-bitowego Vocalizer Automotive dla NVDA

[English](README.md) | Polski | [Slovenčina](README.sk.md)

Projekt dostosowuje starszy, 32-bitowy sterownik Nuance Vocalizer Automotive
5.5 do 32- i 64-bitowych wersji NVDA.

W 32-bitowym NVDA oryginalny sterownik Automotive jest ładowany
bezpośrednio. W 64-bitowym NVDA most uruchamia go w dedykowanym 32-bitowym
hoście syntezatora. Sposób przekazywania dźwięku mowy zależy od zainstalowanego
wariantu: standardowego albo brokered audio.

## Ważne

Pakiet nie zawiera osobnych dodatków z głosami Vocalizer ani przypisanego do
użytkownika pliku `vocalizer_license.ini`. Runtime nadal wymaga ważnej
licencji, którą należy zaimportować osobno.

Ten fork jest utrzymywany niezależnie. Zgłaszaj problemy w tym repozytorium
i nie kieruj próśb o pomoc do dostawców ani opiekunów oryginalnych komponentów.
Oryginalny projekt Vocalizer Automotive 5.5 nie jest już oficjalnie rozwijany ani wspierany. Autor oryginalnego dodatku nie ponosi odpowiedzialności za ten niezależny fork, wprowadzone w nim modyfikacje ani pomoc techniczną.

## Instalacja

1. Zainstaluj publiczny plik `.nvda-addon` z zakładki GitHub Releases albo
   skopiuj repozytorium do katalogu dodatków NVDA.
2. Pakiet zawiera już wymagane pliki runtime Automotive.
3. Zainstaluj osobno własne dodatki z głosami Vocalizer Automotive. Ich
   katalogi zwykle zaczynają się od `vocalizer-voice-`.
4. Uruchom NVDA i otwórz:

   `Menu NVDA > Vocalizer Automotive > Wprowadź licencję`

   Licencja zostanie skopiowana do:

   `%APPDATA%\nvda\vocalizer_license.ini`

5. Uruchom ponownie NVDA i wybierz sterownik odpowiedni dla architektury NVDA:

   - 32-bitowy NVDA: `vocalizerAutomotive`
   - 64-bitowy NVDA: `vocalizerAutomotive32`

## Przetwarzanie dźwięku

W 64-bitowym NVDA 2026.2 i nowszych wariant brokered audio przekazuje
dźwięk mowy przez główny proces NVDA. W 32-bitowym NVDA Automotive korzysta
z natywnej ścieżki bezpośredniej. Sonic Pitch pozostaje zgodny ze ścieżką
brokered audio.

Ten wariant obsługuje natywne przyciszanie dźwięku NVDA. Skrót
`Shift+NVDA+D` przełącza tryby przyciszania dźwięku dostępne w NVDA.
Na 64-bitowej ścieżce brokered NVDA zarządza wybranym trybem i go zapisuje.
Wariant standardowy nie korzysta z tej ścieżki.

## Dostępne warianty

- **Wariant standardowy:** używa klasycznego mostu zgodności w 64-bitowym
  NVDA 2026.1 i nowszych oraz natywnej ścieżki bezpośredniej w 32-bitowym
  NVDA.
- **Wariant brokered audio:** przekazuje dźwięk mowy przez główny proces NVDA
  w 64-bitowym NVDA 2026.2 i nowszych oraz używa natywnej ścieżki bezpośredniej
  w 32-bitowym NVDA.

Instaluj tylko jeden wariant naraz.

## Automatyczne przełączanie języka

W menu znajduje się pozycja **Ustawienia automatycznego przełączania języka**.
Okno wykrywa zainstalowane głosy Automotive na podstawie metadanych `.hdr`
i zapisuje wybrane przypisania głosów w:

`%APPDATA%\nvda\vocalizer.ini`

## Sprawdzenie środowiska

Uruchom:

```powershell
.\tools\Check-VocalizerAutomotiveRuntime.ps1
```

Skrypt pokazuje wymagane pliki runtime, wykryte dodatki głosowe oraz osobny
plik licencji. Nie pobiera ani nie dołącza licencji.

## Budowanie

Aby zbudować kompletny dodatek:

```powershell
.\tools\Build-PublicAddon.ps1
```

Pakiet zostanie zapisany w katalogu `dist` i będzie zawierał pliki runtime
przechowywane w repozytorium. Skrypt zawsze pomija `vocalizer_license.ini`.

Uniwersalny szablon tłumaczeń znajduje się w pliku
`locale/vocalizer_automotive_driver.pot`.

Interfejs dodatku zawiera lokalizacje: `an`, `ar`, `da`, `de`, `el`, `es`, `fi`,
`fr`, `gl`, `hr`, `hu`, `it`, `ja`, `ko`, `nb_NO`, `ne`, `nl`, `pl`, `pt_BR`,
`pt_PT`, `ru`, `sk`, `sl`, `tr` i `zh_CN`. Dokumentacja HTML jest dostępna po
angielsku, polsku i słowacku.

## Licencja

Kod sterownika NVDA i mostu jest udostępniany na licencji GPL-2.0, zgodnie
z plikiem [gpl.txt](gpl.txt). Dołączone pliki runtime są
osobnymi plikami runtime dołączonymi do tego fork’a. Dodatki z głosami i
przypisane do użytkownika pliki licencji nie są dołączane.
