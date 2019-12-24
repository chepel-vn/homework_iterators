import os


class WikiLinkGenerator:
    def __init__(self, filename_source):
        self.filename = filename_source
        self.current_record = -1
        self.count_records = 0

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        if self.current_record >= self.count_records:
            raise StopIteration
        return self.get_next_name_country_from_json()

    # Function generator
    def get_next_name_country_from_json(self):
        """

        (string) -> string or None

        Function get iterable information from json file

        """
        try:
            with open(self.filename, encoding="utf8") as file:
                import json
                json_file = json.load(file)
                self.count_records = len(json_file)
                for number, knot in enumerate(json_file, 1):
                    self.current_record = number
                    country = knot["name"]["common"]
                    # country_name_ = str(country_name).replace(' ', '_')
                    # write_to_file("result.txt", country_name, f"https://en.wikipedia.org/wiki/{country_name_}")
                    yield country

        except FileNotFoundError:
            print(f"Файл \"{self.filename}\" не найден.")
        except KeyError:
            print(f"В процедуре чтения файла \"{self.filename}\" задан неверный ключ либо файл имеет другую структуру.")


# Function write to text file
def write_to_file(filename_result, country, country_wiki_link):
    """

    (string) -> None

    Function writes couples "name of country" = "url to internet library on this country" to text file

    """

    try:
        with open(filename_result, "a", encoding="utf8") as file:
            file.write(f"{country} - {country_wiki_link}\n")
            print(f"{country} - {country_wiki_link}")
    except FileNotFoundError:
        with open(filename_result, "w", encoding="utf8") as file:
            file.write(f"{country} - {country_wiki_link}\n")


# Point to enter to program
if __name__ == "__main__":
    filename = "Data\\result.txt"
    source = "Data\\countries.json"

    # Delete file before writing if it exists
    if os.path.exists(filename):
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        os.remove(file_path)

    wk_iterator = WikiLinkGenerator(source).__iter__()

    for country_name in wk_iterator:
        country_name_ = str(country_name).replace(' ', '_')
        write_to_file(filename, country_name, f"https://en.wikipedia.org/wiki/{country_name_}")
