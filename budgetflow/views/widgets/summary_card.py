import customtkinter as ctk
from config import CARD_CORNER_RADIUS, COLORS

class SummaryCard(ctk.CTkFrame):
    """
    Karta wyświetlająca: ikonę, tytuł, wartość główną, podtytuł/zmianę.
    Przykład: 🏦 "Saldo" / "2 340,50 zł" / "+12% vs poprzedni miesiąc"
    """
    def __init__(self, master, icon: str, title: str,
                 value: str, subtitle: str = "", color: str = None):
        super().__init__(master, corner_radius=CARD_CORNER_RADIUS)
        self.icon_lbl = ctk.CTkLabel(self, text=icon, font=("Segoe UI", 22))
        self.icon_lbl.grid(row=0, column=0, rowspan=2, padx=10, sticky="w")

        self.title_lbl = ctk.CTkLabel(self, text=title, font=("Segoe UI", 13, "bold"))
        self.title_lbl.grid(row=0, column=1, sticky="w", padx=5, pady=(8, 0))
        self.value_lbl = ctk.CTkLabel(
            self, text=value, font=("Segoe UI", 17, "bold"), text_color=color or COLORS["primary"]
        )
        self.value_lbl.grid(row=1, column=1, sticky="w", pady=(0, 8), padx=5)
        self.subtitle_lbl = ctk.CTkLabel(self, text=subtitle, font=("Segoe UI", 11))
        self.subtitle_lbl.grid(row=2, column=1, sticky="w", padx=5, pady=(0, 6))

        self.grid_columnconfigure(1, weight=1)

    def update_value(self, value: str, subtitle: str = ""):
        self.value_lbl.configure(text=value)
        self.subtitle_lbl.configure(text=subtitle)
