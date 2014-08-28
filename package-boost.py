#!/usr/bin/env python

import os
from chip.packages import Package, wrap_install, wrap_default

class BoostPackage(Package):
    def __init__(self, *args, **kwargs):
        super(ConfigPackage, self).__init__(*args, **kwargs)
        self.libpath = os.path.join(self.build_path, "lib")
        self.incpath = os.path.join(self.build_path, "include")

    @wrap_install
    def install(self):
        pass

    @wrap_default('activate')
    def activate(self):
        self.path_push(self.libpath, "LIBRARY_PATH") 
        self.path_push(self.incpath, "CPLUS_INCLUDE_PATH") 

    @wrap_default('deactivate')
    def deactivate(self):
        self.path_pull(self.libpath, "LIBRARY_PATH") 
        self.path_pull(self.incpath, "CPLUS_INCLUDE_PATH") 

pkg = BoostPackage
