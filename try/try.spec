%global debug_package %{nil}

Name: try
Version: 0.1.0
Release: 1%{?dist}
Summary: Inspect a command's effects before modifying your live system

License: MIT
URL: https://github.com/binpash/try
Source0: %{url}/archive/v%{version}.tar.gz

Requires: util-linux mergerfs

%description
`try` lets you run a command and inspect its effects before changing your live system. `try` uses Linux's namespaces (via `unshare`) and the overlayfs union filesystem.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
cp try %{buildroot}%{_bindir}

%files
/usr/bin/try

%changelog
* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net>
- Hello, world!
