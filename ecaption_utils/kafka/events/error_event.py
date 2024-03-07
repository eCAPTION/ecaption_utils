from .base_event import BaseEvent


class ErrorEvent(BaseEvent):
    error_type: str
    error_message: str
