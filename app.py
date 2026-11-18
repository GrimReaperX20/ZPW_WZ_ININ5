def powitanie(imie: str) -> None:
    print(f"Cześć, {imie}! Witaj w aplikacji ZPW_WZ_ININ5.")


def pokaz_zadania(zadania: list[str]) -> None:
    print("\nAktualna lista zadań:")
    for idx, zadanie in enumerate(zadania, start=1):
        print(f"{idx}. {zadanie}")


def main() -> None:
    powitanie("Zespół ZPW")
    lista = ["Konfiguracja repozytorium", "Utworzenie tablicy Trello"]
    pokaz_zadania(lista)


if name == "main":
    main()
