import secrets
import string


def password_generator(
    length = 12,  # длинна пароля'
    use_uppercase = True,
    use_lowercase = True,
    use_digits = True,
    use_symbols = True
) -> str: 
    """
    Генерирует случайный безопасный пароль по заданным параметрам.
    
    :param length: Длина пароля (от 8 до 64)
    :param use_uppercase: Включать заглавные буквы (A-Z)
    :param use_lowercase: Включать строчные буквы (a-z)
    :param use_digits: Включать цифры (0-9)
    :param use_symbols: Включать спецсимволы (#$&!?*)
    :return: Сгенерированный пароль
    :raises ValueError: Если не выбран ни один тип символов
    """

    # Наборы символов
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    numbers = string.digits 
    symbols = "#$&!?*" 


    # Формируем пул доступных символов
    all_chars = ""
    if use_uppercase:
        all_chars += uppercase_chars
    if use_lowercase:
        all_chars += lowercase_chars
    if use_digits:
        all_chars += numbers
    if use_symbols:
        all_chars += symbols


    # Проверка: нельзя генерировать из пустого набора
    if not all_chars:
        raise ValueError("Выберите хотябы один тип символов!")


    # Генерация пароля    
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return(password)

