Name: par2cmdline-turbo
Version: 1.0.1
Release: 1%{?dist}
Summary: par2cmdline × ParPar: speed focused par2cmdline fork

License: GPL-2.0
URL: https://github.com/animetosho/par2cmdline-turbo
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: automake gcc-c++

%description
This is a *simple* fork of par2cmdline which replaces core computation routines with ParPar’s processing backend, improving par2cmdline’s performance on x86/ARM platforms.

%prep
%autosetup -n %{name}-%{version}

%build
./automake.sh
%configure
%make_build

%install
%make_install

%files
/usr/bin/par2
/usr/bin/par2create
/usr/bin/par2repair
/usr/bin/par2verify
/usr/share/man/man1/par2.1.gz

%changelog
* Wed May 24 2023 ErrorNoInternet <errornointernet@envs.net> - 1.0.0-1
- Hello, world!
