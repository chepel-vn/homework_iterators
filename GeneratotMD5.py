import hashlib


# Function read text file and get hash function md5 from next string of file
def get_next_hash_string_from_file(filename):
    """

    (string) -> hash object or None

    Function get iterable information from text file

    """
    try:
        with open(filename, encoding="utf8") as file:
            for s in file:
                s_md5 = hashlib.md5(s.encode()).hexdigest()
                yield s_md5
    except FileNotFoundError:
        print(f"Файл \"{filename}\" не найден.")
    except KeyError:
        print(f"В процедуре чтения файла \"{filename}\" задан неверный ключ либо файл имеет другую структуру.")


# Point of entry to program
if __name__ == "__main__":
    source = "Data\\result.txt"
    md5_iterator = get_next_hash_string_from_file(source)
    for number, next_md5_hash in enumerate(md5_iterator, 1):
        # pass
        print(f"{number}. {next_md5_hash}")
