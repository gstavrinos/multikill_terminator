import signal
import terminatorlib.plugin as plugin
from terminatorlib.util import err, dbg
from terminatorlib.translation import _
from terminatorlib.terminator import Terminator
from terminatorlib.version import APP_VERSION

if float(APP_VERSION) <= 0.98:
    import gtk as Gtk
else:
    import gi
    from gi.repository import Gtk, Gdk

#err('\033[1;31m %s \033[0m' % APP_VERSION)

# AVAILABLE must contain a list of all the classes that you want exposed
AVAILABLE = ['MultiKill']

class MultiKill(plugin.MenuItem):
    capabilities = ['terminal_menu']

    def __init__(self):
        plugin.MenuItem.__init__(self)
        self.entry = Terminator().windows[0]
        self.entry.connect('key-release-event', self.onKeyPress)
        

    def callback(self, menuitems, menu, terminal):
        item = Gtk.MenuItem(_('MultiKill!'))
        item.connect("activate", self.multiKill)
        menuitems.append(item)

    def multiKill(self, widget):
        for t in Terminator().terminals:
            try:
                t.vte.feed_child("\x03", len("\x03"))
            except Exception, ex:
                err('\033[1;31mMultikill failed: %s\033[0m' % ex)
                pass

    def onKeyPress(self, widget, event):
        if float(APP_VERSION) <= 0.98:
            if (event.state & Gtk.gdk.MOD1_MASK == Gtk.gdk.MOD1_MASK) and (event.keyval == 67 or event.keyval == 99): # Alt+C or Alt+c
                self.multiKill(widget)
        else:
            if (event.state & Gdk.ModifierType.MOD1_MASK == Gdk.ModifierType.MOD1_MASK) and (event.keyval == 67 or event.keyval == 99): # Alt+C or Alt+c
                self.multiKill(widget)
