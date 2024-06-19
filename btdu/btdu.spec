%global debug_package %{nil}

Name:           btdu
Version:        0.5.1
Release:        1%{?dist}
Summary:        Sampling disk usage profiler for btrfs
License:        GPL-2.0-only
URL:            https://github.com/CyberShadow/btdu

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  dub
BuildRequires:  gcc
BuildRequires:  ldc
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel

%description
A sampling disk usage profiler for btrfs.

%prep
%autosetup -p1

%build
dub build -b release

%install
install -Dpm755 btdu %{buildroot}%{_bindir}/btdu

%files
%{_bindir}/btdu

%changelog
* Fri May 31 2024 ErrorNoInternet <errornointernet@envs.net> - 0.5.1-1
- Initial packaging.
