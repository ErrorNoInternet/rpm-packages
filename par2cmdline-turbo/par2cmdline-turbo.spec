Name:           par2cmdline-turbo
Version:        1.1.1
Release:        %autorelease
Summary:        Speed focused par2cmdline fork

License:        GPL-2.0-or-later
URL:            https://github.com/animetosho/par2cmdline-turbo
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Obsoletes:      par2cmdline <= 0.8.1
Provides:       par2cmdline

BuildRequires:  automake
BuildRequires:  gcc-c++

%description
A *simple* fork of par2cmdline which replaces core computation
routines with ParPar’s processing backend, improving par2cmdline’s
performance on x86/ARM platforms.

%prep
%autosetup -p1

%build
export CFLAGS="$CFLAGS -Wno-error=implicit-function-declaration"
./automake.sh
%configure
%make_build

%install
%make_install

%check
%make_build check-TESTS

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*

%changelog
%autochangelog
