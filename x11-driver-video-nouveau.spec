%define name		x11-driver-video-nouveau
%define upname		xf86-video-nouveau
%define version		1.0.0
%define snapshot	20120619
%define rel		1

%define release %mkrel 0.%{snapshot}.%{rel}

Summary:	Accelerated open source driver for NVIDIA cards
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/X11
License:	MIT
URL:		http://nouveau.freedesktop.org/
# rm -rf xf86-video-nouveau && git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau/ && cd xf86-video-nouveau/
# git archive --prefix=xf86-video-nouveau-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../xf86-video-nouveau-$(date +%Y%m%d).tar.xz
Source0:	%{upname}-%{snapshot}.tar.xz
BuildRequires:	libdrm-devel >= 2.4.24-3
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	GL-devel
BuildRequires:	udev-devel
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
#xf86-video-nouveau-0.0.16_pre20120322/
%setup -q -n %{upname}-%{snapshot}
#grep -q %{version} configure.ac

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/nouveau_drv.so
%{_mandir}/man4/nouveau*
