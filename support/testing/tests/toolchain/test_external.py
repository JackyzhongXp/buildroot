import os

import infra

class TestExternalToolchainSourceryArmv4(infra.basetest.BRTest):
    config = \
"""
BR2_arm=y
BR2_arm920t=y
BR2_TOOLCHAIN_EXTERNAL=y
BR2_TOOLCHAIN_EXTERNAL_CODESOURCERY_ARM=y
BR2_TARGET_ROOTFS_CPIO=y
# BR2_TARGET_ROOTFS_TAR is not set
"""

    def test_run(self):
        arch = infra.get_file_arch(self.builddir,
                                   "arm-none-linux-gnueabi", "lib/libc.so.6")
        self.assertEqual(arch, "v4T")
        img = os.path.join(self.builddir, "images", "rootfs.cpio")
        self.emulator.boot(arch="armv5",
                           kernel="builtin",
                           options=["-initrd", img])
        self.emulator.login("root")
