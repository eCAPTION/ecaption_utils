import enum
from .events import (
    NewArticleUrlEvent,
    NewArticleExtractedEvent,
    MaximalEntityCooccurrenceSetEvent,
    NewsEmbeddingEvent,
    NewsSearchResultsEvent,
)


class Topic(enum.Enum):
    NEW_ARTICLE_URL = "new_article_url"
    NEW_ARTICLE_EXTRACTED = "new_article_extracted"
    MAXIMAL_ENTITY_COOCCURRENCE_SET = "maximal_entity_cooccurrence_set"
    NEWS_EMBEDDING = "news_embedding"
    NEWS_SEARCH_RESULTS = "news_search_results"


topic_to_type = {
    Topic.NEW_ARTICLE_URL: NewArticleUrlEvent,
    Topic.NEW_ARTICLE_EXTRACTED: NewArticleExtractedEvent,
    Topic.MAXIMAL_ENTITY_COOCCURRENCE_SET: MaximalEntityCooccurrenceSetEvent,
    Topic.NEWS_EMBEDDING: NewsEmbeddingEvent,
    Topic.NEWS_SEARCH_RESULTS: NewsSearchResultsEvent,
}


def get_event_type(topic: Topic):
    return topic_to_type[topic]
