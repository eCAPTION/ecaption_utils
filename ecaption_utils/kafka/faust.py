import enum
import faust
from .topics import Topic, topic_to_type


class FaustApplication(enum.Enum):
    Gateway = "gateway"
    WebScraper = "web_scraper"
    NLP = "nlp"
    NewsEmbedding = "news_embedding"
    Chatbot = "chatbot"
    NewsSearch = "news_search"


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
