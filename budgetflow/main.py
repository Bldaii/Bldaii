"""
BudgetFlow — Aplikacja do zarządzania budżetem domowym
Uruchomienie: python main.py
"""
import customtkinter as ctk
from views.main_window import MainWindow
from database.db_manager import DBManager

def main():
    # Inicjalizacja bazy danych
    DBManager.get_instance()

    # Konfiguracja CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Uruchomienie aplikacji
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
