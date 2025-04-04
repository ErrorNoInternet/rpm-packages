Name:           dwarfs
Version:        0.11.3
Release:        %autorelease
Summary:        A fast high compression read-only file system for Linux, Windows and macOS

License:        GPL-3.0-or-later
URL:            https://github.com/mhx/dwarfs
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(double-conversion)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(utf8cpp)
BuildRequires:  fuse3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libdwarf)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libglog)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)

%description
The Deduplicating Warp-speed Advanced Read-only File System.
A fast high compression read-only file system for Linux and Windows.

%prep
%autosetup -p1

%build
%cmake -GNinja -DWITH_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md CHANGES.md
%license LICENSE
%{_bindir}/dwarfsck
%{_bindir}/dwarfsextract
%{_bindir}/mkdwarfs
%{_includedir}/dwarfs/*
%{_libdir}/cmake/dwarfs/*
%{_libdir}/libdwarfs*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_prefix}/sbin/dwarfs
%{_prefix}/sbin/mount.dwarfs

%changelog
%autochangelog
