%global srcname timg

Name: timg
Version: main
Release: %autorelease
Summary: A terminal image and video viewer

License: GPL-2.0-or-later
URL: https://timg.sh
Source: https://github.com/hzeller/timg/archive/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: git
BuildRequires: g++
BuildRequires: pkg-config
BuildRequires: GraphicsMagick-c++-devel
BuildRequires: turbojpeg-devel
BuildRequires: libexif-devel
BuildRequires: libswscale-free-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: openslide-devel
BuildRequires: pandoc
BuildRequires: zlib-devel

%description
A user-friendly viewer that uses 24-Bit color capabilities and unicode character blocks to display images, animations and videos in the terminal.
On terminals that implement the Kitty Graphics Protocol or the iTerm2 Graphics Protocol this displays images in full resolution.

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/timg
%{_mandir}/timg.1

%changelog
* Wed Mar 29 2023 ErrorNoInternet <error.nointernet@gmail.com> main-1
- change tag

* Wed Mar 29 2023 ErrorNoInternet <error.nointernet@gmail.com> 1.4.5-1
- new package built with tito

