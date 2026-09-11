import random
import string


def generate_password(length=12):
    """Генерирует надёжный случайный пароль."""
    if length < 4:
        return "Ошибка: Длина пароля должна быть не менее 4 символов!"

    # Собираем группы символов
    lowercase = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    uppercase = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits  # 0123456789
    symbols = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Гарантируем, что в пароле будет ХОТЯ БЫ один символ из каждой группы
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Объединяем все символы вместе для генерации остальной части пароля
    all_characters = lowercase + uppercase + digits + symbols

    # Добираем оставшуюся длину случайными символами
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Перемешиваем символы, чтобы первые 4 не шли строго по порядку
    random.shuffle(password)

    # Собираем список в одну строку и возвращаем
    return "".join(password)


def check_password_strength(password):
    """Проверяет сложность пароля и возвращает оценку."""
    score = 0
    feedback = []

    # Проверка длины
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Слишком короткий (желательно от 8 символов).")

    # Проверка на строчные буквы
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Добавь маленькие буквы (a-z).")

    # Проверка на заглавные буквы
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Добавь заглавные буквы (A-Z).")

    # Проверка на цифры
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Добавь цифры (0-9).")

    # Проверка на спецсимволы
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("⚠️ Добавь спецсимволы (напр. @, #, $, %).")

    # Выставляем вердикт
    if score <= 2:
        verdict = "❌ СЛАБЫЙ ПАРОЛЬ"
    elif score <= 4:
        verdict = "⚠️ СРЕДНИЙ ПАРОЛЬ"
    else:
        verdict = "✅ ОЧЕНЬ НАДЁЖНЫЙ ПАРОЛЬ"

    return verdict, feedback


def main():
    """Главное меню программы."""
    print("=== МЕНЕДЖЕР БЕЗОПАСНОСТИ ПАРОЛЕЙ ===")

    while True:
        print("\nЧто ты хочешь сделать?")
        print("1. Сгенерировать пароль")
        print("2. Проверить существующий пароль")
        print("3. Выйти из программы")

        choice = input("Выбери пункт (1/2/3): ").strip()

        if choice == "1":
            try:
                length = int(input("Введите желаемую длину пароля: "))
                new_password = generate_password(length)
                print(f"\nТвой новый надежный пароль: {new_password}")
            except ValueError:
                print("Ошибка: Нужно ввести целое число!")

        elif choice == "2":
            user_password = input("Введи пароль для проверки: ")
            verdict, tips = check_password_strength(user_password)

            print(f"\nРезультат: {verdict}")
            if tips:
                print("Как улучшить:")
                for tip in tips:
                    print(tip)

        elif choice == "3":
            print("Удачи, бро! Безопасность превыше всего.")
            break
        else:
            print("Неверный выбор. Введи 1, 2 or 3.")


# Запуск программы
if __name__ == "__main__":
    main()
