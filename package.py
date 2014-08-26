#!/usr/bin/env python

from chip.packages import Package, wrap_install

class ConfigPackage(Package):
    def __init__(self, *args, **kwargs):
        super(ConfigPackage, self).__init__(*args, **kwargs)

    @wrap_install
    def install(self):
        with self.indir(self.build_path):
            self.run(['cp', './environment', '/pipeline'])

pk = ConfigPackage("config-pipeline@1.0.0")
pk.main()
