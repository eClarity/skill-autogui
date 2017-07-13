# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import pyautogui
import platform

__author__ = 'eClarity'

LOGGER = getLogger(__name__)


class AutoguiSkill(MycroftSkill):
    def __init__(self):
        super(AutoguiSkill, self).__init__(name="AutoguiSkill")

    def initialize(self):
        type_intent = IntentBuilder("TypeIntent"). \
            require("TypeKeyword").require("Text").build()
        self.register_intent(type_intent, self.handle_type_intent)

        press_enter_intent = IntentBuilder("PressEnterIntent"). \
            require("PressEnterKeyword").build()
        self.register_intent(press_enter_intent, self.handle_press_enter_intent)

        mouse_absolute_intent = IntentBuilder("MouseAbsoluteIntent"). \
            require("MouseAbsoluteKeyword").require("X").require("Y").build()
        self.register_intent(mouse_absolute_intent, self.handle_mouse_absolute_intent)

        mouse_scroll_down_intent = IntentBuilder("MouseScrollDownIntent"). \
            require("MouseScrollDownKeyword").require("Scroll").build()
        self.register_intent(mouse_scroll_down_intent, self.handle_mouse_scroll_down_intent)

        mouse_scroll_up_intent = IntentBuilder("MouseScrollUpIntent"). \
            require("MouseScrollUpKeyword").require("Scroll").build()
        self.register_intent(mouse_scroll_up_intent, self.handle_mouse_scroll_up_intent)

        mouse_scroll_right_intent = IntentBuilder("MouseScrollRightIntent"). \
            require("MouseScrollRightKeyword").require("Scroll").build()
        self.register_intent(mouse_scroll_right_intent, self.handle_mouse_scroll_right_intent)

    def handle_type_intent(self, message):
	self.speak_dialog("typing")
	text = message.data.get('Text')
        pyautogui.typewrite(text, interval=0.05)

    def handle_press_enter_intent(self, message):
	self.speak('pressing enter')
        pyautogui.press('enter')

    def handle_mouse_absolute_intent(self, message):
	self.speak('moving mouse now')
	#X = message.data.get('X')
	#Y = message.data.get('Y')
        #pyautogui.moveTo(X, Y)

    def handle_mouse_scroll_down_intent(self, message):
        self.speak('scrolling down now')
        scroll = message.data.get('Scroll')
        scroll_down = int(scroll) * -1
	pyautogui.scroll(scroll_down)

    def handle_mouse_scroll_up_intent(self, message):
        self.speak('scrolling up now')
        scroll = message.data.get('Scroll')
        scroll_up = int(scroll)
	pyautogui.scroll(scroll_up)

    def handle_mouse_scroll_right_intent(self, message):
        if platform.system().lower().startswith('lin'):
            self.speak('scrolling right now')
            scroll = message.data.get('Scroll')
            scroll_right = int(scroll)
	    pyautogui.hscroll(scroll_right)
        else:
            self.speak('Sorry, I cannot scroll right on your current operating system')

    def stop(self):
        pass


def create_skill():
    return AutoguiSkill()
        pyautogui.press('enter')


    def stop(self):
        pass


def create_skill():
    return AutoguiSkill()
