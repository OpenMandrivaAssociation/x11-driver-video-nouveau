%define name		x11-driver-video-nouveau
%define upname		xf86-video-nouveau
%define version		0.0.15
%define snapshot	20100206
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
BuildRequires:	libdrm-devel >= 2.4.17-4
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	GL-devel
Conflicts:	xorg-x11-server < 7.0
# No DKMS package for now; nouveau module is in main kernel.
# If needed, DKMS package may be resurrected, but work is needed to make it
# build with the new linux-2.6 tree of nouveau.
Obsoletes:	dkms-nouveau < 0.0.13-0.20090600
Requires:	kmod(nouveau)
Requires:	nouveau-firmware
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The nouveau project aims to build high-quality, open source drivers
for NVIDIA cards.

%prep
%setup -q -n %{upname}-%{snapshot}

%build
autoreconf -v --install
%configure2_5x 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/nouveau_drv.la
%{_libdir}/xorg/modules/drivers/nouveau_drv.so
%{_mandir}/man4/nouveau*
