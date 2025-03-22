# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
from main import BooksCollector


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

#1
class TestBooksCollector:

    def test_add_new_book(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ""

import pytest
@pytest.mark.parametrize("book_name", ["", "A" * 41])
def test_add_new_book_invalid_length(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name not in collector.books_genre

#2
class TestBooksCollector:

    def test_set_book_genre_valid(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.books_genre["Гарри Поттер"] == "Фантастика"

    def test_set_book_genre_invalid(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Роман")
        assert collector.books_genre["Гарри Поттер"] == ""


#3
class TestBooksCollector:

    def test_get_book_genre(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

#4
class TestBooksCollector:

    def test_get_books_with_specific_genre(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Джунгли")
        collector.set_book_genre("Джунгли", "Мультфильмы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]


#5
class TestBooksCollector:

    def test_get_books_for_children(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_books_for_children() == ["Гарри Поттер"]

#6
class TestBooksCollector:

    def test_add_book_in_favorites(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.favorites

    def test_add_book_in_favorites_twice(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.favorites.count("Гарри Поттер") == 1

#7
class TestBooksCollector:

    def test_delete_book_from_favorites(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.favorites

#8
class TestBooksCollector:

    def test_get_list_of_favorites_books(collector):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_new_book("Джунгли")
        collector.add_book_in_favorites("Джунгли")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер", "Джунгли"]

#9
class TestBooksCollector:

    def test_get_list_of_favorites_books_empty(collector):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

