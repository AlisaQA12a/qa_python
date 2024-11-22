import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби','Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_one_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_genre_is_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'


    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert not collector.get_book_genre('Что делать, если ваш кот хочет вас убить')

    @pytest.mark.parametrize('name', ['Шерлок Холмс', 'Приглашение на убийство'])
    def test_get_books_with_specific_genre_detective_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == [name]

    @pytest.mark.parametrize('name', ['Лило и Ститч', 'Дядюшка Ау'])
    def test_get_books_genre_one_book_in_list(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        assert collector.get_books_genre() == {name :'Мультфильмы'}

    @pytest.mark.parametrize('name', ['Теория Большого Взрыва', '1+1'])
    def test_get_books_for_children_comedy_in_list(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_one_book_adds_successfull(self):
        collector = BooksCollector()
        collector.add_new_book('Лило и Ститч')
        collector.set_book_genre('Лило и Ститч', 'Мультфильмы')
        collector.add_new_book('Теория Большого Взрыва')
        collector.set_book_genre('Теория Большого Взрыва', 'Комедии')
        collector.add_book_in_favorites('Лило и Ститч')
        assert len(collector.favorites) == 1

    @pytest.mark.parametrize('name', ['Лило и Ститч', 'Дядюшка Ау'])
    def test_delete_book_from_favorites_successfull_delete_one_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 0

    @pytest.mark.parametrize('name', ['Лило и Ститч', 'Дядюшка Ау'])
    def test_get_list_of_favorites_books_one_book_in_list(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

