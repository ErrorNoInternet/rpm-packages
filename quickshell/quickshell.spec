%global commit      9e58077c61fce106d613abbfe47e659185e38bf8
%global snapdate    20240619

Name:               quickshell
Version:            0^%{snapdate}
Release:            1%{?dist}
Summary:            Simple and flexbile QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/outfoxxed/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pipewire-devel
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      qt6-qtbase-private-devel

%description
Simple and flexbile QtQuick based desktop shell toolkit for Wayland and X11.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
export QTWAYLANDSCANNER=%{_libdir}/qt6/libexec/qtwaylandscanner
%cmake -GNinja -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE-GPL
%doc README.md
%{_bindir}/quickshell

%changelog
* Mon Jun 03 2024 ErrorNoInternet <errornointernet@envs.net> - 0^20240603-1
- Initial packaging
