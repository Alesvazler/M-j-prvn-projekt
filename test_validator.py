from validator import over_heslo


def test_platne_heslo():
    vysledek, zprava = over_heslo("TajneHeslo1")
    assert vysledek is True
    assert zprava == "Heslo je v pořádku."


def test_kratke_heslo():
    vysledek, zprava = over_heslo("Abc12")
    assert vysledek is False
    assert "alespoň 8 znaků" in zprava


def test_chybi_cislice():
    vysledek, zprava = over_heslo("BezCislice")
    assert vysledek is False
    assert "alespoň jednu číslici" in zprava


def test_chybi_velke_pismeno():
    vysledek, zprava = over_heslo("malapismena1")
    assert vysledek is False
    assert "velké písmeno" in zprava


if __name__ == "__main__":
    test_platne_heslo()
    test_kratke_heslo()
    test_chybi_cislice()
    test_chybi_velke_pismeno()
    print("Všechny testy úspěšně prošly!")