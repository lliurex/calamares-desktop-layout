#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2018, Raul Rodrigo Segura <raurodse@gmail.com>
#
#   GPLv3

from PythonQt.QtGui import *
from PythonQt.QtCore import *
from PythonQt.QtSvg import QSvgWidget
import PythonQt.calamares as calamares

# Set up translations.
# You may skip this if your Calamares module has no user visible strings.
# DO NOT install _ into the builtin namespace because each module loads
# its own catalog.
# DO use the gettext class-based API and manually alias _ as described in:
# https://docs.python.org/3.5/library/gettext.html#localizing-your-module
import gettext
import inspect
import os
_filename = inspect.getframeinfo(inspect.currentframe()).filename
_path = os.path.dirname(os.path.abspath(_filename))
gettext.textdomain('calamares-otheraddons')
_ = gettext.gettext

# Example Python ViewModule.
# A Python ViewModule is a Python program which defines a ViewStep class.
# One UI module ==> one ViewStep.
# This class must be marked with the @calamares_module decorator. A
# ViewModule may define other classes, but only one may be decorated with
# @calamares_module. Such a class must conform to the Calamares ViewStep
# interface and functions as the entry point of the module.
# A ViewStep manages one or more "wizard pages" through methods like
# back/next, and reports its status through isNextEnabled/isBackEnabled/
# isAtBeginning/isAtEnd. The whole UI, including all the pages, must be
# exposed as a single QWidget, returned by the widget function.
#
# For convenience, both C++ and PythonQt ViewSteps are considered to be
# implementations of ViewStep.h. Additionally, the Calamares PythonQt API
# allows Python developers to keep their identifiers more Pythonic on the
# Python side. Thus, all of the following are considered valid method
# identifiers in a ViewStep implementation: isNextEnabled, isnextenabled,
# is_next_enabled.


