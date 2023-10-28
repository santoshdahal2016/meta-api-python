from dataclasses import dataclass
from abc import abstractmethod, abstractclassmethod
from metapython.api.consts import MessagingType, NotificationType


@dataclass
class Message:
    messaging_type: str = MessagingType.RESPONSE
    notification_type: str = NotificationType.REGULAR

    def asdict(self):
        return {
            "messaging_type": self.messaging_type,
            "notification_type": self.notification_type,
        }
