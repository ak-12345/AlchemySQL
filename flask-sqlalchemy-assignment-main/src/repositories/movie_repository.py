class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return Movie.query.all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return Movie.query.filter_by(movie_id=movie_id).all()

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        #Creating a movie int he database
        new_movie = Movie(title=title, director=director, rating=rating)
        return db.session.add(new_movie)

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        #Returning all movies matching the name
        Movie.query.filter(Movie.name.like(title=title)).all()
        return Movie.title.like(title=title)


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
