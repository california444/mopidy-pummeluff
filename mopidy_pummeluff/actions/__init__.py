'''
Python module for Mopidy Pummeluff tags.
'''

__all__ = (
    'PlayPause',
    'Stop',
    'PreviousTrack',
    'NextTrack',
    'Shutdown',
    'Tracklist',
    'ToggleShuffle',
    'Volume',
    'VolumeUp',
    'VolumeDown',
)

from .playback import NextTrack, PlayPause, PreviousTrack, Stop
from .shutdown import Shutdown
from .tracklist import ToggleShuffle, Tracklist
from .volume import Volume, VolumeUp, VolumeDown


ACTIONS = {}
for action in __all__:
    ACTIONS[action] = globals()[action].__doc__.strip()
