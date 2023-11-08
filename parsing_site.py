import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd


def get_max_page() -> int:
    response = requests.get("https://bashesk.ru/corporate/tariffs/unregulated/?PAGEN_1=1")
    soup = BeautifulSoup(response.text, 'html.parser')
    max_page = str(soup.find('input', {'data-current-page': '1'})).split()[2].split('"')[1]
    return int(max_page)


def download_file(link_file: object, name_file: str) -> None:
    response = requests.get(link_file)
    with open(name_file, "wb") as file:
        file.write(response.content)


def get_file(number_page: int) -> None:
    pattern_2019 = r"ПУНЦЭМ_до\s*670кВт_(июль|август|сентябрь|октябрь|ноябрь|декабрь)\s*2019\.xls"
    pattern_2020 = r"ПУНЦЭМ_до\s*670кВт_(январь|февраль|март|апрель|май|июнь|июль)\s*2020\.xls"
    try:
        response = requests.get(f"https://bashesk.ru/corporate/tariffs/unregulated/?PAGEN_1={number_page}")
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        for div in soup.find_all("div", class_="col-10"):
            for link in div.find_all("a"):
                link_get = link.get("href")
                if (re.findall(pattern_2019, link_get)) or (re.findall(pattern_2020, link_get)):
                    url_file = f"https://bashesk.ru{link_get}"
                    name_file = url_file.split('/')[6]
                    print(f"Идет загрузка файла --> {name_file} <--")
                    download_file(url_file, name_file)


def read_file() -> None:
    download_folder = os.getcwd()
    for filename in os.listdir(download_folder):
        if filename.endswith(".xls"):  
            file_path = os.path.join(download_folder, filename)
            df = pd.read_excel(file_path, header=None)
            try:
                value = df.iloc[30, 0]
            except IndexError:
                print(f"Значение не найдено в файле: {filename}")
            else:
                print(value)
        

def main():
    max_page = get_max_page()
    for number_page in range(1, (max_page + 1)):
        get_file(number_page)
        
    print('\nВывод значений:')
    read_file()


if __name__ == "__main__":
    main()
    