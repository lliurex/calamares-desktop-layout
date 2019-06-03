#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <https://github.com/calamares> ===
#
#   Copyright 2014-2015, Philip Müller <philm@manjaro.org>
#   Copyright 2015-2017, Teo Mrnjavac <teo@kde.org>
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#   Copyright 2017, Adriaan de Groot <groot@kde.org>
#   Copyright 2017, Gabriel Craciunescu <crazy@frugalware.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import os

def system_addons(config):
    '''
        Create link to resolv.conf
    '''
    layout = 'default'
    if config['layout'] == 'classic':
        layout = 'classic'
    libcalamares.utils.target_env_call(['llx-desktop-layout','set',layout])
    return None

def run():
    """
    Create ubiquity modifications
    :return:
    """
    config = libcalamares.globalstorage.value('desktoplayout')
    return system_addons(config)