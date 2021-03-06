from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import urllib2
import json
import logging
import cgi
import time
from BinarySearchTree__Sort import Node
from BinarySearchTree__Sort import TreeSort

class MainPage( webapp.RequestHandler ):

  def get( self ):
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <title>Binary Search Tree Sort on Google App Engine</title>')
    self.response.out.write('<link rel="stylesheet" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" type="text/css">')
    self.response.out.write('<link rel="stylesheet" href="http://yui.yahooapis.com/2.7.0/build/base/base.css" type="text/css">')
    self.response.out.write('<link rel="stylesheet" href="css/style.css">')
    self.response.out.write('</head><body>')
    self.response.out.write("""
<div id="doc2" class="yui-t7">
<div id="hd" role="banner"><h1>Binary Search Tree Sort</h1></div>
<div id="bd" role="main">
<form action="/search" method="post" id="mainform">
          <div>
               <label for="search">Enter a vector:</label>
               <input type="text" name="search" id="search" value=""/>
               <input type="submit" value="Go!">
          </div>
</form>
<p class="info">Binary Search Tree Sort</p>
<div id="ft" role="contentinfo"><p>follow me @<a href="http://twitter.com/thinkphp">thinkphp</a></p></div>
</div></body></html>""")

class Controller(webapp.RequestHandler):

      def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<html><head><title>Quick Sort on Google App Engine</title><style type="text/css">body {background:#fff;font-family: Helvetica Neue, Arial, sans-serif; margin-left: 15px;}h1 { font-size: 120px; }p { margin-top: 20px; font-size: 30px; } a { color: #00b7ff; }</style></head><body>')
        self.response.out.write('<h1>&#65;&#100;&#114;&#105;&#97;&#110;&#32;&#83;&#116;&#97;&#116;&#101;&#115;&#99;&#117;</h1>')
        self.response.out.write('<p>&#116;&#119;&#105;&#116;&#116;&#101;&#114; @<a href="&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#116;&#119;&#105;&#116;&#116;&#101;&#114;&#46;&#99;&#111;&#109;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;">&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;</a></p>')
        self.response.out.write('<p>&#119;&#101;&#98;&#115;&#105;&#116;&#101;  <a href="&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;&#46;&#114;&#111;">&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;&#46;&#114;&#111;</a></p>')
        self.response.out.write('<p>&#98;&#108;&#111;&#103; <a href="&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;&#46;&#114;&#111;&#47;&#98;&#108;&#111;&#103;">&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;&#46;&#114;&#111;&#47;&#98;&#108;&#111;&#103;</a></p>')
        self.response.out.write('<p>&#112;&#114;&#111;&#106;&#101;&#99;&#116;&#115; <a href="&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#103;&#105;&#116;&#104;&#117;&#98;&#46;&#99;&#111;&#109;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;">&#104;&#116;&#116;&#112;&#58;&#47;&#47;&#103;&#105;&#116;&#104;&#117;&#98;&#46;&#99;&#111;&#109;&#47;&#116;&#104;&#105;&#110;&#107;&#112;&#104;&#112;</a></p>')
        self.response.out.write('<body></html>')

      def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <title>Binary Search Tree Sort on Google App Engine</title>')
        self.response.out.write('<link rel="stylesheet" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" type="text/css">')
        self.response.out.write('<link rel="stylesheet" href="http://yui.yahooapis.com/2.7.0/build/base/base.css" type="text/css">')
        self.response.out.write('<link rel="stylesheet" href="css/style.css">')
        self.response.out.write('</head><body>')
        self.response.out.write("""
<div id="doc2" class="yui-t7">
<div id="hd" role="banner"><h1>Bin Search Tree Sort</h1></div>
<div id="bd" role="main">

<form action="/search" method="post" id="mainform">
          <div>
               <label for="search">Enter a vector:</label>
               <input type="text" name="search" id="search" value=""/>
               <input type="submit" value="Sorted!">
          </div>
</form><p class="info">Worst-case running time is O(n long n) if balanced</p><p class="info">Worst-case running time is O(n^2) if unbalanced</p><p class="info">Best-case running time is O(n log n)</p><p class="info">Average-case running time is O(n Log n)</p>""")

        ob = TreeSort()

        out = [] 

        q = cgi.escape(self.request.get('search')) 

        q = q.split(',')

        for val in q:

            ob.add( int(val)) 

            out.append( int( val ) )  

        #travers the tree in order way.
        ob.travers( )

        start_time = time.clock()       

        self.response.write('<div class="yui-u">') 

        self.response.write('<div class="yui-u"><h4 style="color: #3c3;font-size: 70px">') 
     
        #display the sorted array
        self.response.write( ob.getSorted( ) )

        self.response.write('</h4>')

        self.response.write('<br/><p style="color: #c1c1d1">')        
        self.response.write( 'Input -> ')     
        self.response.write( out )

        self.response.write('</p>')        
        self.response.write( ("Time execution: %s seconds " % (time.clock() - start_time)) )
        self.response.write('</p>')        

        self.response.write('<div id="ft" role="contentinfo"><p>Created by @<a href="http://thinkphp.ro">Adrian Statescu</a> | <a href="https://github.com/thinkphp/bstsortpy">Fork on GitHub</a></p></div>')
        self.response.write('</div></body></html>')

application = webapp.WSGIApplication([

  ('/', MainPage),

  ('/search', Controller)

], debug=True)


def main():

    run_wsgi_app(application)

if __name__ == '__main__':
  main()