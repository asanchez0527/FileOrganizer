class Movie:
    def __init__(self, name, movie_id, description, release_date, path, image):
        self.name = name
        self.movie_id = movie_id
        self.description = description
        self.release_date = release_date
        self.path = path
        self.image = image

    def summary(self):
        return ("Name: " + self.name + "\n" + "Release date: " +
                self.release_date + "\n" + "Description: " + self.description + "\n"
                + "Path: " + self.path + "\n" + "Image: " + self.image + "\n")
