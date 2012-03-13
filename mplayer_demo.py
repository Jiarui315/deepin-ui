#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Wang Yong
# 
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from dtk.ui.application import Application
from dtk.ui.constant import *
from dtk.ui.theme import *
from dtk.ui.utils import *
from dtk.ui.frame import *
from dtk.ui.mplayer_view import *

def show_video(widget, xid):
    '''Show video.'''
    run_command("mplayer -wid %s %s" % (xid, "/data/Video/Manatee.avi"))
    
if __name__ == "__main__":
    # Init application.
    application = Application("demo", False)

    # Set application default size.
    application.set_default_size(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
    
    # Set application icon.
    application.set_icon(ui_theme.get_pixbuf("icon.ico"))
    
    # Add titlebar.
    application.add_titlebar(
        ["theme", "menu", "max", "min", "close"], 
        ui_theme.get_pixbuf("title.png"), 
        "电影播放器",
        "深度Linux视频演示")
    
    # Add mplayer view.
    mplayer_view = MplayerView()
    mplayer_view.connect("get-xid", show_video)
    mplayer_frame = HorizontalFrame()
    mplayer_frame.add(mplayer_view)
    application.main_box.pack_start(mplayer_frame)
    
    # Run.
    application.run()
    
    
