Начало решения тестового задания:
Web-приложение для определения заполненных форм.
По поводу сроков выполнения: тестовые задания принимаются до тех пор, пока открыта вакансия.

В БД хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Пример шаблона формы:

name: ‘form template name’
field_name1: ‘email’
field_name2: ‘phone’

Всего должно поддерживаться четыре типа данных полей: 
email
телефон
дата
текст.

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате +7 xxx xxx xx xx, дата передается в формате DD.MM.YYYY или YYYY-MM-DD.

Имя шаблона формы задается в свободной форме, например MyForm или Order Form.
Имена полей также задаются в свободной форме (желательно осмысленно), например user_name, order_date или lead_email.

На вход по урлу /get_form POST запросом передаются данные такого вида
f_name1=value1&f_name2=value2

В ответ нужно вернуть имя шаблона формы, если она была найдена.
Чтобы найти подходящий шаблон нужно выбрать тот, поля которого совпали с полями в присланной форме. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в форме.

Если подходящей формы не нашлось, вернуть ответ в следующем формате
{
f_name1: FIELD_TYPE,
f_name2: FIELD_TYPE
}
где FIELD_TYPE это тип поля, выбранный на основе правил валидации, проверка правил должна производиться в следующем порядке дата, телефон, email, текст.


+ решение тестовых задачек для Яндекса
