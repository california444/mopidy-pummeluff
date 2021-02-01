Mopidy Pummeluff
================

Copy of original Pumeluff repo with following changes:
- GPIO Handler disabled so that different GPIO plugin (e.g. mopidy-raspberry-gpio) can be used
- Modification that the same RFID is not triggered again (e.g. when RFID tag stays on the RFID reader an is read and read again)
- Support for Volume down and Volume up (eg via buttons), but not used
- integrated pivoyager into shutdown procedure if RFID tag for shutdown action is read
- changed sound file format to mp3
