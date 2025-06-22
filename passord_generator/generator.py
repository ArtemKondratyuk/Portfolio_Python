import secrets
import string


def password_generator(
    length = 12,  # довжина пароля.
    use_uppercase = True,
    use_lowercase = True,
    use_digits = True,
    use_symbols = True
) -> str: 
    """
    Генерує випадковий безпечний пароль за заданими параметрами.
    
    :param length: Довжина пароля (від 8 до 64),
    :param use_uppercase: Включати прописні літери (A-Z),
    :param use_lowercase: Включати рядкові літери (a-z),
    :param use_digits: Включати цифри (0-9),
    :param use_symbols: Включати спецсимволи (#$&!?*),
    :return: Згенерований пароль,
    :raises ValueError: Якщо не обрано жоден тип символів.
    
    """

    # Набір символів.
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    numbers = string.digits 
    symbols = "#$&!?*" 


    # Формує пул доступних символів.
    all_chars = ""
    if use_uppercase:
        all_chars += uppercase_chars
    if use_lowercase:
        all_chars += lowercase_chars
    if use_digits:
        all_chars += numbers
    if use_symbols:
        all_chars += symbols


    # Перевірка: нельзянеможна згенерувати з пустого набору.
    if not all_chars:
        raise ValueError("Select at least one character type!")


    # Генерація пароля.    
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return(password)

