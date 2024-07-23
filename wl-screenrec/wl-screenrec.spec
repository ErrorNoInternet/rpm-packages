# prevent library files from being installed
%global cargo_install_lib 0

Name:           wl-screenrec
Version:        0.1.4
Release:        %autorelease
Summary:        High performance screen/audio recorder for wlroots

SourceLicense:  Apache-2.0
License:        # FIXME

URL:            https://github.com/russelltg/wl-screenrec
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  vulkan-loader

%global _description %{expand:
High performance screen/audio recorder for wlroots.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/wl-screenrec

%changelog
%autochangelog
