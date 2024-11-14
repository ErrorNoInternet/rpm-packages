Name:           wl-restart
Version:        0.3.0
Release:        %autorelease
Summary:        Restart your compositor when it crashes

# src/wl-socket.{c,h} are GPL-2.0-or-later.
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/Ferdi265/wl-restart
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  scdoc

%description
A simple tool that restarts your compositor when it crashes. It also
creates and destroys the Wayland socket for the compositor, so that
clients that support seamless compositor reconnects (most KDE programs,
e.g. Konsole) don't die with it when your compositor crashes.

%prep
%autosetup -p1

%build
%cmake -DINSTALL_DOCUMENTATION=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wl-restart
%{_mandir}/man1/wl-restart.1*

%changelog
%autochangelog
