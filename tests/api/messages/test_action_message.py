from meta.api.messages.action_message import Action , SenderAction
import pytest


def test_creation():
    action_message = Action(SenderAction.MARK_SEEN)

    assert action_message.event == SenderAction.MARK_SEEN


def test_creation_fail():

    with pytest.raises(ValueError, match="value of param event must be 'mark_seen', 'typing_on', or 'typing_off'"):
        Action("wrong_type")


def test_asdict():
	message_dict = dict(
		sender_action=SenderAction.TYPING_OFF
	)

	action_message_dict = Action(SenderAction.TYPING_OFF).asdict()

	assert message_dict == action_message_dict
