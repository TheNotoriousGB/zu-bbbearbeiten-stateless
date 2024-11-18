from dataclasses import dataclass
import datetime

# Liste für die Items
items = []


@dataclass
class Item:
    text: str
    date: datetime.datetime
    isCompleted: bool = False


def add(text, date):
    # Text anpassen
    text = text.replace('b', 'bbb').replace('B', 'Bbb')

    # Datum parsen
    date = datetime.datetime.strptime(date, '%Y-%m-%d')

    # Neues Item zur Liste hinzufügen
    items.append(Item(text, date))

    # Sortiere die Items nach Datum (aufsteigend)
    items.sort(key=lambda item: item.date)


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    # Sicherstellen, dass wir auf das richtige Item zugreifen
    item = items[index]
    item.isCompleted = not item.isCompleted  # Status des Items umkehren
