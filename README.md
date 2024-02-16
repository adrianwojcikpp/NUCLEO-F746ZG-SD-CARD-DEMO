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
+ Umieścić w [adapterze](https://sklep.msalamon.pl/produkt/czytnik-kart-pamieci-microsd-spi-sdio/) kartę microSD z system plików FAT32.
+ Podłącz zasilanie do NUCLEO i uruchom przykładowy projekt.
+ Naciśnij kilkukrotnie przycisk **USER** obserwując terminal portu szeregowego.  
+ Odłącz zasilanie NUCLEO i sprawdź zawartość karty SD.
+ Uruchom dołączony skrypt Python aby wygenerować wykres z zawrtością pliku.

Na karcie SD powinien powstać plik tekstowy "LOGFILE.CSV", do którego co 0.1 sekundy zapisany będzie **czas** od resetu wyrażony w milisekundach oraz **stan przycisku** USER (0 lub 1). Po każdym zapisie na kartę następuje odczyt ostatniej linijki pliku .csv i przesłanie jej treści po porcie szeregowym. Błąd w zapisie lub odczycie spowoduje miganie diody czerwonej. Prawidłowe działanie programu sygnalizowane jest miganiem diody zielonej. Zakończenie logowania sygnalizowane jest miaganiem diody niebieskiej.

**Konfiguracja portu szeregowego:** 115200 bps, 8 bitów danych, 1 bit stopu, brak parzystości. 

Projekty stworzone za pomocą środowiska [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) w wersji 1.13.2, firmware [STM32CubeF7](https://www.st.com/en/embedded-software/stm32cubef7.html) w wersji 1.16.2. oraz [FatFs](http://elm-chan.org/fsw/ff/) w wersji R0.12c.

## Examples of embedded applications for the NUCLEO-F746ZG kit  <br> + microSD card adapter
Examples of embedded applications for the NUCLEO development kit with the STM32F746ZG microcontroller with an external microSD card adapter. Supplementary teaching materials for Microprocessor systems laboratory classes on Automatic Control and Robotics at the Poznań University of Technology.

The application uses the SDMMC interface to communicate with the SD card usin generic driver provided in the CubeF7 package.

To run the application, proceed as follows:
+ Connect the microSD card adapter to the NUCLEO set:
  + D0 - PC8
  + D1 - PC9
  + D2 - PC10
  + D3 - PC11
  + CK - PC12
  + CMD - PD2
  + VCC - 3V3
  + GND - GND
+ Place a microSD card with the FAT32 file system in the adapter.
+ Connect power to NUCLEO and run the sample project.
+ Press the USER button several times while observing the serial port terminal. 
+ Disconnect NUCLEO power and check the contents of the SD card.
+ Run included Python script to plot log file content.


A text file "LOGFILE.CSV" should be created on the SD card, in which the **time** since the reset expressed in milliseconds and the **state** of the USER button (0 or 1) will be written every 0.1 second. After each write to the card, the last line of the .csv file is read and its content is sent via the serial port. An error in writing or reading is indicated by the red LED flashing. Correct operation of the program is indicated by the green LED flashing. Logging completed is indicated by the blue LED flashing.

**Serial port configuration**: 115200 bps, 8 data bits, 1 stop bit, no parity.

Projects created using the [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) environment version 1.13.2, [STM32CubeF7](https://www.st.com/en/embedded-software/stm32cubef7.html) firmware version 1.16.2. and [FatFs](http://elm-chan.org/fsw/ff/) version R0.12c.