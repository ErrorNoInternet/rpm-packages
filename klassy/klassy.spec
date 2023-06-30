Name: klassy
Version: 4.3.breeze5.27.5
Release: 2%{?dist}
Summary: A highly customizable KDE Plasma Window Decoration

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT
URL: https://github.com/paulmcauley/klassy
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: cmake extra-cmake-modules cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5DBus) cmake(Qt5X11Extras) cmake(KF5GuiAddons) cmake(KF5WindowSystem) cmake(KF5I18n) cmake(KDecoration2) cmake(KF5CoreAddons) cmake(KF5ConfigWidgets) cmake(KF5IconThemes) cmake(KF5Package) cmake(Qt5Quick) cmake(KF5FrameworkIntegration) cmake(KF5KCMUtils) cmake(KF5Kirigami2)

%description
Klassy is a highly customizable binary Window Decoration and Application Style plugin for recent versions of the KDE Plasma desktop. It provides the Klassy, Kite, Oxygen/Breeze, and Redmond icon styles.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%make_build

%install
cd build
%make_install

%files
%doc README.md
/usr/bin/klassy-settings
/usr/lib64/cmake/Klassy/KlassyConfig.cmake
/usr/lib64/cmake/Klassy/KlassyConfigVersion.cmake
/usr/lib64/libklassycommon5.so.%{version}
/usr/lib64/libklassycommon5.so.5
/usr/lib64/qt5/plugins/org.kde.kdecoration2/klassydecoration.so
/usr/lib64/qt5/plugins/styles/klassy.so
/usr/lib64/qt5/plugins/plasma/kcms/klassy/kcm_klassydecoration.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/klassystyleconfig.so
/usr/share/applications/kcm_klassydecoration.desktop
/usr/share/applications/klassystyleconfig.desktop
/usr/share/icons/hicolor/scalable/apps/klassy-settings.svgz
/usr/share/kstyle/themes/klassy.themerc

%changelog
* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 4.3.breeze5.27.5-2
- Add README.md

* Sat May 06 2023 ErrorNoInternet <errornointernet@envs.net> - 4.1.breeze5.25.80-1
- Hello, world!
