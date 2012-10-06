%define upname		xf86-video-nouveau
%define snapshot	%nil
%define rel		2

Summary:	Accelerated open source driver for NVIDIA cards
Name:		x11-driver-video-nouveau
Version:	1.0.2
%if "%snapshot" == ""
Release:	%rel
Source0:	http://nouveau.freedesktop.org/release/%{upname}-%{version}.tar.bz2
%else
Release:	0.%snapshot.%rel
# rm -rf xf86-video-nouveau && git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau/ && cd xf86-video-nouveau/
# git archive --prefix=xf86-video-nouveau-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../xf86-video-nouveau-$(date +%Y%m%d).tar.xz
Source0:	%{upname}-%{snapshot}.tar.xz
%endif
Group:		System/X11
License:	MIT
URL:		http://nouveau.freedesktop.org/
BuildRequires:	libdrm-devel >= 2.4.35
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	GL-devel
%if %mdvver >= 201200
BuildRequires:	pkgconfig(udev) >= 186
%else
BuildRequires:	pkgconfig(udev)
%endif
BuildRequires:	libdrm-devel
BuildRequires:	libdrm-common
Conflicts:	xorg-x11-server < 7.0
# No DKMS package for now; nouveau module is in main kernel.
# If needed, DKMS package may be resurrected, but work is needed to make it
# build with the new linux-2.6 tree of nouveau.
Obsoletes:	dkms-nouveau < 0.0.13-0.20090600
Requires:	kmod(nouveau)
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)
# No firmware needed:
Obsoletes:	nouveau-firmware < 20091212-2

%description
The nouveau project aims to build high-quality, open source drivers
for NVIDIA cards.

%prep
%if "%snapshot" != ""
%setup -q -n %{upname}-%{snapshot}
%else
%setup -q -n %upname-%version
%endif
[ -e autogen.sh ] && ./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/nouveau_drv.so
%{_mandir}/man4/nouveau*