@calamares_module
class SystemAddonsViewStep:
    def __init__(self):
        self.configuration = {'layout':'default'}
        calamares.global_storage.insert('desktoplayout',self.configuration)
        self.translations = {"defaultlayout":"Default layout", "defaultlayoutdescription": "LliureX show two bars", "classiclayout" : "Classic layout","classiclayoutdescription" : "LliureX show one bar"}
        self.main_widget = QFrame()
        self.main_widget.setLayout(QVBoxLayout())
        qsa = QScrollArea()
        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        widget.layout().setAlignment(Qt.AlignCenter | Qt.AlignTop)
        qsa.setWidget(widget)
        qsa.setWidgetResizable(True)

        self.main_widget.layout().addWidget(qsa)

        widget.layout().addLayout(self.createDefaultLayout(False),False)
        widget.layout().addLayout(self.createClassicLayout(True),True)

        

    def createDefaultLayout(self,last):
        gLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout.addLayout(verticalLayout)

        image_package = self.createImage('/usr/share/plasma/look-and-feel/lliurex-desktop/contents/previews/preview.png')
        self.default_name = self.createName(_(self.translations['defaultlayout']))
        self.default_description = self.createDescription(_(self.translations['defaultlayoutdescription']))
        default_check = self.createRadio('default',True)

        verticalLayout.addWidget(self.default_name)
        verticalLayout.addWidget(self.default_description)
        verticalLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        verticalLayout.setContentsMargins(10,20,0,0)
        horizontalLayout.addWidget(default_check)

        gLayout.addWidget(image_package,0,0)
        gLayout.addLayout(horizontalLayout,0,1)
        gLayout.addLayout(self.add_line(),1,1)
        return gLayout


    def createClassicLayout(self,last):

        gLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        verticalLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        verticalLayout.setContentsMargins(10,20,0,0)
        horizontalLayout.addLayout(verticalLayout)
        
        image_package = self.createImage('/usr/share/plasma/look-and-feel/lliurex-desktop-classic/contents/previews/preview.png')
        self.classic_name = self.createName(_(self.translations['classiclayout']))
        self.classic_description = self.createDescription(_(self.translations['classiclayoutdescription']))
        classic_check = self.createRadio('classic',False)

        verticalLayout.addWidget(self.classic_name)
        verticalLayout.addWidget(self.classic_description)
        horizontalLayout.addWidget(classic_check)

        gLayout.addWidget(image_package,0,0)
        gLayout.addLayout(horizontalLayout,0,1)
        return gLayout

    def createImage(self,path_image):
        label = QLabel()
        label.setText("")
        label.setScaledContents(True)
        label.setPixmap(QIcon(path_image).pixmap(300,169))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        label.setSizePolicy(sizePolicy)
        label.setMaximumSize(QSize(300,169))
        label.setObjectName("imagePackage")
        return label

    def createName(self,name):
        label_3 = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        label_3.setFont(font)
        label_3.setObjectName("label_3")
        label_3.setStyleSheet("QLabel{margin-left:5px; }")
        label_3.setText(_(name))
        return label_3

    def createDescription(self,description):
        label_2 = QLabel()
        label_2.setWordWrap(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        label_2.setSizePolicy(sizePolicy)
        label_2.setObjectName("label_2")
        label_2.setStyleSheet("QLabel{margin-left:5px ; color: #666 }")
        label_2.setText(_(description))
        return label_2

    def createRadio(self,layout_selected, selected):
        radioButton = QRadioButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        radioButton.setSizePolicy(sizePolicy)
        radioButton.setObjectName("checkBox")
        radioButton.setChecked(selected)
        radioButton.connect("clicked(bool)",lambda: self.modify_value(layout_selected))
        return radioButton

    def add_line(self):
        layout = QVBoxLayout()
        line = QWidget()
        line.setFixedHeight(2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        line.setSizePolicy(sizePolicy)
        line.setStyleSheet("QWidget{background-color: #ccc}")
        line.setObjectName("line")
        layout.addWidget(line)
        layout.setContentsMargins(20,5,0,0)
        return layout

    def modify_value(self,value):
        configuration = calamares.global_storage.value('desktoplayout')
        configuration['layout'] = value
        calamares.global_storage.insert('desktoplayout',configuration)

    def prettyName(self):
        return _("Desktop layout")

    def isNextEnabled(self):
        return True  # The "Next" button should be clickable

    def isBackEnabled(self):
        return True  # The "Back" button should be clickable

    def isAtBeginning(self):
        # True means the currently shown UI page is the first page of this
        # module, thus a "Back" button click will not be handled by this
        # module and will cause a skip to the previous ViewStep instead
        # (if any). False means that the present ViewStep provides other UI
        # pages placed logically "before" the current one, thus a "Back" button
        # click will be handled by this module instead of skipping to another
        # ViewStep. A module (ViewStep) with only one page will always return
        # True here.
        return True

    def isAtEnd(self):
        # True means the currently shown UI page is the last page of this
        # module, thus a "Next" button click will not be handled by this
        # module and will cause a skip to the next ViewStep instead (if any).
        # False means that the present ViewStep provides other UI pages placed
        # logically "after" the current one, thus a "Next" button click will
        # be handled by this module instead of skipping to another ViewStep.
        # A module (ViewStep) with only one page will always return True here.
        return True

    def jobs(self):
        # Returns a list of objects that implement Calamares::Job.
        return []

    def widget(self):
        # Returns the base QWidget of this module's UI.
        return self.main_widget

    def retranslate(self, locale_name):
        # This is where it gets slightly weird. In most desktop applications we
        # shouldn't need this kind of mechanism, because we could assume that
        # the operating environment is configured to use a certain language.
        # Usually the user would change the system-wide language in a settings
        # UI, restart the application, done.
        # Alas, Calamares runs on an unconfigured live system, and one of the
        # core features of Calamares is to allow the user to pick a language.
        # Unfortunately, strings in the UI do not automatically react to a
        # runtime language change. To get UI strings in a new language, all
        # user-visible strings must be retranslated (by calling tr() in C++ or
        # _() in Python) and reapplied on the relevant widgets.
        # When the user picks a new UI translation language, Qt raises a QEvent
        # of type LanguageChange, which propagates through the QObject
        # hierarchy. By catching and reacting to this event, we can show
        # user-visible strings in the new language at the right time.
        # The C++ side of the Calamares PythonQt API catches the LanguageChange
        # event and calls the present method. It is then up to the module
        # developer to add here all the needed code to load the module's
        # translation catalog for the new language (which is separate from the
        # main Calamares strings catalog) and reapply any user-visible strings.
        calamares.utils.debug("PythonQt retranslation event "
                              "for locale name: {}".format(locale_name))

        # First we load the catalog file for the new language...
        
        try:
            global _
            _t = gettext.translation('desktoplayout',
                                     localedir=os.path.join(_path, 'lang'),
                                     languages=[locale_name])
            
            _ = _t.gettext
        except OSError as e:
            calamares.utils.debug(os.path.join(_path, 'lang'))
            calamares.utils.debug(locale_name)
            calamares.utils.debug(e)
            pass
        
        self.default_name.setText(_(self.translations['defaultlayout']))
        self.default_description.setText(_(self.translations['defaultlayoutdescription']))
        self.classic_name.setText(_(self.translations['classiclayout']))
        self.classic_description.setText(_(self.translations['classiclayoutdescription']))
