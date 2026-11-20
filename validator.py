def over_heslo(heslo: str) -> tuple[bool, str]:
    """Zkontroluje, zda heslo splňuje základní bezpečnostní pravidla."""
    if len(heslo) < 8:
        return False, "Heslo musí mít alespoň 8 znaků."
    if not any(znak.isdigit() for znak in heslo):
        return False, "Heslo musí obsahovat alespoň jednu číslici."
    if not any(znak.isupper() for znak in heslo):
        return False, "Heslo musí obsahovat alespoň jedno velké písmeno."
    return True, "Heslo je v pořádku."


if __name__ == "__main__":
    # Rychlé ruční otestování
    testovaci_hesla = ["abc", "heslo123", "Heslo123"]
    for h in testovaci_hesla:
        vysledek, zprava = over_heslo(h)
        print(f"Heslo '{h}': {vysledek} -> {zprava}")