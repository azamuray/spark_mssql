## Установка

Для начала необходимо поставить MS SQL через докер:

    docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=MyPass@word" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 -d --name=sql mcr.microsoft.com/azure-sql-edge

1. Скачать JAVA по ссылке https://www.oracle.com/java/technologies/downloads/ и установить
2. Скачать JRE по ссылке https://go.microsoft.com/fwlink/?linkid=2259203
3. Указать путь до JRE из ранее скачанного архива. 
4. Установить библиотеку pyspark
5. Создать тестовую таблицу Employees в MS SQL и добавить данные

## Запуск

    python run.py
