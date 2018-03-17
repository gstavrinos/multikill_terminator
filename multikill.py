#!/usr/bin/env python2
import os
import gtk
import signal
#from util import dbg
import terminatorlib.plugin as plugin
from terminatorlib.util import err, dbg
from terminatorlib.terminator import Terminator
from terminatorlib.translation import _

# AVAILABLE must contain a list of all the classes that you want exposed
AVAILABLE = ['MultiKill']

class MultiKill(plugin.MenuItem):
    capabilities = ['terminal_menu']

    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
        item = gtk.MenuItem(_('MultiKill!'))
        item.connect("activate", self.multiKill, terminal)
        menuitems.append(item)

    def multiKill(self, widget, terminal):
        dbg('got here!')
        for t in Terminator().terminals:
            try:
                dbg('close: killing %d' % self.pid)
                os.kill(t.pid, signal.SIGHUP)
            except Exception, ex:
                dbg('os.kill failed: %s' % ex)
                pass