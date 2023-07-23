Name: par2cmdline-turbo
Version: 1.0.1
Release: 3%{?dist}
Summary: par2cmdline × ParPar: speed focused par2cmdline fork

License: GPL-2.0
URL: https://github.com/animetosho/par2cmdline-turbo
Source0: %{url}/archive/v%{version}.tar.gz

Conflicts: par2cmdline
BuildRequires: automake gcc-c++

%description
This is a *simple* fork of par2cmdline which replaces core computation
routines with ParPar’s processing backend, improving par2cmdline’s
performance on x86/ARM platforms.

%prep
%autosetup -n %{name}-%{version}

%build
./automake.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_mandir}/man1/par2.1.gz
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify

%changelog
* Sun Jul 23 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.1-3
- Conflicts with par2cmdline

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.1-2
- Add COPYING and README.md

* Wed May 24 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.0-1
- Hello, world!
