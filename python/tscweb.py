import cherrypy
import sqlite3
import MySQLdb
import json

class TscWebApp(object):
    @cherrypy.expose
    def index(self):
        return "Tactical Space Combat"
    
    @cherrypy.expose
    def list(self):
        db = MySQLdb.connect(host="tscdb.cvnkrcajufxo.us-east-1.rds.amazonaws.com", user="tscdbsa", passwd="P1llar0fAutumn", port=3306, db="tsc")
        c = db.cursor()
        c.execute("select * from v_list_ships")
        r = []
        l = c.fetchone()
        while l is not None:
            r.append(l)
            l = c.fetchone()
        c.close()
        db.close()
        return json.dumps(r)
        

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host':'0.0.0.0', 'server.socket_port': 9090})
    cherrypy.quickstart(TscWebApp())
    
    
