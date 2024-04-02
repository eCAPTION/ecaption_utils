import enum
from .events.information_querying_events import (
    NewArticleUrlEvent,
    NewArticleExtractedEvent,
    MaximalEntityCooccurrenceSetEvent,
    NewsEmbeddingEvent,
    NewsSearchResultsEvent,
    InformationQueryingComponentResultsEvent,
)
from .events.error_event import ErrorEvent
from .events.chatbot_events import (
    AddInstructionEvent,
    DeleteInstructionEvent,
    MoveInstructionEvent,
    NewInfographicEvent,
    ModifiedInfographicEvent,
)


class Topic(enum.Enum):
    NEW_ARTICLE_URL = "new_article_url"
    NEW_ARTICLE_EXTRACTED = "new_article_extracted"
    MAXIMAL_ENTITY_COOCCURRENCE_SET = "maximal_entity_cooccurrence_set"
    NEWS_EMBEDDING = "news_embedding"
    NEWS_SEARCH_RESULTS = "news_search_results"
    INFORMATION_QUERYING_RESULTS = "information_querying_results"
    ERROR = "error"
    ADD_INSTRUCTION = "add_instruction"
    DELETE_INSTRUCTION = "delete_instruction"
    MOVE_INSTRUCTION = "move_instruction"
    NEW_INFOGRAPHIC = "new_infographic"
    MODIFIED_INFOGRAPHIC = "modified_infographic"


topic_to_type = {
    Topic.NEW_ARTICLE_URL: NewArticleUrlEvent,
    Topic.NEW_ARTICLE_EXTRACTED: NewArticleExtractedEvent,
    Topic.MAXIMAL_ENTITY_COOCCURRENCE_SET: MaximalEntityCooccurrenceSetEvent,
    Topic.NEWS_EMBEDDING: NewsEmbeddingEvent,
    Topic.NEWS_SEARCH_RESULTS: NewsSearchResultsEvent,
    Topic.INFORMATION_QUERYING_RESULTS: InformationQueryingComponentResultsEvent,
    Topic.ERROR: ErrorEvent,
    Topic.ADD_INSTRUCTION: AddInstructionEvent,
    Topic.DELETE_INSTRUCTION: DeleteInstructionEvent,
    Topic.MOVE_INSTRUCTION: MoveInstructionEvent,
    Topic.NEW_INFOGRAPHIC: NewInfographicEvent,
    Topic.MODIFIED_INFOGRAPHIC: ModifiedInfographicEvent,
}


def get_event_type(topic: Topic):
    return topic_to_type[topic]
