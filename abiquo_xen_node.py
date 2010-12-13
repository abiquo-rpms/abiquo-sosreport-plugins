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

class abiquo_xen_node(sos.plugintools.PluginBase):
    """Abiquo xen node related information
    """
    def checkenabled(self):
       if self.cInfo["policy"].pkgByName("openwsman") and self.cInfo["policy"].pkgByName("abiquo-xen") and self.cInfo["policy"].pkgByName("abiquo-rimp"):
          return True
       return False

    def setup(self):
        # Xen log
        self.addCopySpec("/var/log/xen/")
        
        #openwsmand conf
        self.addCopySpec("/etc/openwsman/")

        #Libvirt conf
        self.addCopySpec("/etc/libvirt/")

        #Xen conf
        self.addCopySpec("/etc/xen/")
        
        self.collectExtOutput("virsh capabilities")

        return
