%bcond_with         asan

%global commit      c57ac4b1f283896bab7fb91e8fdc9249c18d3afe
%global snapdate    20240915

Name:               quickshell
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
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
export QTWAYLANDSCANNER=%{_libdir}/qt6/libexec/qtwaylandscanner
%cmake  -GNinja \
%if %{with asan}
        -DASAN=ON \
%endif
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DGIT_REVISION=%{commit}
%cmake_build

%install
%cmake_install
ln -s quickshell %{buildroot}%{_bindir}/qs
mv %{buildroot}%{_libdir}/qt-6 %{buildroot}%{_libdir}/qt6

%files
%license LICENSE LICENSE-GPL
%doc README.md CONTRIBUTING.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_libdir}/qt6/qml/Quickshell

%changelog
%autochangelog
