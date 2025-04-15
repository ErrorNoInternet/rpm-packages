Name:           klassy
Version:        6.2.breeze6.2.1
Release:        2%{?dist}
Summary:        A highly customizable KDE Plasma Window Decoration

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT
URL:            https://github.com/paulmcauley/klassy
Source:         %{url}/archive/%{version}.tar.gz
Patch:          klassy-6.3-update.diff

BuildRequires:  cmake
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext

%description
Klassy is a highly customizable binary Window Decoration and Application Style
plugin for recent versions of the KDE Plasma desktop. It provides the Klassy,
Kite, Oxygen/Breeze, and Redmond icon styles.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_bindir}/klassy-settings
%{_datadir}/applications/kcm_klassydecoration.desktop
%{_datadir}/applications/klassy-settings.desktop
%{_datadir}/applications/klassystyleconfig.desktop
%{_datadir}/color-schemes/Klassy*
%{_datadir}/icons/hicolor/scalable/apps/klassy-settings.svgz
%{_datadir}/icons/klassy*
%{_datadir}/kstyle/themes/klassy.themerc
%{_datadir}/plasma/desktoptheme/klassy
%{_datadir}/plasma/layout-templates/org.kde.klassy*
%{_datadir}/plasma/look-and-feel/org.kde.klassy*
%{_libdir}/cmake/Klassy/KlassyConfig.cmake
%{_libdir}/cmake/Klassy/KlassyConfigVersion.cmake
%{_libdir}/libklassycommon5.so*
%{_libdir}/libklassycommon6.so*
%{_libdir}/qt5/plugins/styles/klassy5.so
%{_libdir}/qt6/plugins/kstyle_config/klassystyleconfig.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/kcm_klassydecoration.so
%{_libdir}/qt6/plugins/org.kde.kdecoration2.kcm/klassydecoration/presets/*.klpw
%{_libdir}/qt6/plugins/org.kde.kdecoration3/org.kde.klassy.so
%{_libdir}/qt6/plugins/styles/klassy6.so

%changelog
%autochangelog
