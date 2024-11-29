import xmltodict
import csv
def process_xml(input_file, output_file):
    try:
        with open(input_file, encoding="windows-1251") as rawXml:
            xml_dict = xmltodict.parse(rawXml.read())

        try:
            products = xml_dict["Файл"]["Документ"]["ТаблСчФакт"]["СведТов"]
            if not isinstance(products, list):
                products = [products]  # Если только один элемент, преобразуем в список
        except KeyError as e:
            raise ValueError(f"Ошибка: отсутствует ожидаемый элемент в XML. Детали: {e}")

        with open(output_file, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Товар", "Количество", "Цена"])  # Заголовки

            for product in products:
                name = product.get("@НаимТов", "Не указано")
                quantity = product.get("@КолТов", "0")
                price = product.get("@ЦенаТов", "0")

                writer.writerow([name, quantity, price])
                print(f'Товар: {name}, Количество: {quantity}, Цена: {price}')

        print(f"Данные успешно сохранены в файл: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    process_xml('ex_3.xml', 'output.csv')
