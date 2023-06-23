import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')
hello_topic = app.topic('hello')


@app.agent(hello_topic)
async def hello2(greeting_msg) -> None:
    """Send a message to the hello topic."""
    pass

@app.agent(greetings_topic)
async def greet(greetings):
    """Send a message to the greeting topic."""
    pass



