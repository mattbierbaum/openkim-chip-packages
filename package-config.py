#!/usr/bin/env python

import os
import uuid
import subprocess
from chip.packages import Package, wrap_install, wrap_default

class ConfigPackage(Package):
    def __init__(self, *args, **kwargs):
        super(ConfigPackage, self).__init__(*args, **kwargs)
        self.home = "/pipeline"

    @wrap_install
    def install(self):
        if not os.path.exists(self.home):
            subprocess.check_call(['sudo', 'mkdir', '-p', self.home])

        with self.indir(self.build_path):
            self.run(['cp', './environment', self.home])

        u = str(uuid.uuid4())

        with open(os.path.join(self.home, 'environment.extra'), 'w') as f:
            f.write("UUID="+u)

    @wrap_default('activate')
    def activate(self):
        pass

    @wrap_default('deactivate')
    def deactivate(self):
        pass

pkg = ConfigPackage
