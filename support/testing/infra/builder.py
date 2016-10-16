import os
import shutil
import subprocess

import infra

class Builder(object):
    def __init__(self, config, builddir, logtofile):
        self.config = config
        self.builddir = builddir
        self.logtofile = logtofile
        cur_filepath = os.path.abspath(__file__)
        self.cur_dir = os.path.dirname(cur_filepath)

    def build(self):
        if not os.path.isdir(self.builddir):
            os.makedirs(self.builddir)

        log = "{}-build.log".format(self.builddir)
        if self.logtofile is None:
            log = None

        config_file = "{}.config".format(self.builddir)
        with open(config_file, "w+") as cfd:
            cfd.write(self.config)

        cmd = ["make",
               "-C", self.cur_dir,
               "O={}".format(self.builddir),
               "olddefconfig"]
        with infra.smart_open(log) as log_fh:
            ret = subprocess.call(cmd, stdout=log_fh, stderr=log_fh)
        if ret != 0:
            raise SystemError("Cannot olddefconfig")

        cmd = ["make", "-C", self.builddir]
        with infra.smart_open(log) as log_fh:
            ret = subprocess.call(cmd, stdout=log_fh, stderr=log_fh)
        if ret != 0:
            raise SystemError("Build failed")

    def delete(self):
        shutil.rmtree(self.builddir)
