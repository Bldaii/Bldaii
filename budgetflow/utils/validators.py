from datetime import datetime, date

class ValidationError(Exception):
    pass

def validate_amount(value: str) -> float:
    try:
        val = float(value.replace(",", ".").replace(" ", ""))
        if val <= 0:
            raise ValidationError("Kwota musi być większa od zera.")
        return val
    except Exception:
        raise ValidationError("Niepoprawna kwota.")

def validate_date(value: str) -> date:
    formats = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"]
    for f in formats:
        try:
            return datetime.strptime(value, f).date()
        except ValueError:
            continue
    raise ValidationError("Niepoprawna data. Dozwolone formaty: YYYY-MM-DD, DD.MM.YYYY, DD/MM/YYYY")

def validate_not_empty(value: str, field_name: str) -> str:
    if not value.strip():
        raise ValidationError(f"Pole '{field_name}' nie może być puste.")
    return value

def validate_percentage(value: float) -> float:
    if not (0.0 <= value <= 100.0):
        raise ValidationError("Procent musi być w zakresie 0–100.")
    return value
