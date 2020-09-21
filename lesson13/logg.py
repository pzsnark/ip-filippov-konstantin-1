import logging
logging.basicConfig(
    filename="app.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.INFO
)
log = logging.getLogger("app")
# записать сообщение используя позиционные аргументы форматирования
host = 'localhost'
port = 7777
log.critical("Can't connnect to %s at port %d", host, port)
# записать сообщение используя словарь значений
parms = { 'host': "www.python.org",
"port" : 80
}
log.critical("Can't connect to %(host) at port %(port)d", parms)
log.error("Can't connect to %(host) at port %(port)d", parms)
log.warning("Can't connect to %(host) at port %(port)d", parms)
log.debug("Can't connect to %(host) at port %(port)d", parms)
