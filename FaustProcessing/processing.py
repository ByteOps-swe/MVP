import faust

app = faust.App(
    'hello-world',
    broker='kafka://kafka:9092',
    value_serializer='raw'
)

greetings_topic = app.topic('temperature')

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)

if __name__ == '__main__':
    app.main()
