from datetime import date, datetime, timedelta

def format_currency(amount: float, currency: str = "PLN") -> str:
    # "2 340,50 zł"
    return f"{amount:,.2f} zł".replace(",", "X").replace(".", ",").replace("X", " ")

def format_date(d: date) -> str:
    MONTHS = [
        "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
        "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
    ]
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"

def format_month_year(year: int, month: int) -> str:
    MONTHS = [
        "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
        "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
    ]
    return f"{MONTHS[month-1]} {year}"

def get_relative_date(d: date) -> str:
    today = date.today()
    delta = (today - d).days
    if delta == 0:
        return "Dzisiaj"
    elif delta == 1:
        return "Wczoraj"
    elif delta > 1 and delta <= 7:
        return f"{delta} dni temu"
    else:
        return format_date(d)
