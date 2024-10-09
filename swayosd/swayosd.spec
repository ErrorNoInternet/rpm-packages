%global alt_pkg_name swayosd

Name:           SwayOSD
Version:        0.1.0
Release:        %autorelease
Summary:        GTK based on screen display
License:        GPL-3.0-or-later

URL:            https://github.com/ErikReider/SwayOSD
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  meson
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pulseaudio-libs
BuildRequires:  sassc

%description
A OSD window for common actions like volume and capslock.

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%meson_install
rm %{_datadir}/licenses/swayosd

%files
%doc README.md
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%{_bindir}/swayosd-client
%{_bindir}/swayosd-libinput-backend
%{_bindir}/swayosd-server
%{_datadir}/dbus-1/system-services/org.erikreider.swayosd.service
%{_datadir}/dbus-1/system.d/org.erikreider.swayosd.conf
%{_datadir}/polkit-1/actions/org.erikreider.swayosd.*
%{_datadir}/polkit-1/rules.d/org.erikreider.swayosd.rules
%{_libdir}/systemd/system/swayosd-libinput-backend.service
%{_libdir}/udev/rules.d/99-swayosd.rules
%{_sysconfdir}/xdg/swayosd/style.css

%changelog
%autochangelog
