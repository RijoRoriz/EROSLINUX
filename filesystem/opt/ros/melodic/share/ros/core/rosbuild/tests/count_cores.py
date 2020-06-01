#!/usr/bin/env python2

import os
print(os.sysconf(os.sysconf_names['SC_NPROCESSORS_ONLN']))
