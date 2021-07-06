"""
File: music_player.py
Author: N Johnston

A python arcade background music player for arcade games
"""
from arcade import Sound
from time import sleep


class MusicPlayer:
    """
    the music player class

    volume: float
    bgm_list: List
    music: arcade.Sound()
    current_song_index: int
    current_player: aracde.Sound().play()

    - __init__(): None
    + advance_song(): None
    + go_back(): None
    - play_song(): None
    + setup(): None
    + update(): None
    """

    def __init__(self, volume: float, song_list: list):
        """ initialize instance """

        # Variables used to manage our music. See setup() for giving them
        # values.
        self.volume = volume
        self.bgm_list = song_list
        self._current_song_index = 0
        self.current_player = None
        self.music = None

    @property
    def current_song_index(self):
        """ getter """
        return self._current_song_index

    @current_song_index.setter
    def current_song_index(self, value):
        """ setter """
        if self._current_song_index + value >= len(self.bgm_list):
            self._current_song_index = 0
        else:
            self._current_song_index = value

    def advance_song(self):
        """ moves the song forward one """
        self.current_song_index += 1

    def go_back(self):
        """ moves the song back one """
        self.current_song_index -= 1

    def play_song(self):
        """ play a song in the list """
        # Stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)

        # Play the song
        self.music = Sound(
            self.bgm_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(self.volume)
        # Apparently, if you don't do this next part, the elapsed time is 0.0 and on_update will
        # think the music is over and advance to the next song before starting this one.
        sleep(0.03)

    def setup(self):
        """ starts playing the first song """
        # Go to first
        self.current_song_index = 0
        # Play the song
        self.play_song()

    def update(self):
        """ handle what happens when the end of the song is reached """
        position = self.music.get_stream_position(self.current_player)

        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
            self.advance_song()
            self.play_song()
