import unittest
from app import app
from movie import Movie


class MovieTest(unittest.TestCase):

    def setUp(self):

        self.new_movie = Movie(1234, 'Python Must Be Crazy',
                               'A thrilling new python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 1239990)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie
                                   ))


if __name__ == '__main__':
    unittest.main()
