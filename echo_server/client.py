#1. Проверьте возможность подключения к серверу с локальной, виртуальной и удаленной машины.
#2. Модифицируйте код клиента таким образом, чтобы он читал строки в цикле до тех пор, пока клиент не введет “exit”. Можно считать, что это команда разрыва соединения со стороны клиента.

import socket

sock = socket.socket() #Создание сокета
sock.connect(('localhost', 1899)) #Подключение к серверу

while True:
    a = input() #Просим клиента вводить данные
    if a == 'exit': #Останавливаем с помощью break цикл while по требованию клиента  
        break
    b = bytes(a, encoding='utf-8') #возвращаем объект типа bytes
    sock.send(b) #Отправляем данные на сервер
    data = sock.recv(1024) #Для получения данных от клиента небольшими частями, а именно 1024 Байт
    print(data)

sock.close() #Закрываем соединение 
