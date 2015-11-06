################################################################################
#
# leaktracer
#
################################################################################

LEAKTRACER_VERSION = b1b6c44762669de4fa6b48a02a813bfd3eb53a23
LEAKTRACER_SITE = $(call github,fredericgermain,leaktracer,$(LEAKTRACER_VERSION))
LEAKTRACER_LICENSE = LGPLv2.1+ (Library) GPLv2+ (manual and tools)
LEAKTRACER_LICENSE_FILES = COPYING COPYING.LIB
LEAKTRACER_INSTALL_STAGING = YES

define LEAKTRACER_BUILD_CMDS
	$(MAKE) CROSS_COMPILE="$(TARGET_CROSS)" OBJDIR="$(@D)/build" -C $(@D)
endef

define LEAKTRACER_INSTALL_STAGING_CMDS
	$(MAKE) -C $(@D) install \
		DESTDIR="$(STAGING_DIR)" PREFIX=/usr OBJDIR="$(@D)/build"
endef

define LEAKTRACER_INSTALL_TARGET_CMDS
	$(MAKE) -C $(@D) install \
		DESTDIR="$(TARGET_DIR)" PREFIX=/usr OBJDIR="$(@D)/build"
endef

$(eval $(generic-package))
