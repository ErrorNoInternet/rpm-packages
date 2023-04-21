Name: timg
Version: 1.4.5
Release: %autorelease
Summary: A terminal image and video viewer

License: GPL-2.0-or-later
URL: https://github.com/hzeller/timg
Source0: %{url}/archive/v%{version}.tar.gz

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
Upstream: https://github.com/hzeller/timg

A user-friendly viewer that uses 24-Bit color capabilities and unicode character blocks to display images, animations and videos in the terminal.
On terminals that implement the Kitty Graphics Protocol or the iTerm2 Graphics Protocol this displays images in full resolution.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
cmake ..
%make_build

%install
cd build
%make_install

%files
%license LICENSE
%doc README.md
/usr/local/share/man/man1/timg.1
/usr/local/bin/timg

%changelog
