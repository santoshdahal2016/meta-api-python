from meta.api.consts import SenderAction
from dataclasses import dataclass, asdict

@dataclass
class Action:
    """This represent action i.e seen , typing.
    """
    event: str

    def __post_init__(self):
        self.__validate_event()

    def asdict(self):
        """Return the content of the Action object.
        Returns:
            dict: The content of the Action object.
        """
        return {"sender_action": self.event}

    def __validate_event(self):

        """Private method to validate the event."""
        if  self.event not  in (SenderAction.MARK_SEEN, SenderAction.TYPING_ON, SenderAction.TYPING_OFF):
            raise ValueError("value of param event must be 'mark_seen', 'typing_on', or 'typing_off'")

            

