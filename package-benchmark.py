#!/usr/bin/env python

import os
from chip.packages import Package, wrap_install, wrap_default
from chip.log import createLogger
logger = createLogger('chip')

class BenchmarkPackage(Package):
    def __init__(self, *args, **kwargs):
        super(ConfigPackage, self).__init__(*args, **kwargs)

    @wrap_install
    def install(self):
        logger.info("Running benchmark suite, this may take several minutes")
        with self.indir(self.build_path):
            cmd = './Run -q -i 1 dhry whets > BENCHMARK.txt 2>&1 </dev/null '
            self.run(cmd.split())

        # TODO - either process results and put in extra or put in environment
        # variables which dependers should know about

    @wrap_default('activate')
    def activate(self):
        pass

    @wrap_default('deactivate')
    def deactivate(self):
        pass

pkg = BenchmarkPackage
