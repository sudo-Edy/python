class Television:
    """A Television object that can be powered on/off, muted, and have its channel and volume changed."""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Set default values for a new Television."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the tv on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the tv (only works if it's on)."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Go up one channel. Wraps back to MIN_CHANNEL after MAX_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Go down one channel. Wraps to MAX_CHANNEL after MIN_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase volume by 1. Unmutes if muted, caps at MAX_VOLUME."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume by 1. Unmutes if muted, stops at MIN_VOLUME."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return a string with the tv's current power, channel, and volume."""
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
