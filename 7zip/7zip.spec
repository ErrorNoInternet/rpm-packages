%global debug_package %{nil}

Name:           7zip
Version:        24.05
Release:        1%{?dist}
Summary:        A file archiver with a high compression ratio

License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://7-zip.org
Source0:        %{url}/a/7z%(v='%{version}'; echo "${v//.}")-src.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
This package provides the official 7-Zip console version for Linux

%prep
tar xf %{SOURCE0}

%build
cd CPP/7zip/Bundles/Alone2
%make_build -f ../../cmpl_gcc.mak DISABLE_RAR_COMPRESS=1

%install
install -d %{buildroot}%{_bindir}
install -p CPP/7zip/Bundles/Alone2/b/g/7zz %{buildroot}%{_bindir}

%files
%doc DOC/readme.txt
%license DOC/copying.txt DOC/License.txt
%{_bindir}/7zz

%changelog
* Sun May 26 2024 ErrorNoInternet <errornointernet@envs.net> - 24.05-1
- Bump version.
- Clean a few things up.

* Mon Jul 17 2023 ErrorNoInternet <errornointernet@envs.net> - 23.01-1
- Initial packaging.
