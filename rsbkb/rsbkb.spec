# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

Name:           rsbkb
Version:        1.5.1
Release:        %autorelease
Summary:        CLI tools to encode/decode things

# 0BSD OR MIT OR Apache-2.0
# GPL-3.0-or-later
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        (0BSD OR MIT OR Apache-2.0) AND GPL-3.0-or-later AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
SourceLicense:  GPL-3.0-or-later

URL:            https://github.com/trou/rsbkb
Source:         %{url}/archive/release-%{version}/%{name}-release-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-release-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

for applet in $(%{buildroot}%{_bindir}/rsbkb list); do
    ln -s rsbkb %{buildroot}%{_bindir}/$applet
done

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%doc README.md Changelog.md
%{_bindir}/*

%changelog
%autochangelog