<div align="center">

# 💰 BudżetApp

### Aplikacja desktopowa do zarządzania budżetem domowym

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2+-1F6FEB?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557C?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-W%20budowie-orange?style=for-the-badge)

> Prosta, przejrzysta i funkcjonalna aplikacja do śledzenia przychodów, wydatków i celów oszczędnościowych — dla każdego, kto chce mieć swoje finanse pod kontrolą.

</div>

---

## 📋 Spis treści

- [O projekcie](#-o-projekcie)
- [Funkcjonalności](#-funkcjonalności)
- [Technologie](#-technologie)
- [Instalacja](#-instalacja)
- [Uruchomienie](#-uruchomienie)
- [Struktura projektu](#-struktura-projektu)
- [Zespół](#-zespół)
- [Zrzuty ekranu](#-zrzuty-ekranu)

---

## 🧾 O projekcie

**BudżetApp** to desktopowa aplikacja do zarządzania budżetem domowym, napisana w Pythonie z użyciem biblioteki CustomTkinter. Projekt powstał jako aplikacja zespołowa, z myślą o każdej osobie, która chce świadomie śledzić swoje finanse — bez kont w chmurze, bez subskrypcji, bez reklam.

Wszystkie dane przechowywane są **lokalnie** na dysku użytkownika w formacie JSON.

---

## ✨ Funkcjonalności

### 📊 Pulpit (Dashboard)
- Budżet na dziś — animowany wskaźnik dziennego wykorzystania
- Podsumowanie miesiąca: przychody, wydatki, bilans, stopa oszczędności
- Prognoza wydatków do końca miesiąca (ekstrapolacja liniowa)
- Seria aktywnych dni z rzędu 🔥
- Wykres słupkowy wydatków dziennych z linią limitu
- Boczny panel kategorii wydatków

### 💳 Transakcje
- Dodawanie przychodów i wydatków z kategorią, opisem i datą
- Filtrowanie po miesiącu i typie transakcji
- Historia transakcji z kolorowym oznaczeniem kategorii
- Usuwanie transakcji jednym kliknięciem
- Podsumowanie miesiąca na żywo

### 🏷️ Kategorie
- 10 predefiniowanych kategorii (Jedzenie, Transport, Mieszkanie...)
- Paski postępu top-3 kategorii w bieżącym miesiącu
- Porównanie wydatków kategorii: ten miesiąc vs poprzedni (trendy ↑↓)
- Wykres poziomy wydatków per kategoria

### 🎯 Cele oszczędnościowe
- Dodawanie własnych celów z kwotą docelową i kolorem
- Pasek postępu dla każdego celu
- Szacowany czas do osiągnięcia celu na podstawie bieżącego bilansu
- Wpłaty do celów z aktualizacją w czasie rzeczywistym
- Wykres liniowy symulacji oszczędzania

### 📈 Raporty
- Trend przychodów i wydatków z ostatnich 6 miesięcy (wykres grupowany)
- Najlepszy i najtrudniejszy miesiąc
- Prognoza z alertem o przekroczeniu budżetu
- Zestawienie tabelaryczne miesięcy
- Top kategorie łącznie z 6 miesięcy
- Donut chart wykorzystania miesięcznego budżetu

### ⚙️ Ustawienia
- Ustawianie miesięcznego budżetu (wpływa na wszystkie obliczenia)
- Przełącznik motywu: ciemny / jasny
- Statystyki bazy danych

---

## 🛠️ Technologie

| Biblioteka | Wersja | Zastosowanie |
|---|---|---|
| **Python** | 3.10+ | Język programowania |
| **CustomTkinter** | 5.2+ | Nowoczesny interfejs użytkownika (dark/light mode) |
| **Matplotlib** | 3.7+ | Wykresy: słupkowe, kołowe, liniowe, donut |
| **NumPy** | 1.24+ | Obliczenia do wykresów |
| **JSON** (stdlib) | — | Lokalne przechowywanie danych |

---

## 📦 Instalacja

### Wymagania wstępne
- Python **3.10** lub nowszy
- pip

### Krok 1 — Sklonuj repozytorium

```bash
git clone https://github.com/TWOJA_NAZWA/budzetapp.git
cd budzetapp
```

### Krok 2 — (Opcjonalnie) Utwórz wirtualne środowisko

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Krok 3 — Zainstaluj zależności

```bash
pip install customtkinter matplotlib numpy
```

Lub jeśli istnieje plik `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uruchomienie

```bash
python main.py
```

> ⚠️ Uruchamiaj **wyłącznie** plik `main.py`, nie `gui/gui.py`.

Przy pierwszym uruchomieniu aplikacja automatycznie:
- Tworzy folder `data/` z plikami JSON
- Wczytuje domyślne kategorie
- Ustawia domyślny budżet miesięczny: **3000 zł**

---

## 🗂️ Struktura projektu

```
budzetapp/
│
├── main.py                  # ▶️ Punkt wejścia — uruchamiaj ten plik
│
├── gui/
│   ├── __init__.py
│   └── gui.py               # 🎨 Layout i wygląd okna (Maja)
│
├── panels.py                # 🖥️ Logika każdego ekranu / widoku (Tomek)
├── charts.py                # 📊 Wykresy matplotlib osadzone w CTkFrame (Tomek)
├── logic.py                 # 🧮 Obliczenia: podsumowania, prognozy, statystyki (Tomek + Alan)
├── data_manager.py          # 🗄️ Zapis i odczyt danych JSON (Alan)
│
├── data/                    # 📁 Dane użytkownika (tworzone automatycznie)
│   ├── transactions.json
│   ├── categories.json
│   ├── goals.json
│   └── settings.json
│
└── requirements.txt
```

---

## 👥 Zespół

| Osoba | Rola | Odpowiedzialność |
|---|---|---|
| **Maja** | 🎨 UI/UX Designer | Layout okna, wygląd, stylizacja (`gui/gui.py`) |
| **Tomek** | ⚙️ Lead Developer | Logika paneli, wykresy, kontrolery (`panels.py`, `charts.py`, `logic.py`) |
| **Alan** | 🗄️ Backend / Data | Warstwa danych, operacje JSON (`data_manager.py`, `logic.py`) |
| **[4. osoba]** | 🔧 Developer | Wsparcie, testowanie, integracja |

---

## 📸 Zrzuty ekranu

### Pulpit
![Dashboard](docs/screenshots/dashboard.png)

### Transakcje
![Transactions](docs/screenshots/transactions.png)

### Raporty
![Reports](docs/screenshots/reports.png)

### Cele oszczędnościowe
![Goals](docs/screenshots/goals.png)

> 📁 Dodaj własne screenshoty do folderu `docs/screenshots/` i odkomentuj powyższe linie.

---

## 📄 Licencja

Projekt na licencji [MIT](LICENSE) — możesz go używać, modyfikować i dystrybuować swobodnie.

---

<div align="center">

Zrobione z 🖤 przez zespół podczas nauki Pythona

</div>
