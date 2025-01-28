class HashTable:
    def __init__(self, size):
        # Ініціалізація хеш-таблиці заданого розміру
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Хеш-функція для обчислення індексу
        return hash(key) % self.size

    def insert(self, key, value):
        # Додає пару ключ-значення до хеш-таблиці
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # Оновлюємо значення, якщо ключ вже існує
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        
        # Інакше додаємо нову пару
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        # Отримує значення за заданим ключем
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        # Видаляє пару ключ-значення за ключем
        key_hash = self.hash_function(key)
        for i in range(len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

    def __contains__(self, key):
        # Перевіряє, чи існує ключ у таблиці
        return self.get(key) is not None

    def __str__(self):
        # Повертає вміст таблиці як строку
        items = []
        for bucket in self.table:
            for pair in bucket:
                items.append(f"{pair[0]}: {pair[1]}")
        return "\n".join(items)


# Тестуємо нашу хеш-таблицю:
H = HashTable(4)
H.insert("JavaScript", 1)
H.insert("Python", 2)
H.insert("C#", 3)

print("Вся таблиця до видалення елемента:\n", H)  # Вивід всієї таблиці
print(H.get("JavaScript"))  # Отримання значень
print(H.get("Python"))
print(H.get("C#"))

H.delete("C#")  # Видалити елемент за ключем "C#"

print("Вся таблиця після видалення елемента:\n", H)  # Таблиця після видалення
print(H.get("C#"))  # Спроба отримати значення для видаленого ключа (None)