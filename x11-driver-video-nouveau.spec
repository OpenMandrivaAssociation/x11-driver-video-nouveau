%define name		x11-driver-video-nouveau
%define upname		xf86-video-nouveau
%define version		0
%define snapshot	20090530
%define rel		1

%define release %mkrel 0.%{snapshot}.%{rel}

Summary:	The experimental X.org driver for NVIDIA cards
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/X11
License:	MIT
URL:		http://nouveau.freedesktop.org/
# rm -rf xf86-video-nouveau && git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau/ && cd xf86-video-nouveau/
# git archive --prefix=xf86-video-nouveau-$(date +%Y%m%d)/ --format=tar HEAD | bzip2 > ../xf86-video-nouveau-$(date +%Y%m%d).tar.bz2
Source0:	%{upname}-%{snapshot}.tar.bz2
BuildRequires:	libdrm-devel >= 2.4.5
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	GL-devel
Conflicts:	xorg-x11-server < 7.0
Requires:	kmod(nouveau)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
x11-driver-video-nouveau is the experimental X.org driver for NVIDIA cards.

The nouveau kernel module is also required, available in package
dkms-drm-experimental.

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
