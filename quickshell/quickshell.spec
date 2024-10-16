%bcond_with         asan

%global commit      623e0471d56ce8a0a6186b9fe2e45815f1d910ac
%global snapdate    20241017

Name:               quickshell
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            %autorelease
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(breakpad)
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      qt6-qtbase-private-devel

%if %{with asan}
BuildRequires:      libasan
%endif

%description
Flexible QtQuick based desktop shell toolkit for Wayland and X11.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake  -GNinja \
        -DBUILD_SHARED_LIBS=OFF \
        -DDISTRIBUTOR="Fedora COPR (errornointernet/quickshell)" \
        -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
%if %{with asan}
        -DASAN=ON \
%endif
        -DCMAKE_BUILD_TYPE=Release \
        -DGIT_REVISION=%{commit}
%cmake_build

%install
%cmake_install
ln -s quickshell %{buildroot}%{_bindir}/qs
mv %{buildroot}%{_libdir}/qt-6 %{buildroot}%{_libdir}/qt6

%files
%license LICENSE LICENSE-GPL
%doc BUILD.md CONTRIBUTING.md README.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_libdir}/qt6/qml/Quickshell

%changelog
%autochangelog
