from collections import deque


class Song:
    """ vars: title: '', artist: ''; methods: prompt(), display() """

    def __init__(self, song_title='Untitled', song_artist='Unknown'):
        """ set up variables, assign default values """
        self.title = song_title
        self.artist = song_artist

    def prompt(self):
        """ ask for the name and artist of the Song """
        self.name = input('Song title: ')
        self.artist = input('Artist: ')

    def display(self):
        """ output the name and artist of the Song """
        print(f'"{self.name}" by {self.artist}')


def check_len(queue):
    if len(queue) <= 0:
        return False
    else:
        # has elements
        return True


def main():
    """ a main loop that asks the user for one of the following options:
         - Add new song to the end of the playlist.
         - Insert a new song at the beginning of the playlist (so it will play next).
         - Play a song (this should remove it from the playlist). """

    playlist = deque()
    choice = ''
    while choice.lower() != 'quit' or choice != '4':
        print('Options:')
        print('1. Add a new song to the end of the playlist')
        print('2. Insert a new song to the beginning of the playlist')
        print('3. Play the next song')
        print('4. Quit')
        choice = input('Enter selection: ')

        if choice.lower() == '1':
            # add to end of playlist

            new_song = Song()
            new_song.prompt()
            playlist.append(new_song)

        elif choice.lower() == '2':
            # add song to beginning of playlist

            new_song = Song()
            new_song.prompt()
            playlist.appendleft(new_song)

        elif choice.lower() == '3':
            # play the top song, and remove it
            if check_len(playlist):
                print('Playing:')
                song = playlist.popleft()
                song.display()
            else:
                print('This playlist is empty!')

        # debug
        elif choice.lower() == '5':
            # add song to beginning of playlist
            for song in playlist:
                song.display()

        else:
            print('Please make a valid selection.')

if __name__ == '__main__':
    main()