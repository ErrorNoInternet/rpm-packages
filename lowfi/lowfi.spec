# Generated by rust2rpm 27
%bcond check 1

# prevent library files from being installed
%global cargo_install_lib   0

Name:           lowfi
Version:        1.6.4~dev
Release:        %autorelease
Summary:        Extremely simple lofi player

SourceLicense:  MIT
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND ISC AND (BSD-2-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND MIT AND (Apache-2.0 OR BSL-1.0) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR Zlib) AND Apache-2.0 AND (Unlicense OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND MPL-2.0 AND (0BSD OR MIT OR Apache-2.0)

URL:            https://github.com/talwat/lowfi
Source:         %{url}/archive/%(v=%{version}; echo ${v//\~/-})/%{name}-%(v=%{version}; echo ${v//\~/-}).tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
An extremely simple lofi player.}

%description %{_description}

%prep
%autosetup -n %{name}-%(v=%{version}; echo ${v//\~/-}) -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%files
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%doc README.md
%{_bindir}/lowfi

%changelog
%autochangelog
