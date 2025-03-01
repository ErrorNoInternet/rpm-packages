%global commit      1fd1a3fdf9cb0b6d43c89926f760d4e84d8f31d5
%global snapdate    20240704

Name:               kwin-effects-sliding-notifications
Version:            1.5.0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            %autorelease
Summary:            Sliding animation for notification windows

License:            GPL-3.0-or-later AND MIT
URL:                https://github.com/zzag/kwin-effects-sliding-notifications
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      cmake
BuildRequires:      cmake(KF6Config)
BuildRequires:      cmake(KF6ConfigWidgets)
BuildRequires:      cmake(KF6CoreAddons)
BuildRequires:      cmake(KF6WindowSystem)
BuildRequires:      cmake(KWin)
BuildRequires:      cmake(Qt6)
BuildRequires:      extra-cmake-modules
BuildRequires:      pkgconfig(epoxy)
BuildRequires:      pkgconfig(wayland-server)

%description
This is a simple effect that makes notification windows slide in and
out when they are shown or hidden.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%doc README.md
%{_libdir}/qt6/plugins/kwin/effects/plugins/slidingnotifications.so

%changelog
%autochangelog
