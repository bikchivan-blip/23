text = input("Введіть рядок: ")

chars = set(text)

print("Кількість унікальних літер/символів:", len(chars))

unique_once = {c for c in chars if text.count(c) == 1}
print("Символи, що зустрічаються лише один раз:", unique_once)