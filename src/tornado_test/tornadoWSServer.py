'''
Created on Apr 8, 2015

@author: paepcke
'''

import logging
import os
import socket
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver


class CourseCSVServer(tornado.websocket.WebSocketHandler):
    
#     def __init__(self):
#         super(MainHandler, self).__init__()
#         #**********
#         print('called')
#         #**********
#         self.tornadoLogger = logging.getLogger()
#         self.tornadoLogger.setLevel(logging.DEBUG)
#         #logging.info('Init called.')
#         self.tornadoLogger.info('Init called.')
        
    def check_origin(self, origin):
        return True
        
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def exportClass(self):
        print("Export class was called.")   

if __name__ == "__main__":
    
    loggerAccess  = logging.getLogger('tornado.access')
    loggerApp     = logging.getLogger('tornado.application')
    loggerGeneral = logging.getLogger('tornado.general')
    
    loggerAccess.setLevel(logging.DEBUG)
    loggerApp.setLevel(logging.DEBUG)
    loggerGeneral.setLevel(logging.DEBUG)
    
    #loggerGeneral.log(logging.INFO, 'Logging OK')
    
    application = tornado.web.Application([
                                           (r"/exportClass", CourseCSVServer),
                                           ],
                                          debug=True)

    homeDir = os.path.expanduser("~")
    thisFQDN = socket.getfqdn()
    thisFQDNUnderscored = thisFQDN.replace('.', '_')

    sslRoot = '%s/.ssl/%s' % (homeDir, thisFQDN)
    sslRootUnderscored = '%s/.ssl/%s' % (homeDir, thisFQDNUnderscored)
    #*********
    # For self signed certificate:
    #sslRoot = '/home/paepcke/.ssl/server'
    #*********

    sslArgsDict = {
     #"certfile": sslRoot + '.crt',
     "certfile": sslRootUnderscored + '_cert.cer',
     "keyfile":  sslRoot + '.key',
     }

    http_server = tornado.httpserver.HTTPServer(application,ssl_options=sslArgsDict)

    application.listen(9443,  ssl_options=sslArgsDict)
    tornado.ioloop.IOLoop.instance().start()
