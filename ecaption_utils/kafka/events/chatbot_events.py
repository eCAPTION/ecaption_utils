from .base_event import BaseEvent


class BaseInstructionEvent(BaseEvent):
    infographic_link: str


# Format: I want to add [target_element] next to [infographic_section]
# Possible infographic sections: Header, Number of Shares, Vote on Reliability, Related Facts, Latest Comments, Knowledge Graph Summaries, Similar Articles
class AddInstructionEvent(BaseInstructionEvent):
    target_element: str
    infographic_section: str


# Format: I want to delete [infographic_section]
# Possible infographic sections: Header, Number of Shares, Vote on Reliability, Related Facts, Latest Comments, Knowledge Graph Summaries, Similar Articles
class DeleteInstructionEvent(BaseInstructionEvent):
    infographic_section: str


# Format: I want to move [target_section] to the [direction] of [reference_section]
# Example: relocate the counter showing the infographic's sharing activity to the right of the infographic's knowledge graph section
# Possible infographic sections: Header, Number of Shares, Vote on Reliability, Related Facts, Latest Comments, Knowledge Graph Summaries, Similar Articles
# Possible directions: right, left, above, below
class MoveInstructionEvent(BaseInstructionEvent):
    target_section: str
    reference_section: str
    direction: str


# Chatbot will listen to this event for newly generated infographics
class NewInfographicEvent(BaseEvent):
    infographic_link: str


# Chatbot will listen to this event for modified infographics
class ModifiedInfographicEvent(BaseEvent):
    new_infographic_link: str

