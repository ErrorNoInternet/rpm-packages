%global commit      38ba3fff242c41a7f648d1fede4cf9a36b2b7e61
%global snapdate    20240807

Name:               quickshell
Version:            0^%{snapdate}
Release:            %autorelease
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/outfoxxed/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      qt6-qtbase-private-devel

%description
Flexible QtQuick based desktop shell toolkit for Wayland and X11.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
export QTWAYLANDSCANNER=%{_libdir}/qt6/libexec/qtwaylandscanner
%cmake  -GNinja \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DGIT_REVISION=%{commit}
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE-GPL
%doc README.md CONTRIBUTING.md
%{_bindir}/quickshell

%changelog
%autochangelog
