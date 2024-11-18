from dataclasses import dataclass
import datetime

items = []

@dataclass
class Item:
    text: str
    date: datetime.datetime
    isCompleted: bool = False

def add(text, date):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    # Datum parsen
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    items.append(Item(text, date))

def get_all():
    return items

def get(index):
    return items[index]

def update(index):
    # Hier sicherstellen, dass wir auf das richtige Item zugreifen
    item = items[index]  # Hier holen wir das Item
    item.isCompleted = not item.isCompleted  # Wir ändern den Status des Items
