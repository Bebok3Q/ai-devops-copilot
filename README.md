# DevOps Anomaly Dashboard

## Opis Projektu

Ten projekt to kompleksowe rozwiązanie do analizy logów systemowych w środowiskach DevOps, mające na celu wczesne wykrywanie anomalii i sugerowanie potencjalnych poprawek. Składa się z backendowej aplikacji API (opartej na FastAPI i Pythonie) oraz interaktywnego panelu użytkownika (frontend w React), umożliwiającego monitorowanie logów w czasie rzeczywistym, identyfikowanie problemów i szybkie reagowanie na nie.

Projekt ten demonstruje integrację różnych technologii w celu stworzenia funkcjonalnego i użytecznego narzędzia dla inżynierów DevOps i zespołów utrzymania systemów.

## Kluczowe Funkcjonalności

* **Analiza Logów:** Backendowa aplikacja API przyjmuje logi systemowe, analizuje je pod kątem wzorców i potencjalnych błędów.
* **Wykrywanie Anomalii:** Implementacja (obecnie podstawowa, z potencjałem do rozbudowy) logiki wykrywania anomalii w strumieniu logów.
* **Sugerowanie Poprawek:** System próbuje sugerować potencjalne przyczyny błędów i proponować proste poprawki na podstawie znanych wzorców błędów.
* **Interaktywny Dashboard:** Frontend w React wyświetla analizowane logi, wyróżnia anomalie, prezentuje sugerowane poprawki oraz podstawowe statystyki.
* **Przechowywanie Logów:** Wykorzystanie bazy danych (np. SQLite) do przechowywania analizowanych logów.
* **Konteneryzacja:** Projekt jest konteneryzowany przy użyciu Dockera, co ułatwia wdrożenie i uruchomienie w różnych środowiskach.

## Użyte Technologie

* **Backend:**
    * Python 3
    * FastAPI - nowoczesny, szybki framework API
    * SQLAlchemy - ORM do interakcji z bazą danych
    * Uvicorn - serwer ASGI dla FastAPI
* **Frontend:**
    * React - biblioteka JavaScript do budowania interfejsów użytkownika
    * Axios - klient HTTP do komunikacji z backendem
    * Tailwind CSS - framework CSS do szybkiego stylowania
* **Inne:**
    * Docker - platforma do konteneryzacji aplikacji

## Architektura

Projekt składa się z dwóch głównych części:

1.  **Backend API (FastAPI):**
    * Przyjmuje logi poprzez endpoint `/log/analyze`.
    * Analizuje logi przy użyciu modułu `core.analyzer`.
    * Wykorzystuje `core.patch_generator` do sugerowania poprawek.
    * Zapisuje analizowane logi w bazie danych (SQLAlchemy).
    * Udostępnia endpoint `/log/dashboard` do pobierania logów dla frontendu.
2.  **Frontend (React):**
    * Wysyła żądania do backendu API w celu pobrania danych logów.
    * Wyświetla logi, anomalie, sugerowane poprawki i statystyki w interaktywnym dashboardzie.
    * Wykorzystuje komponenty takie jak `LogCard`, `RecentAnomalies`, `SuggestedFixes` i `BuildStats` do prezentacji danych.

## Uruchomienie Projektu

Aby uruchomić ten projekt lokalnie, wykonaj następujące kroki:

1.  **Wymagania:**
    * Python 3.x
    * Docker

2.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/Bebok3Q/ai-devops-copilot.git]
    cd [ai_devops_copilot]
    ```

3.  **Uruchom backend (przy użyciu Dockera):**
    ```bash
    docker build -t ai-copilot-backend -f backend/Dockerfile .
    docker run -d -p 8000:8000 --name ai-copilot-backend ai-copilot-backend
    ```
    Backend będzie dostępny pod adresem `http://localhost:8000`.

4.  **Uruchom frontend (przy użyciu npm lub yarn):**
    Przejdź do katalogu `frontend`:
    ```bash
    cd frontend
    npm install  # lub yarn install
    npm start    # lub yarn start
    ```
    Frontend będzie dostępny pod adresem `http://localhost:3000` (domyślnie dla Create React App).

## Endpointy API

* `POST /log/analyze`: Przyjmuje treść logu w formacie JSON (`{"content": "..."}`) i zwraca wynik analizy oraz zapisuje log w bazie danych.
* `GET /log/dashboard`: Zwraca listę ostatnich analizowanych logów z bazy danych, zawierającą informacje o błędach, anomaliach i sugerowanych poprawkach.

## Komponenty Frontendowe

* `LogCard`: Wyświetla pojedynczy wpis logu.
* `RecentAnomalies`: Prezentuje listę ostatnio wykrytych anomalii.
* `SuggestedFixes`: Wyświetla listę unikalnych sugerowanych poprawek.
* `BuildStats`: (Obecnie zawiera dummy data) Prezentuje statystyki ostatnich buildów.

## Przyszłe Kierunki Rozwoju

* Implementacja bardziej zaawansowanych algorytmów wykrywania anomalii (np. uczenie maszynowe).
* Integracja z różnymi źródłami logów (np. systemd, pliki logów, scentralizowane systemy logowania).
* Rozbudowa mechanizmu sugerowania poprawek o bardziej szczegółowe instrukcje.
* Dodanie autentykacji i autoryzacji do API.
* Ulepszenie interfejsu użytkownika dashboardu o dodatkowe filtry, wykresy i wizualizacje.
* Dodanie możliwości konfiguracji alertów o wykrytych anomaliach.

## Autor

[Kacper Talaga / Bebok3Q]
