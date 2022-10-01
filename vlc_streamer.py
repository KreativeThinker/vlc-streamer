"""
Github: https://www.github.com/KreativeThinker/vlc-streamer

TODO: Add better documentation for all classes and functions
TODO: Add Lyrics class
"""

from pprint import pprint
from typing import Callable

import ytm  # type: ignore
import vlc  # type: ignore
import pafy  # type: ignore


class Search:
    """
    Search class
    """

    def __init__(self) -> None:
        self.more: dict = {
            "songs": None,
            "artists": None,
            "albums": None,
            "playlists": None
        }
        self.api = ytm.YouTubeMusic()  # type: ignore

    def search(self, query: str) -> dict:
        """
        Search for songs, artists, albums and playlists
        :param query: str, keyword(s) for search.
        :return: dict - songs, artists, albums and playlists
        """
        songs: dict = self.api.search_songs(query)
        artists: dict = self.api.search_artists(query)
        albums: dict = self.api.search_albums(query)
        playlists: dict = self.api.search_playlists(query)

        results: dict = {
            "songs": songs["items"],
            "artists": artists["items"],
            "albums": albums["items"],
            "playlists": playlists["items"],
        }

        self.more["songs"] = songs["continuation"]
        self.more["artists"] = artists["continuation"]
        self.more["albums"] = albums["continuation"]
        self.more["playlists"] = playlists["continuation"]

        return results

    def more_songs(self) -> list:
        """
        Searches for more songs results using saved continuation query
        :return: List of songs in continuation
        """
        if self.more["songs"] is None:
            return []

        songs: dict = self.api.search_songs(continuation=self.more["songs"])
        self.more["songs"] = songs["continuation"]
        return songs["items"]

    def more_artists(self) -> list:
        """
        Searches for more artists results using saved continuation query
        :return: List of artists in continuation
        """
        if self.more["artists"] is None:
            return []

        artists: dict = self.api.search_artists(continuation=self.more["artists"])
        self.more["artists"] = artists["continuation"]
        return artists["items"]

    def more_albums(self) -> list:
        """
        Searches for more albums results using saved continuation query
        :return: List of albums in continuation
        """
        if self.more["albums"] is None:
            return []

        albums: dict = self.api.search_albums(continuation=self.more["albums"])
        self.more["albums"] = albums["continuation"]
        return albums["items"]

    def more_playlists(self) -> list:
        """
        Searches for more playlists results using saved continuation query
        :return: List of playlists in continuation
        """
        if self.more["playlists"] is None:
            return []

        playlists: dict = self.api.search_playlists(continuation=self.more["playlists"])
        self.more["playlists"] = playlists["continuation"]
        return playlists["items"]

    def more_all(self) -> dict:
        """
        Searches for more results of
        songs,
        artists,
        albums and
        playlists.
        :return: Dict of all results
        """
        results: dict = {
            "songs": self.more_songs(),
            "artists": self.more_artists(),
            "albums": self.more_albums(),
            "playlists": self.more_playlists()
        }
        return results


class MediaPlayer:
    """
    MediaPlayer class.
    current_media["state"] = {
        -1: "Paused",
        0: "Idle",
        1: "Playing"
    """

    def __init__(self) -> None:
        self.current_media: dict = dict(
            name=None,
            id=None,
            artists=None,
            album=None,
            duration=None,
            state=0
        )
        self.queue: list[dict] = []
        self.player = vlc.MediaPlayer()

    # TODO: Remove default link. It is only for easy debugging.
    def load_media(self, media_id: str = "U-zySoZ4GTA") -> None:
        """
        Load media mrl to `self.player`
        :param media_id: media id as searched by `Search.search(query)`
        """
        media = pafy.new(media_id).getbestaudio().url
        self.player.set_mrl(media)
        self.current_media["state"] = 0

    def play(self) -> None:
        """
        Play audio and set current media state as playing (1)
        """
        self.player.play()
        self.current_media["state"] = 1

    def pause(self, pause_callback: Callable = print) -> None:
        """
        Pause/Play the media
        :param pause_callback: function, called whenever media is paused/played
        """
        self.player.pause()
        self.current_media["state"] *= -1
        pause_callback(self.current_media["state"])

        # TODO: Create the following functions:-
        #     1.    stop() --- stop all media including queue
        #     2.    next() --- skip to next song
        #     3.    prev() --- return to start/previous song
        #     4.    queue_media() --- add media to queue
        #     5.    view_queue() --- return list of queued media
        #     6.    download_media() --- downloads selected/current media
        #     7.    media_fetch_data() --- returns metadata


if __name__ == "__main__":
    v = Search()
    while True:
        i = int(input(
            """
            1. search all
            2. search more songs
            3. search more artists
            4. search more albums
            5. search more playlists
            6. search more all
            0. exit
            >>> """
        ))

        if i == 1:
            s = input("Query: ")
            pprint(v.search(s))

        elif i == 2:
            pprint(v.more_songs())

        elif i == 3:
            pprint(v.more_artists())

        elif i == 4:
            pprint(v.more_albums())

        elif i == 5:
            pprint(v.more_playlists())

        elif i == 6:
            pprint(v.more_all())

        elif i == 0:
            break
