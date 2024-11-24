import pytest
from main import BooksCollector


@pytest.fixture()
def book():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector