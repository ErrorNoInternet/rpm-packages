Name: kwin-effects-sliding-notifications
Version: 1.5.0
Release: 3%{?dist}
Summary: Sliding animation for notification windows

License: GPL-3.0-or-later
URL: https://github.com/zzag/kwin-effects-sliding-notifications
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: cmake extra-cmake-modules kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kwindowsystem-devel kwin-devel libepoxy-devel qt5-qtbase-devel

%description
This is a simple effect that makes notification windows slide in and out when they are shown or hidden.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
%make_build

%install
cd build
%make_install

%files
%doc README.md
%{_prefix}/%{_lib}/qt5/plugins/kwin/effects/plugins/kwin4_effect_slidingnotifications.so

%changelog
* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.5.0-3
- Add README.md

* Fri Apr 21 2023 ErrorNoInternet <errornointernet@envs.net> - 1.5.0-1
- Hello, world!
