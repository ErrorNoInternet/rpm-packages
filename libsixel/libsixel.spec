Name: libsixel
Version: 1.10.3
Release: 3%{?dist}
Summary: SIXEL encoding and decoding

License: MIT
URL: https://github.com/libsixel/libsixel
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: meson.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(gdlib)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)

%description
An encoder/decoder implementation for DEC SIXEL graphics.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package utils
Summary: SIXEL encoder and decoder utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson -Dtests=enabled
%meson_build

%install
%meson_install
rm %{buildroot}/%{_libdir}/libsixel.a

%check
%meson_test

%files
%license LICENSE
%doc AUTHORS
%doc NEWS
%doc README.md
%{_libdir}/libsixel.so.1
%{_libdir}/libsixel.so.1.0.0

%files devel
%{_bindir}/libsixel-config
%{_includedir}/sixel.h
%{_libdir}/libsixel.so
%{_libdir}/pkgconfig/libsixel.pc

%files utils
%{_bindir}/img2sixel
%{_bindir}/sixel2png
%{_mandir}/man1/img2sixel.1*
%{_mandir}/man1/sixel2png.1*
%{bash_completions_dir}/img2sixel
%{zsh_completions_dir}/_img2sixel

%changelog
* Wed Aug 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.10.3-3
- Enabled tests

* Wed Aug 30 2023 ErrorNoInternet <errornointernet@envs.net> - 1.10.3-2
- Fix a few package review issues

* Sat Jul 29 2023 ErrorNoInternet <errornointernet@envs.net> - 1.10.3-1
- Initial packaging
