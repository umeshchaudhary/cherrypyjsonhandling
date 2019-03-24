#!/usr/bin/python
"""
  pip install cherrypy, simplejson
  python server.py
"""
import cherrypy
import cherrypy_cors
import simplejson

PAGE = [None]
 
class Server(object):

    @cherrypy.expose
    def healthy(self):
        print('in healthy')
        return 'Success'
     
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def read_page(self, **kwargs):
      if cherrypy.request.method.upper() == "OPTIONS":
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'auth_token, Content-Type, Authorization'
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        return "OK"
      global PAGE
      PAGE[0] = cherrypy.request.json['page']
      print(PAGE[0][:100]) 
      return 'OK'
    
    @cherrypy.expose
    def parse_page(self):
      global PAGE
      print(PAGE[0])
      print(len(PAGE[0]))
      return PAGE[0]

if __name__ == '__main__':
    server = Server()
    cherrypy_cors.install()

    cherrypy.tree.mount(server, '/')

    cherrypy.engine.start()
    cherrypy.engine.block()


"""
$.ajax({
    url: 'http://localhost:8080/read-page',
    type: 'post',
    data: '{"page": '+JSON.stringify(document.documentElement.innerHTML)+'}',
    headers: {
        "Content-Type": 'application/json'
    },
    dataType: 'text/heml',
    success: function (data) {
        console.info(data);
    }
});
"""
