from gi.repository import Gtk, Gdk
#import gtk
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
        err('\033[1;31m 1 \033[0m')
        self.entry = Terminator().windows[0]
        err('\033[1;31m 2 \033[0m')
        self.entry.connect('key-release-event', self.onKeyPress)
        err('\033[1;31m 3 \033[0m')
        

    def callback(self, menuitems, menu, terminal):
        err('\033[1;31m 4 \033[0m')
        item = Gtk.MenuItem(_('MultiKill!'))
        err('\033[1;31m 5 \033[0m')
        item.connect("activate", self.multiKill)
        err('\033[1;31m 6 \033[0m')
        menuitems.append(item)
        err('\033[1;31m 7 \033[0m')

    def multiKill(self, widget):
        err('\033[1;31m 8 \033[0m')
        for t in Terminator().terminals:
            err('\033[1;31m 9 \033[0m')
            try:
                t.vte.feed_child("\x03", len("\x03"))
            except Exception, ex:
                err('\033[1;31mMultikill failed: %s\033[0m' % ex)
                pass

    def onKeyPress(self, widget, event):
        err('\033[1;31m 666 \033[0m')
        if (event.state & Gdk.ModifierType.MOD1_MASK == Gdk.ModifierType.MOD1_MASK) and (event.keyval == 67 or event.keyval == 99): # Alt+C or Alt+c
            err('\033[1;31m 777 \033[0m')
            self.multiKill(widget)
