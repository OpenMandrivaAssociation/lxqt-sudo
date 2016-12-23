Name:		lxqt-sudo
Version:	0.11.0
Release:	1
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary:	Sudo for the LXQt desktop
Url:		http://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)

%description
Execute a command as privileged user in LXQt.

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*man?/*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%find_lang %{name} %{name}.lang --with-qt
