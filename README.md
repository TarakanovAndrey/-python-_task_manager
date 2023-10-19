### Hexlet tests and linter status:
[![Actions Status](https://github.com/TarakanovAndrey/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/TarakanovAndrey/python-project-52/actions)

# Менеджер задач  
С функционалом приложения можно ознакомиться по ссылке:  
https://task-manager-j2qw.onrender.com  

## Problems:

1**Ошибка миграции**  
**Проблема.** На рендер ошибка деплоя. Связана с удалением базы данных и миграций вручную.
Текс ошибки "aise InconsistentMigrationHistory(
Oct 14 12:57:47 PM  django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'."  
**Решение.**  
**Текущий статус.**
2**Выпадающее меню**  
**Проблема.** При уменьшении размера экрана навигация сворачивается в выпадающее меню. 
Но при нажатии оно не разворачивается.  
**Решение.**  
**Текущий статус.**  
3. Из вьюхи в шаблон передавать уже готовые данные, чтобы по максимуму не усложнять шаблон лишней логикой.  
4. Не реализованы тесты для третьего шага.  
5. Не до конца релазованы мгновенные собщения в третьем шаге.  
6. Оформление полей ввода не совпадает. Возможно потому что не подключен crispy  
7. Дата создания отображается не в том формате.  
8. 