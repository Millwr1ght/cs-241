import arcade
from music_player import MusicPlayer

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Music test'

# background music
MUSIC_VOLUME = 0.75
SONG_LIST = [
    "./sounds/No Place to Hide.mp3",
    "./sounds/Everpresence.mp3",
    "./sounds/Genesis of the End.mp3"
]

class MusicTest(arcade.Window):
    """ a quick and shoddy python arcade music test class """
    
    def __init__(self, width, height, title):
        """ initialize """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        
        # music
        self.music_player = MusicPlayer(MUSIC_VOLUME, SONG_LIST)
        self.music_player.setup()
        
    def on_update(self, delta_time):
        """ update the music player 
        the arcade documentation says music updates go in on_update() instead of in update() 
        """
        self.music_player.update()
    
    def on_key_press(self, key: int, modifiers: int):
        """ """
        if key == arcade.key.PERIOD:  # . or >
            self.music_player.advance_song()
            self.music_player.play_song()

        if key == arcade.key.COMMA:  # , or <
            self.music_player.go_back()
            self.music_player.play_song()
        
        if key == arcade.key.T:
            self.music_player.test()
        
        if key == arcade.key.SPACE:
            self.music_player.setup()
        
window = MusicTest(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()