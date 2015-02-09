
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import time
from twython import TwythonStreamer
import config as c
class wsHandler(tornado.websocket.WebSocketHandler):
    conn = []
    def open(self):
        self.conn.append(self)

    def on_close(self):
        self.conn.remove(self)


class MyStreamer(TwythonStreamer,wsHandler):
    def on_success(self, data):
        for connection in wsHandler.conn:
            if 'text' in data:
                connection.write_message(data['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print status_code



application = tornado.web.Application([
    (r'/ws', wsHandler),
])

def openstreamer(kelime):
    print kelime
    stream = MyStreamer(c.CONSUMER_KEY,c.CONSUMER_SECRET,
            c.ACCESS_TOKEN,c.ACCESS_SECRET)
    stream.statuses.filter(track=kelime)


import threading
import sys
if __name__ == "__main__":
    if len(sys.argv)<2:
        print "lütfen aranacak kelimeyi belirtiniz"
        exit(1)
    a = threading.Thread(target=openstreamer,args=[sys.argv[1]])
    a.start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



