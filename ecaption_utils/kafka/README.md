# Usage
For comprehensive documentation, refer to the Faust documentation [here](https://faust.readthedocs.io/en/latest/index.html)

## Starting the faust application
```python
from ecaption_utils.kafka.topics import Topic
from ecaption_utils.kafka.events import get_event_type
from ecaption_utils.kafka.faust import get_faust_app, initialize_topics, FaustApplication

# Initialize Faust application
app = get_faust_app(FaustApplication.NLP)

# Initialize Kafka topics (for both consuming and publishing)
topics = initialize_topics(app, [Topic.XXX, Topic.YYY])
```

## Example usage of event consumer
```python
@app.agent(topics[Topic.XXX])
async def handle_event(event_stream):
    async for event in event_stream:
        # Get event properties configured in events.py
        event.xxx_property
        event.yyy_property

        # Handle event
        ...
```

## Example usage of event producer
```python
# E.g. inside an app.agent handler
topic = Topic.XXX
Event = get_event_type(topic)
event = Event(xxx_property=12345)

await topics[topic].send(value=event)
```

## Full example of processing incoming event and emitting subsequent event
```python
@app.agent(topics[Topic.XXX])
async def handle_event(event_stream):
    async for event in event_stream:
        # Get event properties configured in events.py
        event.xxx_property
        event.yyy_property

        # Handle event
        modified_xxx = event.xxx_property

        # Emit subsequent event
        topic = Topic.YYY
        Event = get_event_type(topic)
        event = Event(xxx_property=modified_xxx)

        await topics[topic].send(value=event)
```

## Running a Faust worker (i.e. consumer)
Spawn consumers with `@app.agent`s that listen to and consume particular topics.

E.g. for `main.py` file:
```
faust -A main worker -l info
```
