import pandas as pd
from pandas import DataFrame


class Tree:
    """
    Класс для динамического построения дерева Tree и фильтрации объектов на разных уровнях иерархии.

    Args:
        *classifiers (str): Классификаторы, соответствующие уровням иерархии.

    Attributes:
        classifiers (tuple[str]): Кортеж классификаторов.
        data (DataFrame): Загруженные данные из файла 'tree_data.xlsx'.
    """

    def __init__(self, *classifiers: str) -> None:
        """
        Инициализирует объект класса Tree.

        Args:
            *classifiers (str): Классификаторы, соответствующие уровням иерархии.
        """
        self.classifiers = classifiers
        self.data = self.load_data()
        
    def load_data(self) -> DataFrame:
        """
        Загружает данные из файла 'tree_data.xlsx' и возвращает их в виде DataFrame.

        Returns:
            DataFrame: Загруженные данные.

        Raises:
            FileNotFoundError: Если файл 'tree_data.xlsx' не найден.
        """
        try:
            data = pd.read_excel('tree_data.xlsx')  
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Ошибка -> файл не найден!")

    def get_children(self, *filters: tuple[str, str]) -> list[str]:
        """
        Возвращает список объектов на данном уровне иерархии с учетом указанных классификаторов и их значений.

        Args:
            *filters (tuple[str, str]): Пары классификатор-значение для фильтрации.

        Returns:
            list[str]: Список объектов, соответствующих фильтрам.
        """
        children = self.data.copy()  
        for filter_pair in filters:
            classifier, value = filter_pair
            children = children[children[classifier] == value]  
        return children['объект'].tolist()
        