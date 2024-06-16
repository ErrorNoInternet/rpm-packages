# Generated by rust2rpm 26
%bcond_without check

%global commit 148bca7982dc19807b14a3c5bb531912120e8210
%global snapdate 20240616

%global crate hsize
%global cargo_install_lib 0

Name:           hsize
Version:        0^%{snapdate}
Release:        %autorelease
Summary:        Convert file sizes to and from human-readable units
License:        LGPL-3-only

URL:            https://github.com/ErrorNoInternet/hsize
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  (crate(clap/default) >= 4.0.0 with crate(clap/default) < 5.0.0~)
BuildRequires:  (crate(clap/derive) >= 4.0.0 with crate(clap/derive) < 5.0.0~)
BuildRequires:  (crate(clap/env) >= 4.0.0 with crate(clap/env) < 5.0.0~)
BuildRequires:  (crate(num-derive/default) >= 0.0.0 with crate(num-derive/default) < 1.0.0~)
BuildRequires:  (crate(num-traits/default) >= 0.0.0 with crate(num-traits/default) < 1.0.0~)
BuildRequires:  (crate(oorandom/default) >= 11.0.0 with crate(oorandom/default) < 12.0.0~)
BuildRequires:  (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0~)

%global _description %{expand:
Convert file sizes to and from human-readable units.}

%description %{_description}

%prep
%autosetup -n %{crate}-%{commit} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/hsize

%changelog
%autochangelog
