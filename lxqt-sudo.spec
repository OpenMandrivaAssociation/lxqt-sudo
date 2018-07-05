Name:		lxqt-sudo
Version:	0.13.0
Release:	1
Source0:	https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Summary:	Sudo for the LXQt desktop
Url:		http://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake ninja
BuildRequires:	qmake5
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	lxqt-build-tools git-core

%description
Execute a command as privileged user in LXQt.

%files
%{_bindir}/*
%{_mandir}/*man?/*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_qt5 \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
