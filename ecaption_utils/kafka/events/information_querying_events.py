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
    entity_labels: dict[int, str]


class NewsSearchResultsEvent(InformationQueryingComponentEvent):
    title: str
    description: str
    image: str
    related_articles: list[dict[str, str]]

    # For the graph image
    adjlist: dict[int, list[int]]
    node_occurrences: dict[int, int]
    entity_labels: dict[int, str]


class InformationQueryingComponentResultsEvent(InformationQueryingComponentEvent):
    title: str
    description: str
    image: str
    related_articles: list[dict[str, str]]
    related_facts: list[str]

    # For the graph image
    adjlist: dict[int, list[int]]
    node_occurrences: dict[int, int]
    entity_labels: dict[int, str]
