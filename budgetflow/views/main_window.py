import customtkinter as ctk
from config import APP_NAME, WINDOW_MIN_SIZE, DEFAULT_THEME, COLORS
from views.sidebar import Sidebar
from views.panels.dashboard_panel import DashboardPanel
from utils.event_bus import EventBus

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.minsize(*WINDOW_MIN_SIZE)
        self._sidebar = Sidebar(self, self.on_navigation)
        self._sidebar.grid(row=0, column=0, sticky="ns")
        self._main_content = None
        self._current_panel = None

        # Topbar
        self._topbar = ctk.CTkFrame(self)
        self._topbar.grid(row=0, column=1, sticky="ew", padx=(0,0), pady=(0,0))
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._active_section_title = ctk.CTkLabel(self._topbar, text="Pulpit", font=("Segoe UI", 18, "bold"))
        self._active_section_title.pack(side="left", padx=12, pady=6)
        # Theme switch button
        self._theme_btn = ctk.CTkButton(self._topbar, text="🌙", width=32, command=self.toggle_theme)
        self._theme_btn.pack(side="right", padx=12)
        # Settings button
        self._settings_btn = ctk.CTkButton(self._topbar, text="⚙️", width=32)
        self._settings_btn.pack(side="right", padx=(0, 4))

        EventBus.subscribe("theme_changed", self._on_theme_changed)
        EventBus.subscribe("navigate", self._on_eventbus_navigation)

        self.show_panel("dashboard")

    def _on_theme_changed(self, mode):
        # (Opcjonalnie: zaktualizuj kolory topbaru/MainWindow)
        pass

    def _on_eventbus_navigation(self, panel_name):
        self.show_panel(panel_name)

    def on_navigation(self, panel_name):
        self.show_panel(panel_name)

    def show_panel(self, panel_name: str):
        # Niszczy poprzedni panel, pokazuje żądany
        if self._current_panel is not None:
            self._current_panel.destroy()
            self._current_panel = None

        self._active_section_title.configure(text=self._panel_title(panel_name))

        from views.panels.dashboard_panel import DashboardPanel
        from views.panels.transactions_panel import TransactionsPanel
        from views.panels.categories_panel import CategoriesPanel
        from views.panels.goals_panel import GoalsPanel
        from views.panels.reports_panel import ReportsPanel

        panels = {
            "dashboard": DashboardPanel,
            "transactions": TransactionsPanel,
            "categories": CategoriesPanel,
            "goals": GoalsPanel,
            "reports": ReportsPanel,
        }
        PanelClass = panels.get(panel_name, DashboardPanel)
        self._current_panel = PanelClass(self)
        self._current_panel.grid(row=1, column=1, sticky="nsew", padx=(0,0), pady=(0,0))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def toggle_theme(self):
        import customtkinter as ctk
        current = ctk.get_appearance_mode()
        new_mode = "dark" if current == "light" else "light"
        ctk.set_appearance_mode(new_mode)
        EventBus.publish("theme_changed", new_mode)

    @staticmethod
    def _panel_title(panel_name):
        t = {
            "dashboard": "Pulpit",
            "transactions": "Transakcje",
            "categories": "Kategorie",
            "goals": "Cele",
            "reports": "Raporty",
        }
        return t.get(panel_name, "Pulpit")
