from .base_event import BaseEvent


class InformationQueryingComponentEvent(BaseEvent):
    url: str


class NewArticleUrlEvent(InformationQueryingComponentEvent):
    pass


class NewArticleExtractedEvent(InformationQueryingComponentEvent):
    title: str
    description: str
    text: str
    image: str


class MaximalEntityCooccurrenceSetEvent(InformationQueryingComponentEvent):
    maximal_entity_cooccurrence_set: list[list[str]]


class NewsEmbeddingEvent(InformationQueryingComponentEvent):
    node_occurrences: dict[int, int]
    adjlist: dict[int, list[int]]


class NewsSearchResultsEvent(InformationQueryingComponentEvent):
    results: list[dict[str, str]]
