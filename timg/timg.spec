Name: timg
Version: 1.6.0
Release: 2%{?dist}
Summary: A terminal image and video viewer

License: GPL-2.0-only
# The following are under different terms, but are unused and removed in %prep.
#
# - third_party/qoi is MIT
# - third_party/stb is MIT OR Unlicense

URL: https://github.com/hzeller/timg
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cairo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: GraphicsMagick-c++-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libdeflate-devel
BuildRequires: libexif-devel
BuildRequires: librsvg2-devel
BuildRequires: libsixel-devel
BuildRequires: libswscale-free-devel
BuildRequires: openslide-devel
BuildRequires: pandoc
BuildRequires: pkg-config
BuildRequires: poppler-glib-devel
BuildRequires: qoi-devel
BuildRequires: stb_image-devel
BuildRequires: stb_image_resize-devel
BuildRequires: turbojpeg-devel

%description
A user-friendly terminal image viewer that uses graphic capabilities of
terminals (Sixel, Kitty or iTerm2), or 24-bit color capabilities and Unicode
character blocks if these are not available. On terminals that implement the
Sixel protocol, the Kitty Graphics Protocol, or the iTerm2 Graphics Protocol,
this displays images in full resolution.

%prep
%autosetup -n %{name}-%{version}
rm -rf third_party

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/timg
%{_mandir}/man1/timg.1*

%changelog
* Sat Mar 09 2024 ErrorNoInternet <errornointernet@envs.net> - 1.6.0-2
- Fix licenses and add clarification.
- Clean up descriptions and missing chaneglog entries.

* Fri Jan 26 2024 ErrorNoInternet <errornointernet@envs.net> - 1.6.0-1
- Update to version 1.6.0.

* Tue Nov 21 2023 ErrorNoInternet <errornointernet@envs.net> - 1.5.2-2
- Enable libsixel and qoi support as they are now in the Fedora repos.

* Thu Aug 31 2023 ErrorNoInternet <errornointernet@envs.net> - 1.5.2-1
- Update to version 1.5.2.

* Sat Jul 29 2023 ErrorNoInternet <errornointernet@envs.net> - 1.5.1-1
- Update to version 1.5.1.
- Disable libsixel support as it isn't packaged in the Fedora repos yet.

* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-6
- Fix package review issues.

* Sat Jul 08 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-5
- Fix package review issues.

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-4
- Fix package review issues.

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-3
- Add LICENSE and README.md.

* Wed May 24 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-2
- Install to /usr instead of /usr/local.

* Fri Apr 21 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-1
- Initial packaging.
