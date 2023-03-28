%global srcname timg

Name: timg
Version: 1.4.5
Release: 1%{?dist}
Summary: A terminal image and video viewer.

License: GPL-2.0
URL: https://timg.sh
Source0: https://github.com/hzeller/timg/archive/refs/tags/v%{version}.tar.gz

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
mkdir build
cd build
%cmake ..
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/timg
%{_mandir}/timg.1

%changelog
