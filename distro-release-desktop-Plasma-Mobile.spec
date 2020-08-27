# This should really be a subpackage of distro-release,
# but at this time, rpm has no way to package different
# conflicting files with the same name in different subpackages.
#
# Plasma and Plasma Mobile can't share the same default
# /etc/xdg/kwinrc and friends.
#
# But let's at least use the same source tarball.

Summary:	Plasma Mobile desktop configuration
Name:		distro-release-desktop-Plasma-Mobile
Version:	4.2
Release:	0.1
URL:		https://github.com/OpenMandrivaSoftware/distro-release
Source0:	https://github.com/OpenMandrivaSoftware/distro-release/archive/%{version}/distro-release-%{version}.tar.gz
BuildArch:	noarch
Group:		Graphical Desktop/KDE
Requires:	task-plasma-mobile-minimal
Requires:	noto-sans-fonts
License:	GPLv3

%description
Plasma Mobile desktop configuration

%prep
%autosetup -p1 -n distro-release-%{version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/xdg
cp -a desktops/Plasma-Mobile/* %{buildroot}%{_sysconfdir}/xdg/

%files
%{_sysconfdir}/xdg/*
