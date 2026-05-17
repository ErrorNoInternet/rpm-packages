%bcond_with         asan

%global commit      7d1c9a9c6721606b129829134d6f614f015621e2
%global commits     818
%global snapdate    20260511
%global tag         0.3.0

Name:               quickshell-git
Version:            %{tag}^%{commits}.git%(c=%{commit}; echo ${c:0:7})
Release:            2%{?dist}
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/quickshell-%{commit}.tar.gz

Conflicts:          quickshell <= %{tag}

BuildRequires:      cmake
BuildRequires:      cmake(cpptrace)
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6CorePrivate)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      cmake(VulkanHeaders)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(libzstd)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(polkit-agent-1)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      spirv-tools

%if %{with asan}
BuildRequires:      libasan
%endif

Provides:           desktop-notification-daemon

%description
Flexible toolkit for making desktop shells with QtQuick, targeting
Wayland and X11.

%prep
%autosetup -n quickshell-%{commit} -p1

%build
%cmake  -GNinja \
%if %{with asan}
        -DASAN=ON \
%endif
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DDISTRIBUTOR="Fedora COPR (errornointernet/quickshell)" \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml \
        %{?commit:-DGIT_REVISION=%{commit}}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%license LICENSE-GPL
%doc BUILD.md
%doc CONTRIBUTING.md
%doc README.md
%doc changelog/v%{tag}.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg
%{_libdir}/qt6/qml/Quickshell

%changelog
%autochangelog
