################################################################################
#
# polkit
#
################################################################################

POLKIT_VERSION = 0.113
POLKIT_SITE = http://www.freedesktop.org/software/polkit/releases/
POLKIT_LICENSE = GPLv2
POLKIT_LICENSE_FILES = COPYING

POLKIT_INSTALL_STAGING = YES

POLKIT_DEPENDENCIES = expat host-intltool libglib2 spidermonkey

# We could also support --with-authfw=pam
POLKIT_CONF_OPTS = \
	--with-authfw=shadow \
	--with-os-type=unknown \
	--disable-man-pages \
	--disable-examples \
	--with-mozjs=mozjs-24

ifeq ($(BR2_INIT_SYSTEMD),y)
POLKIT_CONF_OPTS += \
	--enable-libsystemd-login=yes \
    --with-systemdsystemunitdir=$(TARGET_DIR)/lib/systemd/system
else
POLKIT_CONF_OPTS += \
	--enable-libsystemd-login=no \
    --without-systemdsystemunitdir
endif

$(eval $(autotools-package))
