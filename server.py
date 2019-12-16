#!/usr/bin/env python3.7

import asyncio
import logging
import quart


app = quart.Quart(__name__, template_folder="templates", static_folder="static")
log = logging.getLogger(__name__)

@app.route("/")
async def index():
    return await quart.render_template("index.html")


@app.websocket("/ws1")
async def ws1():
    while True:
        data = await quart.websocket.receive()
        print(f"Got {data}!")
        await quart.websocket.send(f"Подтверждаем, что получили '{data}'!")


@app.websocket("/ws2")
async def ws2():
    user = quart.websocket.remote_addr

    async def sending():
        import datetime
        while True:
            data = "Время " + str(datetime.datetime.now())
            log.info("Пользователь %s: SEND[%r]", user, data)
            await quart.websocket.send(data)
            await asyncio.sleep(1)

    async def receiving():
        while True:
            data = await quart.websocket.receive()
            log.info("Пользователь %s: RECV[%r]", user, data)

    try:
        log.info("Пользователь %s подключился :)", user)
        producer = asyncio.create_task(sending())
        consumer = asyncio.create_task(receiving())
        await asyncio.gather(producer, consumer)
    finally:
        log.info("Пользователь %s отключился :(", user)


@app.websocket("/ws3")
async def ws3():
    user = quart.websocket.remote_addr
    queue = asyncio.Queue()

    async def sending():
        import datetime
        while True:
            data = await queue.get()
            log.info("Пользователь %s: SEND[%r]", user, data)
            await quart.websocket.send(data)

    async def receiving():
        while True:
            data = await quart.websocket.receive()
            log.info("Пользователь %s: RECV[%r]", user, data)
            await queue.put(data)

    try:
        log.info("Пользователь %s подключился :)", user)
        producer = asyncio.create_task(sending())
        consumer = asyncio.create_task(receiving())
        await asyncio.gather(producer, consumer)
    finally:
        log.info("Пользователь %s отключился :(", user)


# TODO(2): Упражнение.
# Реализуйте логику широковещательной отправки сообщений всем подключенным пользователям.
# Для этого используйте множество очередей сообщений всех пользователей.


def main():
    app.config.from_mapping(DEBUG=True, ENV="dev")
    app.run()


if __name__ == "__main__":
    main()