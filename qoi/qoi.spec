%global commit 41e8f84bf68f7bb658430a37b5647c172d86e38e
%global snapdate 20230828

Name: qoi
Version: %{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release: 1%{?dist}
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
Requires: %{name}%{?isa} = %{version}-%{release}

%description tools
Tools for fast, lossless image compression using the "Quite OK Image Format".

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}
BuildArch: noarch

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

%files

%files tools
%license LICENSE
%doc README.md
%{_bindir}/qoibench
%{_bindir}/qoiconv

%files devel
%{_includedir}/qoi.h

%changelog
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
