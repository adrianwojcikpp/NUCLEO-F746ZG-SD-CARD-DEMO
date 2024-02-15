# Przykłady aplikacji wbudowanych dla zestawu NUCLEO-F746ZG <br> + adapter karty microSD

Przykładowa aplikacja wbudowane dla zestawu uruchomieniowego NUCLEO z mikrokontrolerem STM32F746ZG z zewnętrznym [adapterem karty microSD](https://sklep.msalamon.pl/produkt/czytnik-kart-pamieci-microsd-spi-sdio/). Materiały uzupełniające zajęcia laboratoryjne z przedmiotu *Systemy mikroproceosrorowe* na kierunku Automatyka i Robotyka Politechniki Poznańskiej.

Aplikacja wykorzystuje insterfejs SDMMC do komunikacji z kartą SD wraz z generycznym driverem dostarczonym w pakiecie CubeF7. 

W celu uruchomienia aplikacji, należy:
+ Podłączyć [adapter karty microSD](https://sklep.msalamon.pl/produkt/czytnik-kart-pamieci-microsd-spi-sdio/) do zestawu NUCLEO:
  + D0 - PC8
  + D1 - PC9
  + D2 - PC10
  + D3 - PC11
  + CK - PC12
  + CMD - PD2
  + VCC - 3V3
  + GND - GND
+ Umieścić w [adapterze](https://sklep.msalamon.pl/produkt/czytnik-kart-pamieci-microsd-spi-sdio/) kartę microSD z system plików FAT32
+ Podłącz zasilanie do NUCLEO i uruchom przykładowy projekt.
+ Naciśnij kilkukrotnie przycisk **USER** obserwując terminal portu szeregowego. Odłącz zasilanie NUCLEO i sprawdź zawartość karty SD.

Na karcie SD powinien powstać plik tekstowy "LOGFILE.CSV", do którego co 1 sekundę zapisany będzie **czas** od resetu wyrażony w milisekundach oraz **stan przycisku** USER (0 lub 1). Po każdym zapisie na kartę następuje odczyt ostatniej linijki pliku .csv i przesłanie jej treści po porcie szeregowym. Błąd w zapisie lub odczycie spowoduje miganie diody czerwonej. Prawidłowe działanie programu sygnalizowane jest miganiem diody zielonej.

**Konfiguracja portu szeregowego:** 115200 bps, 8 bitów danych, 1 bit stopu, brak parzystości. 

Projekty stworzone za pomocą środowiska [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) w wersji 1.13.2, firmware [STM32CubeF7](https://www.st.com/en/embedded-software/stm32cubef7.html) w wersji 1.16.2. oraz [FatFs](http://elm-chan.org/fsw/ff/) w wersji R0.12c.