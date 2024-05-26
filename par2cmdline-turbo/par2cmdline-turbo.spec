Name: par2cmdline-turbo
Version: 1.1.1
Release: 2%{?dist}
Summary: ParPar x par2cmdline: speed focused par2cmdline fork

License: GPL-2.0-or-later
URL: https://github.com/animetosho/par2cmdline-turbo
Source0: %{url}/archive/v%{version}.tar.gz

Obsoletes: par2cmdline <= 0.8.1
Provides: par2cmdline
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
%make_build -Wno-error=implicit-function-declaration

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
* Sun May 26 2024 ErrorNoInternet <errornointernet@envs.net> - 1.1.1-2
- Clean up a few things.
- Fix aarch64 build by adding -Wno-error=implicit-function-declaration for posix_memalign.

* Thu Aug 31 2023 ErrorNoInternet <errornointernet@envs.net> - 1.1.0-2
- Fixed a few package review issues

* Wed Aug 09 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.1-4
- Cleaned some stuff up

* Sun Jul 23 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.1-3
- Conflicts with par2cmdline

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.1-2
- Add COPYING and README.md

* Wed May 24 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.0-1
- Hello, world!
