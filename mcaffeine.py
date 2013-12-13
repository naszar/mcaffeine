#!/usr/bin/python2
#based on: http://learngtk.org/pygtk-tutorial/statusicon.html
#icons from https://launchpad.net/caffeine  
import gtk
import os

EMPTY = "/usr/share/icons/hicolor/scalable/status/caffeine-cup-empty.svg"
FULL  = "/usr/share/icons/hicolor/scalable/status/caffeine-cup-full.svg"
DPMS_ACTIVE = True
DPMS_OFF = False

class StatusIcon:
    def __init__(self):
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_file(EMPTY)
        self.statusicon.connect("activate", self.left_click_event)
        self.statusicon.set_tooltip("StatusIcon Example")
        self.the_state = DPMS_ACTIVE
        self.statusicon.connect("popup-menu", self.right_click_event)
    def left_click_event(self, icon):
        if self.the_state == DPMS_ACTIVE:
            self.statusicon.set_from_file(FULL)
            self.the_state = DPMS_OFF
            os.system("xset dpms 0 0 0")
        else:
            self.statusicon.set_from_file(EMPTY)
            self.the_state = not self.the_state
            os.system("xset dpms 0 0 200")
    def right_click_event(self, icon, button, time):
        pass
StatusIcon()
gtk.main()

