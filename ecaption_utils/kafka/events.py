import faust


class InformationQueryingComponentEvent(faust.Record):
    url: str


class NewArticleUrlEvent(InformationQueryingComponentEvent):
    request_id: int


class NewArticleTextEvent(InformationQueryingComponentEvent):
    text: str


class MaximalEntityCooccurrenceSetEvent(InformationQueryingComponentEvent):
    maximal_entity_cooccurrence_set: list[list[str]]


class NewsEmbeddingEvent(InformationQueryingComponentEvent):
    node_occurrences: dict[int, int]
    adjlist: dict[int, list[int]]
