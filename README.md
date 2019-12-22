# Некоторые задачи синхронзиации

## Перед началом работы

Вам понадобится:

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python 3.7+](https://python.org/downloads/windows/)

Склонируйте проект. Откройте проект в VS Code.
Установите `quart`: `pip install -U quart`.

## Понедельник 16.12

### Шаг первый: обмен сообщениями

Запустите сервер -- `python3.7 server1.py` -- и браузер -- `http://localhost:5000`. Перейдите в первый урок.

В браузере откройте "Инструменты для разработчика", в них найдите JS-консоль.
Там вы должны увидеть сообщение "Начали работу!".

Ознакомьтесь с исходных кодом серверной части `server1.py` и исходных кодом страницы `templates/p_1_start.html`.
Убедитесь, что вы понимаете, как работает связка веб-страницы и сервера.

Сделайте упражнение в `templates/p_1_start.html`.

Далее, запустите взамен первого сервера -- второй (`server2.py`). Ознакомьтесь с комментариями в исходном коде.
Изучите отличия в поведении и функциональности.

Наконец, запустите взамен второго сервера -- третий (`server3.py`). Ознакомьтесь с комментариями в исходном коде.
Изучите отличия в поведении и функциональности.

Сделайте упражнение в `server3.py`.

### Шаг второй: монотонный счетчик

**Важно**: второй шаг требует выполненного в `server3.py` упражнения.

Запустите сервер -- `python3.7 server3.py` -- и браузер -- `http://localhost:5000`. Перейдите во второй урок.

Реализуйте монотонный счетчик: который умеет только расти. Для этого вспомните разобранную на занятии модель счетчика.
Следуйте указаниям в `templates/p_2_inc_counter.html`.

### Шаг третий: обычный счетчик

Это ваше домашнее задание.

Во-первых, доделайте классную работу и доведите обычный счетчик до рабочего состояния.

Во-вторых, добавьте операцию *уменьшения* счетчика.

Попробуйте самостоятельно адаптировать заготовку из `templates/p_2_inc_counter.html`:

* добавить две кнопки -- увеличения и уменьшения счетчика;
* адаптировать тестовый сценарий для нажатия двух кнопок попеременно.

## Вторник 17.12

**Важно**: можно воспользоваться сервером `server4.py`, так как он содержит всю разработанную ранее функциональность.

### Шаг четвертый: правки по Левенштейну

Ваша задача -- реализовать функцию расчета списка правок, которые переводят одну строку в другую.
Правка -- это операция вставки символа, операция удаления символа и операция замены символа.

Чтобы реализовать функцию расчета списка правок вам нужно модифицировать алгоритм расчета
расстояние Левенштейна между двумя строками и добавить в него обратный ход, извлекающий правки.

Сигнатура функции должна быть такая:

```js
function editList(left, right);
```

Исходный код функции должен быть размещен в файле `templates/j_editlist.js`.
Это нужно, чтобы код можно было переиспользовать на шаге 6.

Остальные подробности -- см. в `templates/p_4_editlist.html`.

### Шаг пятый: модель документа

> NB: Если вы работате самостоятельно, без лекционного материала,
> то для лучшего понимания концепции вам будут полезны статьи по [TreeDoc](https://hal.inria.fr/inria-00445975/document)
> и [LSEQ](https://hal.archives-ouvertes.fr/hal-00921633/document).

Ваша задача -- реализовать модель документа, поддерживающую операции вставки, удаления и замены,
но использующую абсолютное позиционирование символов внутри. Также модель документа должна
сериализоваться в пару множеств D1 и D2: D1 -- множество пар (позиция, символ), D2 -- множество
удаленных позиций.

Сигнатуры функций модели документа такие:

```js
function public_newDocument() {}
function public_getContent(document) {}

function public_serializeState(document) {} // можно отложить реализацию до 7-го шага
function public_mergeWithSerializedState(document, serializedState) {} // можно отложить реализацию до 7-го шага

function public_insertAfter(document, index, symbol) {} // реализация фиксирована, не трогать
function public_remove(document, index) {} // реализация фиксирована, не трогать
function public_replace(document, index, symbol) {} // реализация фиксирована, не трогать

function _getPositionByIndex(document, index) {}
function _allocate(document, begin, end) {}
function _allocateLeft(document, begin, end) {}
function _allocateRight(document, begin, end) {}
function _applyInsert(document, position, symbol) {}
function _applyRemove(document, position) {}
```

Исходный код функции должен быть размещен в файле `templates/j_treedoc.js`.
Это нужно, чтобы код можно было переиспользовать на шаге 6.

Описание функций, указания и другие подробности -- в `templates/p_5_treedoc.html`.

## Четверг 19.12

### Шаг шестой: интегрируем текстовое поле и модель документа

Ваша задача -- состыковать код из четвертого и пятого шагов.

В заготовке вас ждет интерфейс с текстовым полем. При изменении текстового поля
в нижней части экрана с помощью функции `editList` из `templates/j_editlist.js`
пересчитывается список правок между текущим содержимым модели (правая часть экрана)
и текущим содержимым текстового поля (левая часть экрана).

Вам нужно реализовать логику за кнопкой "Перенести в модель", которая приведет
содержимое модели к такой же строке, что и в текстовом поле.

Указания и подробности -- см. в `templates/p_6_textarea.html`.

### Шаг седьмой: собираем воедино

Ваша задача -- взять наработки с шестого шага и добавить пересылку данных
при изменении модели документа.

Стартовый шаблон и указания -- см. `templates/p_7_integration.html`.

Код работы с сетью можно позаимствовать из первых трех шагов.
Код для работы с текстовым полем -- из шестого.

Это задание для самостоятельной разработки.

NB: При получении сообщения по сети сперва всегда нужно синхронизировать
текстовое поле и модель, и лишь затем -- применять изменения, пришедшие по сети.

## Пятница 20.12

### Улучшение 1: непрыгающий курсор

Чтобы решить проблему прыгающего курсора при синхронизации, нужно сделать следующее:

Во-первых, в `j_treedoc.js` реализовать функцию:

```js
function _getIndexByPosition(document, position) {
    // Вернуть индекс по указанной позиции.
    // То есть вернуть число неудаленных символов, которые предшествуют данной позиции.
}
```

Тесты для проверки следующий:

```js
function testPositionSync() {
    let d = public_newDocument();
    public_insertAfter(d, -1, "c");
    public_insertAfter(d,  0, "a");
    public_insertAfter(d,  1, "t");
    assertEquals(public_getContent(d), "cat");
    for (var i = -1; i <= 3; ++i) {
        assertEquals(i, _getIndexByPosition(d, _getPositionByIndex(d, i)));
    }
}

function testPositionSyncWithInsertions() {
    let d = public_newDocument();
    public_insertAfter(d, -1, "a");
    var p = _getPositionByIndex(d, 0);

    assertEquals(public_getContent(d), "a");
    assertEquals(0, _getIndexByPosition(d, p));

    public_insertAfter(d, -1, "b");
    assertEquals(public_getContent(d), "ba");
    assertEquals(1, _getIndexByPosition(d, p));

    public_insertAfter(d, -1, "c");
    assertEquals(public_getContent(d), "cba");
    assertEquals(2, _getIndexByPosition(d, p));
}

function testPositionSyncWithDeletions() {
    let d = public_newDocument();
    public_insertAfter(d, -1, "c");
    public_insertAfter(d,  0, "a");
    public_insertAfter(d,  1, "t");
    var p = _getPositionByIndex(d, 2);

    assertEquals(public_getContent(d), "cat");
    assertEquals(2, _getIndexByPosition(d, p));
    public_remove(d, 0);
    assertEquals(public_getContent(d), "at");
    assertEquals(1, _getIndexByPosition(d, p));
    public_remove(d, 0);
    assertEquals(public_getContent(d), "t");
    assertEquals(0, _getIndexByPosition(d, p));
}
```

Во-вторых, улучшить интеграцию между текстовым полем и моделью.

Работа с курсором строится через работу с выделенной областью -- selection range.
Это пара чисел, определяющих диапазон выделенного текста. Если диапазон пустой,
то есть левая и правая границы совпадают, то диапазон кодирует точку расположения курсора.

Наша задача состоит в том, чтобы сохранить диапазон выделения на этапе синхронизации.

Для получения выделенной области используйте следующий код:

```js
var start = $("#integration-textarea").prop("selectionStart");
var end = $("#integration-textarea").prop("selectionEnd");
console.log("Курсор находится в позиции (" + start + ", " + end + ")");
```

Для обновления выделенной области используйте следующий код:

```js
$("#integration-textarea").get()[0].setSelectionRange(start, end);
```

Таким образом, чтобы решить задачу сохранения положения курсора,
код синхронизации нужно модифицировать примерно так:

```js
var startIndex = $("#integration-textarea").prop("selectionStart");
var startPosition = _getPositionByIndex(document, startIndex);
var endIndex = $("#integration-textarea").prop("selectionEnd");
var endPosition = _getPositionByIndex(document, endIndex);

// здесь код синхронизации

startIndex = _getIndexByPosition(startPosition);
endIndex = _getIndexByPosition(endPosition);

$("#integration-textarea").get()[0].setSelectionRange(startIndex, endIndex);
```

### Улучшение 2: улучшение производительности `editList`

В `editList` при расчете списка правок мы ищем минимальный по длине список правок.
Само свойство минимальности мы никак не используем. Также строки, передаваемые как аргументы
в функцию `editList` обычно отличаются в небольшой : мы отслеживаем правки, внесенные человеком,
и человеческие правки обычно локальные.

Поэтому предлагается добавить в реализацию `editList(left, right)` следующую эвристику:
откусим у `left` и `right` общий префикс, далее откусим у `left` и `right` общий суффикс,
и только после этого -- для двух оставшихся середин строк -- посчитаем `editList`
(не забыв скорректировать индексы).

```text
** 1: Исходные строки

left  = "hello, dolly"
right = "hello dolly"

** 2: Откусываем префикс

p     = "hello"
left  = ", dolly"
right = " dolly"

** 3: Откусываем суффикс

p     = "hello"
s     = " dolly"
left  = ","
right = ""

Далее считаем editList(left, right); индексы корректируем на длину общего префикса.
```

Как измерить выгоду от такого улучшения?

Добавьте в код страницы следующую функцию для измерения времени работы функции:

```js
function bench(name, fn) {
    var begin = new Date();
    var result = fn();
    var end = new Date();
    console.log("[bench] Фрагмент " + name + " выполнялся " + (end - begin) + "мс");
    return result;
}

// Далее по коду функцию можно использовать следующим образом.
// Будем использовать языковое сокращение:
//
//   () => expr;
//
// Эквивалентно:
//
//   function() { return expr; }
//
// Тогда:

// Было:
var diff = editList(left, right);
// Стало:
var diff = bench("editList-1", () => editList(left, right));

// Было:
$(...).val(public_getContent(d));

// Стало так:
bench("render", () => $(...).val(public_getContent(d)));
// Или так:
$(...).val(bench("render", () => public_getContent(d)));
```

### Улучшение 3: уменьшаем объем синхронизации

Сейчас при общении между клиентами мы передаем полное состояние документа, что может быть
существенным объемом для больших документов.

При этом модель документа -- с множествами D1 и D2 -- подразумевает, что в множества D1 и D2
элементы только добавляются.

За счет этого наблюдения мы можем сэкономить на объеме передаваемых данных и пересылать только
новые добавленные элементы в D1 и D2.

### Улучшение 4: уменьшаем частоту синхронизации

Сейчас мы вызываем синхронизацию между текстовым полем, моделью и сервером при каждом изменении
текстового поля.

Можно чуть уменьшить частоту синхронизации, делая её не чаще, чем раз в несколько миллисекунд.

Для этого можно воспользоваться методом `throttle` из библиотеки [lodash](https://github.com/lodash/lodash).

Во-первых, нужно подключить библиотеку: скачайте из репозитория файл `static/js/lodash.min.js`,
добавьте в `p_7_integration.html` строку `<script src="/static/js/lodash.min.js" crossorigin="anonymous"></script>`
рядом с аналогичными про `jquery`, `popper`.

Во-вторых, трансформируйте ваш код следующим образом:

```js
// Было:

$("#integration-textarea").on("input", function() {
    // ... раз-два-три ...
});

// Стало:

var onInput = _.throttle(function() {
    // ... раз-два-три ...
}, /* Вызывать не чаще, чем каждые */ 100 /* миллисекунд. */);

$("#integration-textarea").on("input", onInput);
$("#integration-textarea").on("blur", onInput.flush);
```
