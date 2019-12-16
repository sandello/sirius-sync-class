## Понедельник 16.12

### В классе

Скачайте скелет проекта и запустите его. Вам нужно запустить сервер -- `python3.7 server.py` --
и браузер -- `http://localhost:5000`.

Для ознакомления с JS сделайте упражнение 1 в `templates/index.html`: напишите выбор уникального имени пользователя. См. [Math.random()](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Math/random).

Далее можете ознакомиться с реализацией серверной части. Для этого попробуйте последовательно менять точку подключения браузера с `/ws1` до `/ws3` в index.html.

Далее, сделайте упражнение 2: измените код хендлера `/ws3`, чтобы он распространял сообщения, полученные от одного пользователя (браузера) до всех остальных. Подсказка: заведите для этого множество очередей всех пользователей.

Как понять, что упражнение выполнено верно?
- в браузере 1 открываем страницу; в странице вычисляется имя "кошка", отправляется на сервер, страница 1 получает от сервера "кошка", и в браузере печатается "кошка";
- в браузере 2 открываем страницу, в странице вычисляется имя "собака", отправляется на сервер, страница 1 получает от сервера "собака", страница 2 получает от сервера "собака", и на странице 1 рисуется "кошка, собака", на странице 2 рисуется "собака".

Наконец, приступайте к упражнению 3: раскомментируйте в `templates/index.html` код кнопки счетчика -- и реализуйте механизм синхронизации!

Подсказки:
- можно использовать структуру данных [Set](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Set) для моделирования множества, или можно использовать [Array](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Array) для моделирования множества поверх массива;
- при отправке структурированных данных используйте метод [JSON.stringify](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) для превращения JS-объектов в JSON;
    - обратите внимание, что `Set` просто так в JSON не превращается: это сложный объект;
    - чтобы сериализовать множество в список используйте сниппет `var a = []; s.forEach(function(x) { a.push(x); }); JSON.stringify(a);`;
- при получении используйте [JSON.parse](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) для превращения JSON в JS-объект;
- печатайте объекты в консоль браузера "как есть" через [console.log](https://developer.mozilla.org/ru/docs/Web/API/Console/log);

Полезные ссылки:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Python 3.7+](https://www.python.org/downloads/windows/)
* [Quart](https://pgjones.gitlab.io/quart/index.html) (`pip3 install -U quart`)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://api.jquery.com/)

### Домашнее задание

Во-первых, довести классную работу до рабочего состояния: реализовать счетчик с операцией инкремента.

Во-вторых, добавить операцию *декремента*: теперь счетчик можно и уменьшать, и увеличивать!

Для верстки двух кнопок можно использовать следующий фрагмент кода:
```html
<div class="counter">
    <p id="counter-value" class="lead"></p>
    <div class="btn-group">
        <button id="counter-dec-button" type="button" class="btn btn-danger">Минус</button>
        <button id="counter-inc-button" type="button" class="btn btn-success">Плюс</button>
    </div>
</div>
```

Не забудьте правильным образом подправить id-шники кнопок в JS-коде!
