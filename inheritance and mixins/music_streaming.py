class ShareMixin:
    def share(self, friend):
        print(f"{self.song} shared with {friend}")

class LikeMixin:
    def like(self):
        print(f"You liked {self.song}")

class Song:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist

class Playlist(Song, ShareMixin, LikeMixin):
    pass

track = Playlist("Shape of You", "Ed Sheeran")
track.like()
track.share("Rahul")
