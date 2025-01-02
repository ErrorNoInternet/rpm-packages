%global debug_package %{nil}

Name:           btdu
Version:        0.6.0
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
export DFLAGS="%{_d_optflags}"
dub build

%install
install -Dpm755 btdu %{buildroot}%{_bindir}/btdu
install -Dpm644 btdu.1 %{buildroot}%{_mandir}/man1/btdu.1

%files
%{_bindir}/btdu
%{_mandir}/man1/btdu.1*

%changelog
%autochangelog
