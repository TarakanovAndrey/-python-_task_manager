### Hexlet tests and linter status:
[![Actions Status](https://github.com/TarakanovAndrey/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/TarakanovAndrey/python-project-52/actions)

# Менеджер задач  
С функционалом приложения можно ознакомиться по ссылке:  
https://task-manager-j2qw.onrender.com  

## Problems:
1. **Поле "Подтверждение пароля".**  
**Проблема.** Форма создания пользователя связана с моделью. В форме есть поле "Подтверждение пароля".
Его хранить не надо. Но данное поле в модели я создал.  
**Решение.** Для подтверждения пароля сделать отельную форму, без связи с моделью. Из модели и связанной с ней 
формы удалить.  
**Текущий статус.**  


2. **Ошибка миграции**  
**Проблема.** На рендер ошибка деплоя. Связана с удалением базы данных и миграций вручную.
Текс ошибки "aise InconsistentMigrationHistory(
Oct 14 12:57:47 PM  django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'."  
**Решение.**  
**Текущий статус.**
3. **Выпадающее меню**  
**Проблема.** При уменьшении размера экрана навигация сворачивается в выпадающее меню. 
Но при нажатии оно не разворачивается.  
**Решение.**  
**Текущий статус.**  