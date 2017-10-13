#!/usr/bin/env python3

import i3ipc

i3 = i3ipc.Connection()
colormode = '%{F{{ n_red }} }'

def on_mode(self, e):
    if e.change != 'default':
        modestr = colormode + '  ' + e.change
    else:
        modestr = ' '
    print(modestr, flush=True)

i3.on('mode', on_mode)

i3.main()

