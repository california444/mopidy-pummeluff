'''
Python module for Mopidy Pummeluff volume tag.
'''

__all__ = (
    'Volume',
    'VolumeUp',
    'VolumeDown',
)

from logging import getLogger

from .base import Action

LOGGER = getLogger(__name__)


class Volume(Action):
    '''
    Sets the volume to the percentage value retreived from the tag's parameter.
    '''

    @classmethod
    def execute(cls, core, volume):  # pylint: disable=arguments-differ
        '''
        Set volume of the mixer.

        :param mopidy.core.Core core: The mopidy core instance
        :param volume: The new (percentage) volume
        :type volume: int|str
        '''
        LOGGER.info('Setting volume to %s', volume)
        try:
            core.mixer.set_volume(int(volume))
        except ValueError as ex:
            LOGGER.error(str(ex))

    def validate(self):
        '''
        Validates if the parameter is an integer between 0 and 100.

        :param mixed parameter: The parameter

        :raises ValueError: When parameter is invalid
        '''
        super().validate()

        try:
            number = int(self.parameter)
            assert 0 <= number <= 100
        except (ValueError, AssertionError):
            raise ValueError('Volume parameter has to be a number between 0 and 100')

class VolumeUp(Action):
    '''
    sets the volume up by 5%
    '''
    @classmethod
    def execute(cls, core):
        '''
        Set volume of the mixer.
        '''
        number = int(core.mixer.get_volume())
        if (number < 95):
            number = number + 5
            LOGGER.info('Setting volume to %s', number)
            core.mixer.set_volume(number)
        else:
            core.mixer.stes_volume(100)
            LOGGER.info('Setting volume to 100')

class VolumeDown(Action):
    '''
    sets the volume down by 5%
    '''
    @classmethod
    def execute(cls, core):
        '''
        Set volume of the mixer.
        '''
        number = int(core.mixer.get_volume())
        if (number > 5):
            number = number - 5
            LOGGER.info('Setting volume to %s', number)
            core.mixer.set_volume(number)
        else:
            core.mixer.stes_volume(0)
            LOGGER.info('Setting volume to 0')
