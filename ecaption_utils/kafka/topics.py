import enum
from .events import (
    NewArticleUrlEvent,
    NewArticleTextEvent,
    MaximalEntityCooccurrenceSetEvent,
)


class Topic(enum.Enum):
    NEW_ARTICLE_URL = "new_article_url"
    NEW_ARTICLE_TEXT = "new_article_text"
    MAXIMAL_ENTITY_COOCCURRENCE_SET = "maximal_entity_cooccurrence_set"


topic_to_type = {
    Topic.NEW_ARTICLE_URL: NewArticleUrlEvent,
    Topic.NEW_ARTICLE_TEXT: NewArticleTextEvent,
    Topic.MAXIMAL_ENTITY_COOCCURRENCE_SET: MaximalEntityCooccurrenceSetEvent,
}


def get_event_type(topic: Topic):
    return topic_to_type[topic]
