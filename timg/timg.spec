Name: timg
Version: 1.4.5
Release: %{autorelease}
Summary: A terminal image and video viewer

License: GPL-2.0-or-later
URL: https://github.com/hzeller/timg
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cmake git g++ pkg-config GraphicsMagick-c++-devel turbojpeg-devel libexif-devel libswscale-free-devel libavcodec-free-devel libavformat-free-devel libavdevice-free-devel openslide-devel pandoc zlib-devel

%description
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
/usr/local/share/man/man1/timg.1
/usr/local/bin/timg

%changelog
* Fri Apr 21 2023 ErrorNoInternet <errornointernet@envs.net> - 1.4.5-1
- Hello, world!
