# WeatherCast
### Умный сервис прогноза погоды - Проектное задание для "Школы будущих CTO" - Выполнено Колокольниковым Георгием
__Уровень сложности:__  
Попытался сделать задачку со звездочкой =)

#### Проектирование сервиса:
Используемые технологии:  
- Python 3.7.4
- Django 2.2.1
- GeoIP2 для определения локации пользователя
- Openweathermap API
- HTML, CSS, Bootstrap

Пользовательский интерфейс:  
- Сайт (возможно, далее будет добавлен Telegram-бот, привязанный к сайту)  

Формат ответа:   
- На главной странице веб-сайта выводится текстовая информация о погоде, а также погодная пиктограмма. Дополнительно выводится графическая информация о рекомендуемом комплекте одежды.

#### Демонстрация работы сервиса:
- видео представлено по ссылке ниже:
- ....

#### Процесс работы сервиса:
- картинка!
1. Пользователь попадает на главную страницу веб-сайта
2. Происходит определение его города с помощью GeoIP
3. Формируется запрос к openweather API с определенным городом.
4. Данные полученные с API парсятся в словарь, включающий температуру, тип погодных условий (солнечно, облачно, осадки), индекс картинки погоды. 
4.1 Если такого города нет, то в словарь добавляется флаг и запись о некорректном городе.
5. Выполняется простейшая логика для формирования пути к картинке комплекта одежды в зависимости от погодных условий. Путь к картинке добавляется в словарь.
6. Происходит рендеринг страницы, словарь подставляется в шаблон. Пользователю выводится текстовая информация и картинка погоды. Дополнительно пользователю в зависимости от погодных условий рекомендуется комплект одежды (всего 9 для мужчин и 9 для женщин). 
7. В случае, если город по GeoIP определен неверно, или пользователь хочет узнать погоду в другом городе, он может нажать на кнопку, в результате чего произойдет переход на другую страницу. 
8. На новой странице пользователь должен ввести город и выбрать свой пол. 
9. После заполнения формы пользователь получит информацию по погоде в заданном городе и комплект одежды с учетом указанного пола.
10. Дополнительно пользователь может перейти на страницу "About", где представлена информация по проекту.


