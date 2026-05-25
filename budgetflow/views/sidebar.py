import customtkinter as ctk
from config import APP_NAME, SIDEBAR_WIDTH, COLORS
from utils.event_bus import EventBus

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_nav_callback=None):
        super().__init__(master, width=SIDEBAR_WIDTH)
        self.on_nav_callback = on_nav_callback
        self.configure(width=SIDEBAR_WIDTH)
        self.active_panel = "dashboard"

        # Logo i nazwa
        self.label = ctk.CTkLabel(self, text=APP_NAME, font=("Segoe UI", 19, "bold"))
        self.label.pack(pady=(10, 30))

        # Przyciski nawigacyjne
        self.buttons = {}
        menu_items = [
            ("dashboard", "Pulpit", "🏠"),
            ("transactions", "Transakcje", "💸"),
            ("categories", "Kategorie", "📦"),
            ("goals", "Cele", "🎯"),
            ("reports", "Raporty", "📊"),
        ]
        for ident, label, emoji in menu_items:
            btn = ctk.CTkButton(
                self, text=f"{emoji} {label}", width=SIDEBAR_WIDTH-20,
                fg_color=self._get_fg(ident), command=lambda x=ident: self._on_click(x),
                anchor="w"
            )
            btn.pack(pady=2, padx=10)
            self.buttons[ident] = btn

        # Spacer
        ctk.CTkLabel(self, text="").pack(expand=True, fill="y")

        # Saldo miesięczne (dummy, docelowo podpiąć EventBus i TransactionController)
        self.balance_label = ctk.CTkLabel(self, text="Saldo: -- zł", font=("Segoe UI", 13, "bold"))
        self.balance_label.pack(pady=(10, 14))

        EventBus.subscribe("data_refreshed", self._refresh_balance)
        self._refresh_balance(None)

    def _on_click(self, panel_name):
        self.active_panel = panel_name
        for ident, btn in self.buttons.items():
            btn.configure(fg_color=self._get_fg(ident))
        # Publikacja eventu
        EventBus.publish("navigate", panel_name)
        if self.on_nav_callback:
            self.on_nav_callback(panel_name)

    def _get_fg(self, ident):
        return COLORS["primary"] if ident == self.active_panel else "transparent"

    def _refresh_balance(self, _):
        # Docelowo: pobierz z TransactionController.monthly_summary/balance
        self.balance_label.configure(text="Saldo: -- zł")
