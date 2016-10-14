import subprocess
import os
import infra.basetest

class TestRootfsOverlay(infra.basetest.BRTest):
    config = infra.basetest.basic_toolchain_config + infra.basetest.minimal_config + """
BR2_ROOTFS_OVERLAY="%s %s"
""" % (infra.basetest.filePath("tests/infra.rootfs-overlay1"),
       infra.basetest.filePath("tests/infra.rootfs-overlay2"))

    def test_run(self):
        ret = subprocess.call(["cmp",
                               infra.basetest.filePath("tests/infra.rootfs-overlay1/test-file1"),
                               os.path.join(self.builddir, "target", "test-file1")])
        self.assertEqual(ret, 0)
        ret = subprocess.call(["cmp",
                               infra.basetest.filePath("tests/infra.rootfs-overlay2/etc/test-file2"),
                               os.path.join(self.builddir, "target", "etc", "test-file2")])
        self.assertEqual(ret, 0)
