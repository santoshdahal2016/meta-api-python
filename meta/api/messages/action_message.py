class Action:
    """This represent action i.e seen , typing.
    """

    def __init__(self, event):
        assert event != "", "param event must be non empty"
        assert event in (
            "mark_seen",
            "typing_on",
            "typing_off",
        ), 'value of param event must be "mark_seen","typing_on" or "typing_off"'

        self.__event = event

    def set_event(self, event):
        assert event != "", "param event must be non empty"
        assert event in (
            "mark_seen",
            "typing_on",
            "typing_off",
        ), 'value of param event must be "mark_seen","typing_on" or "typing_off"'

        self.__event = str(event)

    def asdict(self):
        """Return the content of the Action object.
        Returns:
            dict: The content of the Action object.
        """

        return {"sender_action": self.__event}
