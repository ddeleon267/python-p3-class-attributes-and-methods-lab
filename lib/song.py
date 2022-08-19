import ipdb

class Song:
    count = 0
    all = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # ipdb.set_trace()
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_song_to_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)
        cls.add_to_genre_count(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)
        cls.add_to_artist_count(artist)


    @classmethod
    def add_to_genre_count(cls, genre):
        # ipdb.set_trace()
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1