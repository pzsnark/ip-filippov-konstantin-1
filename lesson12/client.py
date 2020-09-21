# программа клиента запрашивающая текущее время
import socket
import threading
import time

# s = socket(AF_INET, SOCK_STREAM)  # создаем сокет
# s.connect(("localhost", 8888))  # соединение с сервером
# tm = s.recv(1024)  # принять не более 1024 байтов данных
# s.close()
# print("Текущее время: %s" % tm.decode("ascii"))


# логические флаги, об отключении и подключении клиентов
shutdown = False
join = False


def receving(name, sock):
    """функция для приема сообщений с сервера"""
    while not shutdown:
        try:
            while True:
                # получаем сообщения
                data, addr = sock.recvfrom(1024)
                # обязательно декодируем сообщение
                print(data.decode("utf-8"))
                # ждем 0.2 секунды, на всякий случай
                time.sleep(0.2)
        except:
            pass


server = ("localhost", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 0))

name = input("Name: ")

# одельный поток для получения сообщений
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("[" + name + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input("[You] :: ")

            if message != "":
                # обязательно кодируем сообщение
                # указыываем само сообщение и куда его отправить
                s.sendto(("[" + name + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + name + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()