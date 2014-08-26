#!/usr/bin/env python

from chip.packages import Package, wrap_install, wrap_default

class ConfigPackage(Package):
    def __init__(self, *args, **kwargs):
        super(ConfigPackage, self).__init__(*args, **kwargs)

    @wrap_install
    def install(self):
        with self.indir(self.build_path):
            self.run(['cp', './environment', '/pipeline'])

    @wrap_default('activate')
    def activate(self):
        self.path_push('hahlol', "CONF") 

    @wrap_default('deactivate')
    def deactivate(self):
        self.path_pull('hahlol', "CONF") 

pk = ConfigPackage("config-pipeline@1.0.0")
pk.main()
