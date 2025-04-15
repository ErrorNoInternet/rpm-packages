# Generated by rust2rpm 27
%bcond check 1

%global cargo_install_lib   0
%global commit              083f15c1b1596d141dec6cc492d6ab5df5eab411
%global snapdate            20250415

Name:           minefetch
Version:        0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:        %autorelease
Summary:        Ping Minecraft servers from your terminal

License:        ((MIT OR Apache-2.0) AND NCSA) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND LGPL-3.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  LGPL-3.0-or-later

URL:            https://github.com/ErrorNoInternet/minefetch
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-%{commit} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/minefetch

%changelog
%autochangelog
