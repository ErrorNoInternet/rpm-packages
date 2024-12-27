%bcond_with         asan

%global commit      08836ca1f3af748d38152e79c544b77dc5e4b3e9
%global snapdate    20241227

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
BuildRequires:      cmake(Qt6ShaderTools)
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
BuildRequires:      spirv-tools

%if %{with asan}
BuildRequires:      libasan
%endif

%description
Flexible toolkit for making desktop shells with QtQuick, targeting
Wayland and X11.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake  -GNinja \
        -DBUILD_SHARED_LIBS=OFF \
        -DDISTRIBUTOR="Fedora COPR (errornointernet/quickshell)" \
        -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml \
%if %{with asan}
        -DASAN=ON \
%endif
        -DCMAKE_BUILD_TYPE=Release \
        -DGIT_REVISION=%{commit}
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE-GPL
%doc BUILD.md CONTRIBUTING.md README.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_libdir}/qt6/qml/Quickshell

%changelog
%autochangelog
