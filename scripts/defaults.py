import focus      # add some default focus handling and cycling functions
import focusmodel # default focus models
import behavior   # defines default behaviors for interaction with windows
import callbacks  # a lib of functions that can be used as binding callbacks
import windowplacement # use a routine in here to place windows

# try focus something when nothing is focused
focus.fallback = 1

# set up the mouse buttons
focusmodel.setup_click_focus() # use focusmodel.setup_sloppy_focus() instead to
                               # make focus follow the cursor
behavior.setup_window_clicks()
behavior.setup_window_buttons()
behavior.setup_scroll()

# my window placement algorithm
ob.ebind(ob.EventAction.PlaceWindow, windowplacement.random)

# run xterm from root clicks
ob.mbind("Left", ob.MouseContext.Root, ob.MouseAction.Click,
         lambda(d): ob.execute("xterm", d.screen))

ob.kbind(["A-F4"], ob.KeyContext.All, callbacks.close)

# focus bindings
ob.kbind(["A-Tab"], ob.KeyContext.All, focus.focus_next_stacked)
ob.kbind(["A-S-Tab"], ob.KeyContext.All, focus.focus_prev_stacked)

# desktop changing bindings
ob.kbind(["C-1"], ob.KeyContext.All, lambda(d): callbacks.change_desktop(d, 0))
ob.kbind(["C-2"], ob.KeyContext.All, lambda(d): callbacks.change_desktop(d, 1))
ob.kbind(["C-3"], ob.KeyContext.All, lambda(d): callbacks.change_desktop(d, 2))
ob.kbind(["C-4"], ob.KeyContext.All, lambda(d): callbacks.change_desktop(d, 3))
ob.kbind(["C-A-Right"], ob.KeyContext.All,
         lambda(d): callbacks.next_desktop(d))
ob.kbind(["C-A-Left"], ob.KeyContext.All,
         lambda(d): callbacks.prev_desktop(d))

ob.kbind(["C-S-A-Right"], ob.KeyContext.All,
         lambda(d): callbacks.send_to_next_desktop(d))
ob.kbind(["C-S-A-Left"], ob.KeyContext.All,
         lambda(d): callbacks.send_to_prev_desktop(d))

# focus new windows
ob.ebind(ob.EventAction.NewWindow, callbacks.focus)

print "Loaded defaults.py"
