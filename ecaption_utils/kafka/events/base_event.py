import faust


class BaseEvent(faust.Record):
    request_id: int
