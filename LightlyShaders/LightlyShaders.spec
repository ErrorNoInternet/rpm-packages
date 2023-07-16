Name: LightlyShaders
Version: master
Release: 1%{?dist}
Summary: Round corners and outline effect for KWin

License: GPL-3.0-or-later
URL: https://github.com/a-parhom/LightlyShaders
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qttools-static
BuildRequires: qt5-qtx11extras-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kwin-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libepoxy-devel
BuildRequires: kdecoration-devel

%description
This is a fork of Luwx's LightlyShaders, which in turn is a fork of ShapeCorner.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/%{_datadir}/kwin
mv %{buildroot}/kwin/shaders %{buildroot}/%{_datadir}/kwin
mkdir -p %{buildroot}/%{_prefix}/%{_lib}/qt5/plugins/kwin/effects/plugins
mv %{buildroot}/kwin/effects/plugins/kwin4_effect_lightlyshaders.so %{buildroot}/%{_prefix}/%{_lib}/qt5/plugins/kwin/effects/plugins

%files
%doc README.md
%{_datadir}/kwin/shaders/1.10/lightlyshaders.frag
%{_datadir}/kwin/shaders/1.40/lightlyshaders.frag
%{_prefix}/%{_lib}/qt5/plugins/kwin/effects/plugins/kwin4_effect_lightlyshaders.so
%{_prefix}/%{_lib}/qt5/plugins/kwin/effects/configs/kwin4_lightlyshaders_config.so

%changelog
* Sat Jul 08 2023 ErrorNoInternet <errornointernet@envs.net> - master
- Hello, world!
