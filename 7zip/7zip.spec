%global debug_package %{nil}

Name:           7zip
Version:        24.08
Release:        1%{?dist}
Summary:        The official 7-Zip console version for Linux

License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://7-zip.org
Source0:        %{url}/a/7z%(v='%{version}'; echo "${v//.}")-src.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
A file archiver with a high compression ratio.

%prep
tar xf %{SOURCE0}

%build
cd CPP/7zip/Bundles/Alone2
%make_build -f ../../cmpl_gcc.mak DISABLE_RAR_COMPRESS=1

%install
install -Dp CPP/7zip/Bundles/Alone2/b/g/7zz %{buildroot}%{_bindir}/7zz

%files
%license DOC/copying.txt DOC/License.txt
%doc DOC/readme.txt
%{_bindir}/7zz

%changelog
%autochangelog
