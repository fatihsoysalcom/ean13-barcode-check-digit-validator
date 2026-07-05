# EAN13 Barcode Check Digit Validator

This example demonstrates the GS1 Mod-10 algorithm for validating the check digit of an EAN-13 barcode. It takes a 13-digit barcode string, calculates the expected check digit based on the first 12 digits, and compares it with the provided 13th digit to determine validity. This helps prevent data entry errors for product identification numbers.

## Language

`python`

## How to Run

Save the code as `ean13_validator.py`. Run from your terminal using `python ean13_validator.py`. The script will validate several example barcodes and then prompt you to enter your own.

## Original Article

This example accompanies the Turkish article: [GTIN / EAN-13 Barkod Kontrol Basamağını Doğrulama: GS1 Mod-10 Algoritması Detaylı Anlatım](https://fatihsoysal.com/blog/gtin-ean-13-barkod-kontrol-basamagini-dogrulama-gs1-mod-10-algoritmasi-detayli-anlatim/).

## License

MIT — see [LICENSE](LICENSE).
