Name:		lxqt-sudo
Version:	2.2.0
Release:	1
Source0:	https://github.com/lxqt/lxqt-sudo/releases/download/%{version}/lxqt-sudo-%{version}.tar.xz
Summary:	Sudo for the LXQt desktop
Url:		https://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt2-build-tools)

%description
Execute a command as privileged user in LXQt.

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*man?/*
%dir %{_datadir}/lxqt/translations/lxqt-sudo

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name
