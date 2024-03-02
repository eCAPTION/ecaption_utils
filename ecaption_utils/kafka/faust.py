import enum
import faust
from .topics import Topic, topic_to_type


class FaustApplication(enum.Enum):
    Gateway = "gateway"
    WebScraper = "web_scraper"
    NLP = "nlp"
    NewsEmbedding = "news_embedding"
    Chatbot = "Chatbot"


faust_application_to_port: dict[FaustApplication, int] = {
    FaustApplication.Gateway: 6066,
    FaustApplication.WebScraper: 6067,
    FaustApplication.NLP: 6068,
    FaustApplication.NewsEmbedding: 6069,
    FaustApplication.Chatbot: 6070,
}


def get_faust_app(app_id: FaustApplication):
    return faust.App(
        app_id.value,
        broker="kafka://localhost:9092",
        web_port=faust_application_to_port[app_id],
    )


def initialize_topics(app: faust.App, topics: list[Topic]):
    initialized_topics = {}

    for topic in topics:
        initialized_topics[topic] = app.topic(
            topic.value, value_type=topic_to_type[topic]
        )

    return initialized_topics
