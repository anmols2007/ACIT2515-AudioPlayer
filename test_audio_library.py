import unittest
import inspect
from datetime import time
from song import Song
from podcast import Podcast
from playlist import PlayList
from audio_library import AudioLibrary


class TestAudioLibrary(unittest.TestCase):
    """
    Authors: Anmol Anand(A01174846), Felix Ruttan(A01070306), 
    Nicholas Janus(A01179897)
    """

    def setUp(self):
        """called before every test method"""
        self.logPoint()
        self.library = AudioLibrary()
        self.song1 = Song('Crazy', 'Gnarls Barkley','St. Elsewhere', '3:02', "music/", "crazy.mp3")
        self.podcast1 = Podcast('Startalk', "Neil deGrasse Tyson", "56:02", "podcasts/", "startalk.mp3", "2020", "18", time(0, 15, 23), 12)
        self.playlist1 = PlayList('study time', "playlist for my study sessions")
        self.library.add_playlist(self.playlist1)
        self.library.add_podcast(self.podcast1)
        self.library.add_song(self.song1)
    
    def tearDown(self):
        """called after every test method"""
        self.logPoint()

    def test_init(self):
        """1A: tests the constructor"""
        pass

    def test_add_song(self):
        """tests the test_song method"""
        self.library.add_song(self.song1)

        self.assertIn(self.song1, self.library.get_song_list())

    def test_add_podcast(self):
        """tests the add_podcast method"""
        self.library.add_podcast(self.podcast1)

        self.assertIn(self.podcast, self.library.get_playlist_list())
    
    def test_add_playlist(self):
        """tests the add_playlist method"""
        self.library.add_playlist(self.playlist1)

        self.assertIn(self.playlist1, self.get_playlist_list())

    def test_remove_song(self):
        """tests the remove_song method"""
        self.library.remove_song(self.song1)

        self.assertNotIn(self.song1, self.library.get_song_list())
    
    def test_remove_podcast(self):
        """tests the remove_podcast method"""
        self.library.remove_podcast(self.podcast1)

        self.assertNotIn(self.podcast1, self.get_podcast_list())

    def test_remove_playlist(self):
        """tests the remove_playlist method"""
        self.library.remove_playlist(self.playlist1)

        self.assertNotIn(self.playlist1, self.library.get_playlist_list())

    def test_get_song_list(self):
        """tests the get_song_list method"""
        expected_output = [self.song1]

        self.assertEqual(self.get_song_list, expected_output)
    
    def test_get_podcast_list(self):
        """tests the get_podcast_list method"""
        expected_output = [self.podcast1]

        self.assertEqual(self.get_podcast_list, expected_output)

    def test_get_playlist_list(self):
        """tests the get_playlist_list method"""
        expected_output = [self.playlist1]

        self.assertEqual(self.get_playlist_list, expected_output)
    
    def test_number_of_songs(self):
        """tests the number_of_songs method"""
        expected_output = 1

        self.assertEqual(self.library.number_of_songs(), expected_output)
    
    def test_number_of_podcasts(self):
        """tests the number_of_podcasts method"""
		self.podcast2 = Podcast('BCIT speaks', "Anmol", "58:05", "podcasts/", "bcit_speaks.mp3", "2", "2020", time(0, 15, 23), 10)
        self.library.add_podcast(self.podcast2)
        expected_output = 2

        self.assertEqual(self.library.number_of_podcasts(), expected_output)
    
    def test_number_of_playlists(self):
        """test the number_of_playlists method"""
        self.playlist2 = PlayList('Workout', 'Gym time and marathons')
        self.playlist3 = PlayList('Transit', 'Help me pass the time in the SkyTrain')
        self.library.add_playlist(playlist2)
        self.library.add_playlist(playlist3)
        expected_output = 3

        self.assertEqual(self.library.number_of_playlists(), expected_output)
        
    def logPoint(self):
        """utility method to trace control flow"""
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s -%s()' % (currentTest, callingFunction))


if __name__ == "__main__":
    unittest.main()
