from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Movie(QObject):

    def __init__(self, name, movie_id, description, release_date, path, image):
        QObject.__init__(self)
        self._name = name
        self._movie_id = movie_id
        self._description = description
        self._release_date = release_date
        self._path = path
        self._image = image

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, new_movie_id):
        self._movie_id = new_movie_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, new_release_date):
        self._release_date = new_release_date

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, new_image):
        self._image = new_image





