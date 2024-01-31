import faust


class InformationQueryingComponentEvent(faust.Record):
    url: str


class NewArticleUrlEvent(InformationQueryingComponentEvent):
    pass


class NewArticleTextEvent(InformationQueryingComponentEvent):
    text: str


class MaximalEntityCooccurrenceSetEvent(InformationQueryingComponentEvent):
    maximal_entity_cooccurrence_set: list[list[str]]
