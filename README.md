# Wstęp

Autmatyzacja przypadków testowych została stworzona w języku Python (3.7.3) z zastosowaniem wzorca
projektowego Page Object Pattern.


## Przypadki testowe ujęte w projekcie:

• Weryfikacja komunikatu błędu dla adresu e-mail o błędnej składni (test@test) wprowadzonego w
oknie logowania do aplikacji,
• Weryfikacja komunikatu błędu dla niewypełnionego pola login (adres e-mail) w oknie logowania,
• Weryfikacja komunikatu błędu dla niewypełnionego pola hasło w oknie logowania do aplikacji,
• Walidacja komunikatu błędu dla wylotu i powrotu odbywającego się z tego samego
lotniska, w panelu wyszukiwania lotów,
• Weryfikacji poprawności zmiany kierunku lotu, dla lotniska wylotu i lotniska docelowego,
• Weryfikacji zmiany wartości pola data powrotu, po zmianie charakterystyki wyszukiwania
poprzez wybranie opcji „W jedną stronę”.1. Okno logowania

# Opis przypadków testowych:
Przypadek testowy opisany w funkcji test_incorrect_login_msg (ID: 01) wykonuje przejście do
okna logowania za pomocą adresu e-mail. Weryfikuje poprawność komunikatu po wprowadzeniu
do pola „E-mail” adresu o błędnej składni (test@test).

Przypadek testowy test_empty_login_msg (ID:02) po przejściu do okna logowania weryfikuje
poprawność komunikatu w wypadku nie uzupełnienia wartości w polu „E-mail”.

Test test_empty_password_msg (ID: 03) po przejściu do okna logowania (za pomocą adresu e-mail)
weryfikuje poprawność komunikatu w przypadku nie wprowadzenia wartości w polu „Hasło”.

## ID: 01 - test_incorrect_login_msg
Tytuł: Logowanie użytkownika – Wprowadź niepoprawny składniowo adres e-mail w polu e-
mail panelu logowania do systemu.
Środowisko: Chrome wersja 74.0.3729.157, Ubuntu 19.04
Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.
### Kroki:
1. Wejdź na stronę "https://www.skyscanner.pl/"
2. Kliknij przycisk "Zaloguj się"
3. W sekcji „Kontynuuj przez” wybierz: "E – mail"
4. Wpisz niepoprawny składniowo e-mail (test@test)
5. Utrać focus z pola „E-mail”

### Oczekiwany rezultat:
Poniżej pola „E-mail” pojawia się komunikat: „Upewnij się, że adres e-mail jest prawidłowy”

## ID: 02 - test_empty_login_msg
Tytuł: Logowanie użytkownika – Pozostaw pustą wartość w polu „E-mail” w oknie logowania
do systemu skyscanner.
Środowisko: Chrome wersja 74.0.3729.157, Ubuntu 19.04
Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

### Kroki:
1. Wejdź na stronę "https://www.skyscanner.pl/"
2. Kliknij "Zaloguj się"
3. W sekcji „Kontynuuj przez” wybierz: "E – mail"
4. Pozostaw pole adres e-mail puste
5. Utrać focus z pola „E-mail”

### Oczekiwany rezultat:
Poniżej pola „E-mail” pojawia się komunikat: „Podaj adres e-mail”ID: 03
Tytuł: Logowanie użytkownika – Pozostaw pustą wartość w polu „Hasło” w oknie logowania
do systemu skyscanner.
Środowisko: Chrome wersja 74.0.3729.157, Ubuntu 19.04
Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

### Kroki:
1. Wejdź na stronę "https://www.skyscanner.pl/"
2. Kliknij "Zaloguj się"
3. W sekcji „Kontynuuj przez” wybierz: "E – mail"
4. Pozostaw pole hasło puste
5. Utrać focus z pola „Hasło”

### Oczekiwany rezultat:
Poniżej pola „Hasło” pojawia się komunikat: „Podaj hasło”


## ID: 03 - test_empty_password_msg
Tytuł: Logowanie użytkownika – Pozostaw pustą wartość w polu „Hasło” w oknie logowania
do systemu skyscanner.
Środowisko: Chrome wersja 74.0.3729.157, Ubuntu 19.04
Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

### Kroki:
1. Wejdź na stronę "https://www.skyscanner.pl/"
2. Kliknij "Zaloguj się"
3. W sekcji „Kontynuuj przez” wybierz: "E – mail"
4. Pozostaw pole hasło puste
5. Utrać focus z pola „Hasło”

### Oczekiwany rezultat:
Poniżej pola „Hasło” pojawia się komunikat: „Podaj hasło”
