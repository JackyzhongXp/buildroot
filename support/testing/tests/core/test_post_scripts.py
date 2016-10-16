import os

import infra.basetest

class TestPostScripts(infra.basetest.BRTest):
    config = infra.basetest.BASIC_TOOLCHAIN_CONFIG + \
"""
BR2_INIT_NONE=y
BR2_SYSTEM_BIN_SH_NONE=y
# BR2_PACKAGE_BUSYBOX is not set
BR2_ROOTFS_POST_BUILD_SCRIPT="{}"
BR2_ROOTFS_POST_IMAGE_SCRIPT="{}"
BR2_ROOTFS_POST_SCRIPT_ARGS="foobar baz"
""".format(infra.filepath("tests/infra.post-build.sh"),
           infra.filepath("tests/infra.post-image.sh"))

    # TODO
    def check_post_log_file(self, path):
        pass
    #     f = open(path, "r")
    #     lines = f.readlines()

    def test_run(self):
        self.check_post_log_file(os.path.join(self.builddir, "build", "post-build.log"))
        self.check_post_log_file(os.path.join(self.builddir, "build", "post-image.log"))
