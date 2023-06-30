%global debug_package %{nil}

Name: try
Version: 0.1.0
Release: 1%{?dist}
Summary: Inspect a command's effects before modifying your live system

License: MIT
URL: https://github.com/binpash/try
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: make pandoc
Requires: util-linux mergerfs

%description
`try` lets you run a command and inspect its effects before changing your live system. `try` uses Linux's namespaces (via `unshare`) and the overlayfs union filesystem.

%prep
%autosetup -n %{name}-%{version}

%build
cd man
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp try %{buildroot}%{_bindir}
cp man/try.1 %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%doc README.md
/usr/bin/try
/usr/share/man/man1/try.1.gz

%changelog
* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 0.1.0-1
- Hello, world!
