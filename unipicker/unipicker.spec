%global debug_package %{nil}

%global commit      dc43edd5161027a6af269c5a457e62755545e510
%global snapdate    20240102

Name:               unipicker
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            4%{dist}
Summary:            Search unicode characters in console and copy to clipboard

License:            MIT
URL:                https://github.com/jeremija/unipicker
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch:              unipicker-rofi.diff

BuildRequires:      make
BuildRequires:      python3
BuildRequires:      python3-gobject-base

Recommends:         fzf

%description
A CLI utility for searching unicode characters by description and
optionally copying them to clipboard.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/unipickerrc
%{_bindir}/unipicker
%{_datadir}/unipicker/symbols*

%changelog
%autochangelog
