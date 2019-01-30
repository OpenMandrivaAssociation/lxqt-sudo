Name:		lxqt-sudo
Version:	0.14.0
Release:	1
Source0:	https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Summary:	Sudo for the LXQt desktop
Url:		http://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt-build-tools)

%description
Execute a command as privileged user in LXQt.

%files -f %{name}.lang
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
%find_lang %{name} --with-qt --all-name
