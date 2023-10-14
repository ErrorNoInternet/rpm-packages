%global commit 8d35d93cdca85d2868246c2a8a80a1e2c16ba2a8
%global snapdate 20230911

Name: qoi
Version: 0^%{snapdate}
Release: 2%{?dist}
Summary: The "Quite OK Image Format" for fast, lossless image compression

License: MIT
URL: https://github.com/phoboslab/qoi
Source0: %{url}/archive/%{commit}/qoi-%{commit}.tar.gz
Patch0: Makefile-ldflags.patch

BuildRequires: gcc
BuildRequires: libpng-devel
BuildRequires: stb_image-devel
BuildRequires: stb_image_write-devel
BuildRequires: make

%description
The "Quite OK Image Format" for fast, lossless image compression.

%package tools
Summary: Tools for %{name}

%description tools
Tools for fast, lossless image compression using the "Quite OK Image Format".

%package devel
Summary: Development files for %{name}
BuildArch: noarch
Provides: qoi-static = %{version}-%{release}

%description devel
Headers for fast, lossless image compression using the "Quite OK Image Format".

%prep
%autosetup -n qoi-%{commit} -p1

%build
%make_build bench conv

%install
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_includedir}
install -p qoibench qoiconv %{buildroot}/%{_bindir}
install -p qoi.h %{buildroot}/%{_includedir}

%files tools
%license LICENSE
%doc README.md
%{_bindir}/qoibench
%{_bindir}/qoiconv

%files devel
%license LICENSE
%{_includedir}/qoi.h

%changelog
* Sat Oct 14 2023 ErrorNoInternet <errornointernet@envs.net> - 0^20230911-2
- Add `Provides: qoi-static` to the -devel package

* Tue Oct 10 2023 ErrorNoInternet <errornointernet@envs.net> - 0^20230911-1
- Use caret versioning
- Remove `Requires` from the -devel and -tools package
- Add LICENSE to -devel package

* Thu Aug 31 2023 ErrorNoInternet <errornointernet@envs.net> - 20230828git41e8f84-1
- Bump package version
- Split package into -tools and -devel

* Sun Jul 16 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-3
- Add Makefile-ldflags patch (now includes Fedora's LDFLAGS)
- devel package now requires base package

* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-2
- Merge qoi-devel into qoi

* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-1
- Hello, world!
