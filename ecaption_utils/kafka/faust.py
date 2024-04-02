import enum
import faust
from .topics import Topic, topic_to_type
from .events import ErrorEvent


class FaustApplication(enum.Enum):
    Gateway = "gateway"
    WebScraper = "web_scraper"
    NLP = "nlp"
    NewsEmbedding = "news_embedding"
    NewsSearch = "news_search"
    FactQuerying = "fact_querying"
    Chatbot = "chatbot"
    InfographicGeneration = "infographic_generation"


def get_faust_app(app_id: FaustApplication, broker_url: str, port: int):
    return faust.App(
        app_id.value,
        broker=broker_url,
        web_port=port,
    )


def initialize_topics(app: faust.App, topics: list[Topic]):
    initialized_topics = {}

    for topic in topics:
        initialized_topics[topic] = app.topic(
            topic.value, value_type=topic_to_type[topic]
        )

    return initialized_topics


def get_error_handler(app: faust.App):
    error_topic = app.topic(Topic.ERROR.value, value_type=topic_to_type[Topic.ERROR])

    async def handle_error(request_id: int, error_type: str, error_message: str):
        error_event = ErrorEvent(
            request_id=request_id,
            error_type=error_type,
            error_message=error_message,
        )

        await error_topic.send(value=error_event)

    return handle_error
