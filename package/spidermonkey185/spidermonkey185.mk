################################################################################
#
# Spidermonkey (1.8.5)
#
################################################################################

SPIDERMONKEY185_VERSION = 1.0.0
SPIDERMONKEY185_SITE = http://ftp.mozilla.org/pub/js
SPIDERMONKEY185_SOURCE = js185-${SPIDERMONKEY185_VERSION}.tar.gz

SPIDERMONKEY185_INSTALL_STAGING = YES

SPIDERMONKEY185_DEPENDENCIES = host-python host-perl

SPIDERMONKEY185_LICENSE = MPLv1.1 or GPLv2.0+ or LGPLv2.1+

SPIDERMONKEY185_SUBDIR = js/src

# This define is used by jscpucfg.cpp which is normally used to runtime-detect
# the system endianess.
SPIDERMONKEY185_CONF_ENV = \
	HOST_CXXFLAGS="$(HOST_CXXFLAGS) -DFORCE_$(BR2_ENDIAN)_ENDIAN"

# Mozilla mixes up target, host and build.  See the comment in configure.in
# around line 360.  Also, nanojit fails to build on sparc64 with
# #error "unknown nanojit architecture", so disable the JIT.
SPIDERMONKEY185_CONF_OPTS = \
		--target=$(GNU_TARGET_NAME) \
		--build=$(GNU_TARGET_NAME) \
		--host=$(GNU_HOST_NAME) \
		$(if $(BR2_sparc64),--disable-tracejit)

$(eval $(autotools-package))
