Name: timg
Version: 1.4.5
Release: 6%{?dist}
Summary: A terminal image and video viewer

License: GPL-2.0-only AND GPL-2.0-or-later AND MIT
URL: https://github.com/hzeller/timg
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: GraphicsMagick-c++-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libdeflate-devel
BuildRequires: libsixel
BuildRequires: libexif-devel
BuildRequires: libswscale-free-devel
BuildRequires: openslide-devel
BuildRequires: pandoc
BuildRequires: pkg-config
BuildRequires: stb_image-devel
BuildRequires: stb_image_resize-devel
BuildRequires: turbojpeg-devel

%description
A user-friendly viewer that uses 24-Bit color capabilities and unicode
character blocks to display images, animations and videos in the
terminal. On terminals that implement the Kitty Graphics Protocol or
the iTerm2 Graphics Protocol this displays images in full resolution.

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
%{_mandir}/man1/timg.1*
%{_bindir}/timg

%changelog
* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-6
- Bump version and fix package review issues

* Sat Jul 08 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-5
- Fix package review issues

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-4
- Fix Fedora Review issues

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-3
- Add LICENSE and README.md

* Wed May 24 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-2
- Install to /usr instead of /usr/local

* Fri Apr 21 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-1
- Hello, world!
