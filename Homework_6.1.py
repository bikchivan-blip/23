books = {}

books["B01"] = "Математика"
books["B02"] = "Фізика"
books["B03"] = "Математика" 

print("Пошук за шифром B01:", books.get("B01", "Не знайдено"))

books["B02"] = "Вища фізика"

if "B03" in books:
  del books["B03"]

unique_titles = set(books.values())
print("Унікальні назви книг:", unique_titles)