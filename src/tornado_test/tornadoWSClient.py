#!/usr/bin/env python

'''
Created on Apr 9, 2015

Not quite working. See tornado.concurrent.py and
tornado.websocket.py for hints. I dropped getting
it to run, b/c the clients I need right now are all
Javascript. Therefore, see tornado_test.js for an
example client.

@author: paepcke
'''

import sys
import time
import tornado
#import platform

from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado.web import Application

try:
    import thread
except ImportError: #TODO use Threading instead of _thread in python3
    import _thread as thread


class CourseCSVServer(WebSocketHandler):

    def on_message(self, message):
        print(message)
    
    def on_error(self, error):
        print(error)
    
    def on_close(self):
        print("### closed ###")
    
    def on_open(self):
        def run(*args):
            for i in range(3):
                # send the message, then wait
                # so thread doesnt exit and socket
                # isnt closed
                self.write_message("Hello %d" % i)
                time.sleep(1)
        time.sleep(1)
        self.close()
        print("Thread terminating...")
        thread.start_new_thread(run, ())

def on_message(ws, msg):
    print("Received '%s' from server." % msg)

if __name__ == "__main__":
    #websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "ws://echo.websocket.org/"
    else:
        host = sys.argv[1]
    
    # Get a tornado 'Future' instance whose result
    # is a WebSocketClientConnection. Tornado Futures 
    # are defined in tornado.concurrent.py. Two important
    # methods are result(timeout=None), and done()
    connectionFuture = tornado.websocket.websocket_connect("wss://mono.stanford.edu:9443/exportClass", on_message_callback=on_message)
    print("waiting for connection to complete...")
    while not connectionFuture.done():
        time.sleep(0.1)
    print("Connection completed...")
    wsClientConnection = connectionFuture.result()
    print "Sending 'Hello, World'..."
    wsClientConnection.write_message("Hello, World")
    print "Receiving..."
    time.sleep(3)
#    resultFuture =  wsClientConnection.read_message()
#    print "Received '%s'" % resultFuture.result()
    wsClientConnection.close()
        
        
        
#     application = Application([(r'/', CourseCSVServer)], debug=True)
#     application.listen(9443)
#     IOLoop.instance().start()
    
#     ws = websocket.WebSocketApp(host,
#         on_message = on_message,
#         on_error = on_error,
#         on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()


# From a different source:

# import websocket
# 
# if __name__ == '__main__':
# 
#     ws = websocket.WebSocket() 
#     websocket.create_connection("ws://localhost:8080/websocket")
#     print "Sending 'Hello, World'..."
#     ws.send("Hello, World")
#     print "Sent"
#     print "Reeiving..."
#     result =  ws.recv()
#     print "Received '%s'" % result
#     ws.close()
