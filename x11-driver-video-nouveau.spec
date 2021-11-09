%define upname xf86-video-nouveau
%define snapshot %{nil}

%define _disable_ld_no_undefined 1

Summary:	Accelerated open source driver for NVIDIA cards
Name:		x11-driver-video-nouveau
Version:	1.0.17
%if "%snapshot" == ""
Release:	3
Source0:	http://xorg.freedesktop.org/archive/individual/driver/%{upname}-%{version}.tar.bz2
%else
Release:	1.%snapshot.1
# rm -rf xf86-video-nouveau && git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau/ && cd xf86-video-nouveau/
# git archive --prefix=xf86-video-nouveau-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../xf86-video-nouveau-$(date +%Y%m%d).tar.xz
Source0:	%{upname}-%{snapshot}.tar.xz
%endif
Group:		System/X11
License:	MIT
URL:		http://nouveau.freedesktop.org/
Patch1:		0001-nouveau-fixup-driver-for-new-X-server-ABI.patch
Patch2:		0002-remove-sarea.h-usage.patch

BuildRequires:	pkgconfig(libdrm) >= 2.4.35
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.19
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(udev) >= 186
BuildRequires:	libdrm-common
Requires:	udev
Conflicts:	xorg-x11-server < 7.0
# No DKMS package for now; nouveau module is in main kernel.
# If needed, DKMS package may be resurrected, but work is needed to make it
# build with the new linux-2.6 tree of nouveau.
Obsoletes:	dkms-nouveau < 0.0.13-0.20090600
Requires:	kmod(nouveau)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
# No firmware needed:
Obsoletes:	nouveau-firmware < 20091212-2
# (tpg) these are needed to get vdpau works out of box
Requires:	%{_lib}dri-drivers-nouveau
Requires:	%{_lib}vdpau-driver-nouveau

%description
The nouveau project aims to build high-quality, open source drivers
for NVIDIA cards.

%prep
%if "%snapshot" != ""
%setup -q -n %{upname}-%{snapshot}
%else
%setup -q -n %upname-%version
%endif
%autopatch -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/nouveau_drv.so
%doc %{_mandir}/man4/nouveau*
