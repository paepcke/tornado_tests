'''
Created on Dec 2, 2015

@author: paepcke
'''

import sys

from tornado import httpserver
from tornado import web
import tornado
import tornado.ioloop


'''
Template for building a Python HTTP server using the tornado 
library. For building a secure server, i.e. one reachable
via HTTPS instead of HTTP, see tornado_ssl_template.
The actual code in this template is tiny, bloated only by 
all my comments. The official minimal Hello World is:

	  import tornado.ioloop
	  import tornado.web
	  
	  class MainHandler(tornado.web.RequestHandler):
	      def get(self):
	          self.write("Hello, world")
	  
	  if __name__ == "__main__":
	      application = tornado.web.Application([
	          (r"/", MainHandler),
	      ])
	      application.listen(8888)
	      tornado.ioloop.IOLoop.current().start()
	  


The principle is that tornado runs in an infinite loop that is 
started in the 'main' section of this template. You subclass
tornado.web.RequestHandler, overriding the get() and/or post()
methods. Your class constitutes a tornado 'application' that 
is associated with a port you specify. Tornado then continuously
listens to that port for HTTP requests, invoking your get()/post() 
methods as needed.

For more documentation, including threading, see 
http://tornadokevinlee.readthedocs.org/en/latest/web.html.

For testing your server, try http://hurl.it. It lets you
specify a full URL, such as http://myserver.com/myservice?foo=bar,
and will show you the response from your server.

'''

class MyClass(tornado.web.RequestHandler):
    '''
    Describe what this class does.
    '''


    def initialize(self):
        '''
        Use this method for initialization, not the 
        usual __init__(). Tornado makes no guarantees about
        the paramaters it expects for __init__(). The framework
        uses initialize() instead.
        '''
        pass
    
    def get(self):
        '''
        To handle HTTP GET messages, provide this get() method.
        URL query strings are provided as a dict in self.request.arguments. 
        Query strings are the URL part like ...?foo=bar&fum=10.
        '''
        
        # Anything you write or print to stdout
        # is sent to the requesting browser.
        self.write("<html><body>GET method was called: %s.</body></html>" % str(self.request.arguments))
        
    def post(self):
        '''
        If you want to handle HTTP POST requests,
        Provide this method. The passed-in info is
        provided as a dict in self.request.arguments.
        '''
        
        # Anything you write or print to stdout
        # is sent to the requesting browser.
        self.write("<html><body>POST method was called: %s.</body></html>" % str(self.request.arguments))


if __name__ == "__main__":

    # Create a tornado 'application'. The
    # regular expression r"/myservice" determines
    # how the incoming URL must look to invoke your
    # get() or post() methods. In this case URLs
    # must start with: http://myserver.com/myservice
    # and possbly have a query string attached: ?foo=bar&fum=10.
    # To have your service reachable at the top level, as
    # in http://myserver.com?color=blue, use r"/".
    
        
    application = tornado.web.Application([
            (r"/myservice", MyClass),
            ])

    # Tell tornado which port to listen to:
    application.listen(8080)
    
    print('Starting my service on port 8080.')    
    
    try:
        # Enter an infinite loop that can be
        # exited via cnt-C:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
            print('Stopping my service.')
            sys.exit()
    
