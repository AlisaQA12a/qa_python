import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_one_book(self, book):
        assert len(book.get_books_genre()) == 1

    def test_set_book_genre_genre_is_in_list(self, book):
        book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert book.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'


    def test_get_book_genre_book_without_genre(self, book):
        assert not book.get_book_genre('Гордость и предубеждение и зомби')

    @pytest.mark.parametrize('name', ['Шерлок Холмс', 'Приглашение на убийство'])
    def test_get_books_with_specific_genre_detective_genre(self,collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == [name]


    def test_get_books_genre_one_book_in_list(self, book):
        book.set_book_genre('Гордость и предубеждение и зомби', 'Мультфильмы')
        assert book.get_books_genre() == {'Гордость и предубеждение и зомби' :'Мультфильмы'}

    @pytest.mark.parametrize('name', ['Теория Большого Взрыва', '1+1'])
    def test_get_books_for_children_detective_does_not_return_in_list(self,collector, name):
        collector.add_new_book(name)
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre(name, 'Комедии')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_one_book_adds_successfully(self, collector):
        collector.add_new_book('Лило и Ститч')
        collector.add_new_book('Теория Большого Взрыва')
        collector.add_book_in_favorites('Лило и Ститч')
        assert len(collector.favorites) == 1


    def test_delete_book_from_favorites_successfully_delete_one_book(self,book):
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(book.favorites) == 0


    def test_get_list_of_favorites_books_one_book_in_list(self, book):
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert book.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

