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
import webbrowser
from mtranslate import translate




__author__ = 'oren'

LOGGER = getLogger(__name__)

def translate(sentence):
    translated = translate(sentence, "zh")
    return translated


class TranslateSkill(MycroftSkill):
    def __init__(self):
        super(TranslateSkill, self).__init__(name="TranslateSkill")

    def initialize(self):
        translate_intent = IntentBuilder("TranslateIntent"). \
            require("TranslateKeyword").optionally("Word").build()
        self.register_intent(translate_intent,
                             self.handle_translate_intent)

    def handle_translate_intent(self, message):
        word = message.data["Word"]
        print("----------------------")
        print(word)
        print("----------------------")
        word = translate(word)
        self.speak(word)
        webbrowser.open('http://google.com/?q=' + word)

    def stop(self):
        pass


def create_skill():
    return TranslateSkill()
