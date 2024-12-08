Name:           peaclock
Version:        0.4.3
Release:        %autorelease
Summary:        A responsive clock for the terminal

License:        MIT
URL:            https://github.com/octobanana/peaclock
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  pkgconfig(icu-i18n)

%description
Peaclock is a responsive and customizable clock, timer, and stopwatch
for the terminal.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/peaclock

%changelog
%autochangelog
