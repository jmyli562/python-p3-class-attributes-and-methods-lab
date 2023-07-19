class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.increment_song_count()
        Song.add_song_genre(genre)
        Song.add_song_artist(artist)

    @classmethod
    def increment_song_count(cls):
        cls.count += 1

    @classmethod
    def add_song_genre(cls, genres):
        if genres not in Song.genres:
            cls.genres.append(genres)
            Song.genre_count[genres] = 1
        else:
            Song.genre_count[genres] += 1

    @classmethod
    def add_song_artist(cls, artist):
        if artist not in Song.artists:
            cls.artists.append(artist)
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
