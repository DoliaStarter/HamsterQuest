# HamsterQuest

# Зависимости
Чтобы установить все зависимости.
```
pip install -r requirements.txt
```


# Запуск
Для того что бы все работало нужен доступ в интернет
Чтобы запустить 
```
login@host:$ git clone https://github.com/DoliaStarter/HamsterQuest.git hackathon
login@host:$ cd hackathon/hacknaquest 
login@host:~/hackathon/hacknaquest$ python manage.py runserver  
```

# Изменения
## HTML
В проекте имплементирована система наследования для шаблонов: все страницы наследуються от двух базовых класов которыми являються страница с двумя колонами(`two_col_base.html`) и страница с тремя колонами(`three_col_base.html`).
Каждая страница предоставляет секции которые можно расширять.

Блоки:
  - `styles`: блок который можна добавлять файлы со стилями css. **Внимание!** Чтобы можна было добавить стили к странице, на ней должна находиться линия `{% load static %}`
  - `toolbar`: блок в который находиться в верхеней части страницы. По умолчанию в нем выписано назание текущего кабинета. ( в будущим думаю будет лого ). В `toolbar` находиться подсекция:
       
       -`action_buttons` - в нее можна добавлять кнопки для навигации
  
  - `content` - секция в которой находиться содержание страницы. Состоит из блоков:
 
      -`columns` - шаблон из колон. В нем находяться блоки:
       
       - `left_column`: - колона которая, будет находиться слева  
       - `right_column`: - колона которая будет находиться справа
       - `center`: - если выбрана страница которая состоит из трёх колон (`three_col_base.html`)
      
      -`plain_text` - блок который идет после колон. В него можна добавлять текст и прочие необходимые элементы. По умолчанию пустой
  
  
  
Каждое приложение имеет папку с заготовкой, которая будет возвращяться после перехода по даному адресу.

Например:

запрос на адрес `127.0.0.1:8000/quest_manager/`, вернет страницу под адресом `main/templates/quest_manager/index.html`.

Поэтому для изменения внешнего вида **нужно** использовать эти заготовки. 

## CSS
Для того чтобы изменить стиль страницы в первую очередь нужно использовать файл который являеться специфическими для конкретной страницы. Например для страницы `main/templates/main_page/index.html` лучше всего использовать файл `main/static/styles/main_page.css`. Только в случае крайней нужды можна изменять файл `main/static/styles/base.css`, посколько этот файл описывает стиль который являеться общим для **всех** страниц проекта. 

## JS
Для того чтобы добавить скрипты JS, вы должны перейти в папку своего проекта в папке `main/static/scripts/`. 
Если это скрипты, которые могут быть использованы во всем документе (например переключение секций), помещаем в файл `main/static/scripts/common.js`. Это модуль (о модулях и почему мы их используем ниже), поэтому в конце файла находим линейку `export {func1, func2, ...}` и изменяем ее на  `export {func1, func2, ..., yourFunctionName}`. 

## JS и модули

Теперь важный нюанс насчёт того как работаем с JS. 
Поскольку скрипты JS могут быть немаленькими, а людей работает много - могут появиться проблемы. Например у 2 людей будут функции с одинаковыми названиями. В таком случае одна из функций пропадет, что привидет к долгому и скучному дэбагу. 
На счастье JS позволяет избежать таких проблем используя пакеты. 
Как их использовать в JS

В модуле который хотим куда-то импортировать пишем:

```javascript
export {func1, func2, func3, ....}
```

В модуле который импортируем:

```javascript
import * as ModuleName from Path
```

Теперь чтобы использовать функции из модуля

```javascript
ModuleName.functionName(params)
```
Чтобы загрузить модуль в HTML (или файл в который импортируеться модуль):
```html
<script type="module" src=path></script>
```
**Внимание!** При таком импорте как выше скрипт создает свое именное пространство, причем назание его нам не известно, что значит что мы не сможем вызвать функции после такого импорта. 
Другими словами:
```javascript
// module.js
function foo(param) {
  console.log(param)
}

export {foo}
```
```html
<script type="module" src='module.js'></script>
....
<button onclick=foo('hello')></button> 
```
Выдаст ошибку.
Для того привязать `foo` c параметром `hello` делаем:

1. Переносим импорт скрипта вниз документа.
2. Приписыаем id к кнопке `<button id='to_click'></button>`
3. Пишим следующий код
```html
<script type="module">
import * as Module from 'module.js'
document.getElementById('to_click').onclick = (_) => Module.foo('hello')  
</script>
```

Теперь насчёт того, что это `(_) => Module.foo('hello')` за странная вещь.
Это JS синтаксис для лямбды.

Зачем нам лямбда ? 

Когда мы привязываем что-то с уровня JS - мы должны передавать референцию на функцию иначе мы привяжем не функцию а результат ее выполнения. На помощь приходит лямбда, которая являеться функцией единстенной задачей которой будет вызвать другую функцию в которую мы передали параметр.

Почему `(_)` ?

Когда браузер вызывает функцию - он автоматически подает в нее аргумент который являеться событием нажатия. Вообще полезная штука, которая позволяет узнавать такие вещи как например кнопка на которую нажали, что позволяет ее изменять. Но нам здесь это не нужно, поэтому указываем что параметр неважный и называем его `_`.

