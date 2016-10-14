import infra.basetest
import subprocess
import os

class TestYaffs2(infra.basetest.BRTest):
    config = infra.basetest.basic_toolchain_config + infra.basetest.minimal_config + """
BR2_TARGET_ROOTFS_YAFFS2=y
"""

    def test_run(self):
        self.assertTrue(os.path.exists(os.path.join(
            self.builddir, "images", "rootfs.yaffs2")))
