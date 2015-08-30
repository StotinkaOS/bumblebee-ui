#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
#
# This file is part of bumblebee-ui.
#
# bumblebee-ui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# bumblebee-ui is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with bumblebee-ui. If not, see <http://www.gnu.org/licenses/>.
#
### END LICENSE

# UI MODULE
import pygtk
pygtk.require('2.0')
import gtk
import gobject

# SYSTEM MODULE
import os
import subprocess

# ORIGINAL CLASS
import Config
from AppSettings import Applications_settings, IconSet
from DesktopFile import DesktopFile, DesktopFileSet

class BumblebeeIndicator():

# INITIALIZATION OF INDICATOR AND MENU
    def __init__(self):
        self.ind = gtk.StatusIcon()
        self.ind.connect("popup-menu", self.build_menu)
        self.lock_file = "/tmp/.X%s-lock" % Config.vgl_display

    def quit(self, widget, data=None):
        gtk.main_quit()
        
    def pos(menu, ignore, icon):
        return (gtk.StatusIcon.position_menu(menu, icon))

    def build_menu(self, icon, button, time):
        self.menu = gtk.Menu()
        self.prefered_app_submenu = gtk.MenuItem("Preferred Apps")
        self.update_menu()
        self.prefered_app_submenu.connect('activate', self.update_menu)
        self.menu.append(self.prefered_app_submenu)
        
        item2 = gtk.MenuItem("Configure Apps")
        item2.connect("activate", self.app_configure)
        self.menu.append(item2)
        self.menu.show_all()

        self.menu.popup(None, None, None, button, time)
        
#TODO An UI to configure Bumblebee would be nice
	    
        self.build_menu_separator(self.menu)
        
        quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit.connect("activate", self.quit)
        self.menu.append(quit)
        
        self.menu.show_all()

    def build_menu_separator(self, menu):
    	separator = gtk.SeparatorMenuItem()
    	separator.show()
        menu.append(separator)

# FUNCTIONS TO BUILD THE "PREFERRED APP" MENU FROM THE LOCAL DESKTOP FILES
    def update_menu(self, widget=None):	
        pref_menu=gtk.Menu()
        self.add_submenu_items( pref_menu, Config.default_preferred_apps )
    	self.build_menu_separator( pref_menu )
        self.add_submenu_items( pref_menu, DesktopFileSet().get_configured_from_check() )
        pref_menu.show()
        self.prefered_app_submenu.set_submenu(pref_menu)

    def add_submenu_items(self, submenu, items_list):
        for Name, Exec_list in items_list : 
            subitem = gtk.MenuItem(label=Name)
            subitem.connect("activate", self.call_app, Exec_list)
        	subitem.show()
            submenu.append( subitem )
        
# FUNCTION TO DEFINE THE APPLICATIONS SETTING LINK IN THE INDICATOR

    def app_configure(self,widget):
        Applications_settings()

# FUNCTION TO LAUNCH THE APPS WITHIN THE INDICATOR
    def call_app(self, widget, app_exec):
#FIXME There is a problem when closing the launched app and when the indicator has been closed: the indicator is still running : What a daemon!!
        subprocess.Popen(app_exec,shell=False)
        
    def state_checker(self):
      if os.path.exists(self.lock_file):
        self.ind.set_from_file(gtk.icon_theme_get_default().lookup_icon("bumblebee-indicator-active", 48, 0).get_filename())
      else:
        self.ind.set_from_file(gtk.icon_theme_get_default().lookup_icon("bumblebee-indicator", 48, 0).get_filename())
      gobject.timeout_add_seconds(5, self.state_checker)

# MAIN LOOP LAUNCHING A STATE CHECK EVERY TWO SECONDS
    def main(self):
      self.state_checker()
      gtk.main()

if __name__ == "__main__":
    indicator = BumblebeeIndicator()
    indicator.main()
