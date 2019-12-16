## Понедельник 16.12

Скачайте скелет проекта и запустите его. Вам нужно запустить сервер -- `python3.7 server.py` --
и браузер -- `http://localhost:5000`.

Для ознакомления с JS сделайте упражнение 1 в `templates/index.html`: напишите выбор уникального имени пользователя. См. [Math.random()](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Math/random).

Далее можете ознакомиться с реализацией серверной части. Для этого попробуйте последовательно менять точку подключения браузера с `/ws1` до `/ws3` в index.html.

Далее, сделайте упражнение 2: измените код хендлера `/ws3`, чтобы он распространял сообщения, полученные от одного пользователя (браузера) до всех остальных. Подсказка: заведите для этого множество очередей всех пользователей.

Наконец, приступайте к упражнению 3: раскомментируйте в `templates/index.html` код кнопки счетчика -- и реализуйте механизм синхронизации!

Подсказки:
- при отправке структурированных данных используйте метод [JSON.stringify](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) для превращения JS-объектов в JSON;
- при получении используйте [JSON.parse](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) для превращения JSON в JS-объект;
- печатайте объекты в консоль браузера "как есть" через [console.log](https://developer.mozilla.org/ru/docs/Web/API/Console/log);

Полезные ссылки:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Python 3.7+](https://www.python.org/downloads/windows/)
* [Quart](https://pgjones.gitlab.io/quart/index.html) (`pip3 install -U quart`)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://api.jquery.com/)
