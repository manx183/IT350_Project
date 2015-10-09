import cherrypy
import MySQLdb

def connect(thread_index):
	# Create a connectiona nd store it int he current thread
	cherrypy.thread_data.db = MySQLdb.connect('localhost', 'user', 'password', 'database')

# Tell CherryPy to call "connect" for each thread, when it starts up
cherrypy.engine.subscribe('start_thread', connect)

class Root:
	def index(self):
		#sample page that displays the number of records in "table"
		#open a cursor, using the DB connection for the current thread
		c = cherrypy.thread_data.db.cursor()
		c.execute('select count(*) from Student')
		res = c.fetchone()
		c.close()
		return "<html><body>Hello, you have %d records in your table</body></html>" % res[0]
	index.exposed = True

cherrypy.quickstart(Root())
