'''
Created on Apr 8, 2015

@author: paepcke
'''

from checkbox import application
import os
import socket
import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.websocket.WebSocketHandler):
        
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"

    def exportClass(self):
        print("Export class was called.")   

if __name__ == "__main__":
    application = tornado.web.Application([
                                           (r"/", MainHandler),
                                           ])

    homeDir = os.path.expanduser("~")
    thisFQDN = socket.getfqdn()

    sslRoot = '%s/.ssl/%s' % (homeDir, thisFQDN)
    #*********
    # For self signed certificate:
    #sslRoot = '/home/paepcke/.ssl/server'
    #*********

    sslArgsDict = {
     "certfile": sslRoot + '.crt',
     "keyfile":  sslRoot + '.key',
     }

    #http_server = tornado.httpserver.HTTPServer(application,ssl_options=sslArgsDict)

    application.listen(9443)
    tornado.ioloop.IOLoop.instance().start()
