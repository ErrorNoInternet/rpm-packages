%global commit 36190eb07dc5d85f408d998d1884eb69573adf68
%global snapdate 20230615

Name: qoi-devel
Version: %{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release: 1%{?dist}
Summary: The "Quite OK Image Format" for fast, lossless image compression

License: MIT
URL: https://github.com/phoboslab/qoi
Source0: %{url}/archive/%{commit}/qoi-%{commit}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Headers for fast, lossless image compression using the "Quite OK Image Format".

%prep
%autosetup -n qoi-%{commit}

%install
mkdir -p %{buildroot}/%{_includedir}
cp qoi.h %{buildroot}/%{_includedir}

%files
%license LICENSE
%doc README.md
%{_includedir}/qoi.h

%changelog
* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb
- Hello, world!
