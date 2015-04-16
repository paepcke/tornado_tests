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
        
    @classmethod
    def getCertAndKey(cls):
        '''
        Return a 
        
        '''
        homeDir = os.path.expanduser("~")
        sslDir = '%s/.ssl/' % homeDir
        try:
            certFileName = next(fileName for fileName in os.listdir(sslDir) 
	                               if fileName.endswith('.cer') or fileName.endswith('.crt'))
        except StopIteration:
            raise(ValueError("Could not find ssl certificate file in %s" % sslDir))
        
        try:
            privateKeyFileName = next(fileName for fileName in os.listdir(sslDir) 
	                                     if fileName.endswith('.key'))
        except StopIteration:
            raise(ValueError("Could not find ssl private key file in %s" % sslDir))
        return (os.path.join(sslDir, certFileName),
                os.path.join(sslDir, privateKeyFileName))
           

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

    (certFile,keyFile) = CourseCSVServer.getCertAndKey()
    sslArgsDict = {'certfile' : certFile,
                   'keyfile'  : keyFile}
                   
    

    http_server = tornado.httpserver.HTTPServer(application,ssl_options=sslArgsDict)

    application.listen(9443,  ssl_options=sslArgsDict)
    tornado.ioloop.IOLoop.instance().start()
