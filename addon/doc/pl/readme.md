# Sterownik Vocalizer Automotive 5.5

Ten dodatek dostosowuje starszy, 32-bitowy sterownik Nuance Vocalizer Automotive 5.5 do 32- i 64-bitowych wersji NVDA.

W 32-bitowym NVDA oryginalny sterownik Automotive jest ładowany bezpośrednio. W 64-bitowym NVDA most uruchamia go w dedykowanym 32-bitowym hoście syntezatora. Sposób przekazywania dźwięku mowy zależy od zainstalowanego wariantu: standardowego albo brokered audio.

## Instalacja

1. Zainstaluj dodatek.
2. Zainstaluj osobno dodatki z głosami.
3. Użyj menu **Menu NVDA > Vocalizer Automotive**, aby wprowadzić licencję i skonfigurować automatyczne przełączanie języka.
4. Uruchom ponownie NVDA i wybierz `vocalizerAutomotive` w 32-bitowym NVDA albo `vocalizerAutomotive32` w 64-bitowym NVDA.

Plik licencji nie jest dołączony do pakietu i trzeba go zaimportować z własnej licencjonowanej kopii.

## Przetwarzanie dźwięku

W 64-bitowym NVDA 2026.2 i nowszych wariant brokered audio przekazuje dźwięk mowy przez główny proces NVDA. W 32-bitowym NVDA Automotive korzysta z natywnej ścieżki bezpośredniej. Sonic Pitch pozostaje zgodny ze ścieżką brokered audio.

Ten wariant obsługuje natywne przyciszanie dźwięku NVDA. Skrót `Shift+NVDA+D` przełącza tryby przyciszania dźwięku dostępne w NVDA. Na 64-bitowej ścieżce brokered NVDA zarządza wybranym trybem i go zapisuje. Wariant standardowy nie korzysta z tej ścieżki.

## Dostępne warianty

- **Wariant standardowy:** używa klasycznego mostu zgodności w 64-bitowym NVDA 2026.1 i nowszych oraz natywnej ścieżki bezpośredniej w 32-bitowym NVDA.
- **Wariant brokered audio:** przekazuje dźwięk mowy przez główny proces NVDA w 64-bitowym NVDA 2026.2 i nowszych oraz używa natywnej ścieżki bezpośredniej w 32-bitowym NVDA.

Instaluj tylko jeden wariant naraz.

## Automatyczne przełączanie języka

Okno ustawień wykrywa zainstalowane głosy na podstawie ich metadanych `.hdr` i zapisuje wybrane przypisania w pliku `%APPDATA%\nvda\vocalizer.ini`.

## Tłumaczenia

Interfejs dodatku zawiera lokalizacje `an`, `ar`, `da`, `de`, `el`, `es`, `fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`, `ko`, `nb_NO`, `ne`, `nl`, `pl`, `pt_BR`, `pt_PT`, `ru`, `sk`, `sl`, `tr` i `zh_CN`. Dokumentacja HTML jest dostępna po angielsku, polsku i słowacku.
