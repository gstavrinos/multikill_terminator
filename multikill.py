#!/usr/bin/env python2
import os
import gtk
import signal
import terminatorlib.plugin as plugin
from terminatorlib.util import err, dbg
from terminatorlib.translation import _
from terminatorlib.terminator import Terminator

# AVAILABLE must contain a list of all the classes that you want exposed
AVAILABLE = ['MultiKill']

class MultiKill(plugin.MenuItem):
    capabilities = ['terminal_menu']

    def __init__(self):
        plugin.MenuItem.__init__(self)
        #self.entry = gtk.Window()

    def callback(self, menuitems, menu, terminal):
        #self.entry.connect('key-press-event', self.onKeyPress)
        item = gtk.MenuItem(_('MultiKill!'))
        item.connect("activate", self.multiKill)
        menuitems.append(item)

    def multiKill(self, widget):
        for t in Terminator().terminals:
            try:
                t.vte.feed_child("\x03")
            except Exception, ex:
                dbg('\033[1;31mMultikill failed: %s\033[0m' % ex)
                pass

    # def onKeyPress(self, widget, event):
    #     dbg('\033[1;31m'+str(key)+'\033[0m')
    #     if event.state == gtk.gdk.MOD1_MASK and (event.keyval == 67 or event.keyval == 99: # Alt+C or Alt+c
    #         self.multiKill(self, widget)

# TODO add keyboard shortcut
# Commented out lines move towards that direction