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
       if self.cInfo["policy"].pkgByName("abiquo-core") or os.path.exists("/opt/abiquo/tomcat/webapps/"):
          return True
       return False

    def setup(self):
        # tomcat log
        self.addCopySpec("/opt/abiquo/tomcat/logs/")


        #conf files
        self.addCopySpec("/opt/abiquo/config/")
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
