### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools
import os
import re
import tempfile

class abiquo_server(sos.plugintools.PluginBase):
    """Abiquo server related information
    """
    def checkenabled(self):
       if self.cInfo["policy"].pkgByName("abiquo-server") or os.path.exists("/opt/abiquo/tomcat/webapps/server"):
          return True
       return False

    def setup(self):
        # tomcat log
        self.addCopySpec("/opt/abiquo/tomcat/logs/catalina.out")
        self.addCopySpec("/opt/abiquo/tomcat/logs/vsm.log")
        self.addCopySpec("/opt/abiquo/tomcat/logs/ssm.log")
        self.addCopySpec("/opt/abiquo/tomcat/logs/server.log")
        self.addCopySpec("/opt/abiquo/tomcat/logs/virtualfactory.log")
        self.addCopySpec("/opt/abiquo/tomcat/logs/am.log")
        self.addCopySpec("/opt/abiquo/tomcat/logs/nodecollector.log")

        self.addCopySpec("/opt/abiquo/config/")

        #conf files
        self.addCopySpec("/opt/abiquo/tomcat/webapps/am/WEB-INF/classes/conf/config.xml")
        self.addCopySpec("/opt/abiquo/tomcat/webapps/server/WEB-INF/classes/conf/config.xml")
        self.addCopySpec("/opt/abiquo/tomcat/webapps/virtualfactory/WEB-INF/classes/conf/config.xml")
        self.addCopySpec("/opt/abiquo/tomcat/webapps/vsm/WEB-INF/classes/conf/config.xml")
        self.addCopySpec("/opt/abiquo/tomcat/webapps/nodecollector/WEB-INF/classes/conf/config.xml")
        self.addCopySpec("/opt/abiquo/tomcat/conf/")

        #MySQL dump
        jndiFile = open("/opt/abiquo/tomcat/conf/Catalina/localhost/server.xml").read()
        dbUsername, dbPassword = re.search(r'username="([^"]+)"\s+password="([^"]*)"', jndiFile).groups()

        dbSearch = re.search(r'url="[^:]+:[^:]+://(?P<host>[^:]+)(:(?P<port>[^/]+))?/(?P<schema>.+)\?.+"', jndiFile)
        dbHost = dbSearch.group('host')
        dbPort = dbSearch.group('port')
        if dbPort == None:
            dbPort = '3306'
        dbSchema = dbSearch.group('schema')
        
        self.collectExtOutput("mysqldump -h "+dbHost+" -P "+dbPort+" -u "+dbUsername+" --password="+dbPassword+" "+dbSchema)

        return
