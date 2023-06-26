Name: mergerfs
Version: 2.35.1
Release: 1%{?dist}
Summary: A featureful FUSE based union filesystem

License: ISC
URL: https://github.com/trapexit/mergerfs
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: gcc-c++ git
Requires: fuse

%description
mergerfs is a union filesystem geared towards simplifying storage and
management of files across numerous commodity storage devices. It is
similar to mhddfs, unionfs, and aufs.

%global debug_package %{nil}

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
/usr/bin/mergerfs
/usr/bin/mergerfs-fusermount
/sbin/mount.mergerfs
%doc %{_mandir}/*

%changelog
* Mon Jun 26 2023 ErrorNoInternet <errornointernet@envs.net>
- Some minor changes

* Fri Apr 26 2019 Antonio SJ Musumeci <trapexit@spawn.link>
- Update description

* Mon Jan 25 2016 Antonio SJ Musumeci <trapexit@spawn.link>
- Remove sbin files

* Sat Sep 05 2015 Antonio SJ Musumeci <trapexit@spawn.link>
- Include PREFIX to install

* Mon Dec 29 2014 Joe Lawrence <joe.lawrence@stratus.com>
- Tweak rpmbuild to archive current git HEAD into a tarball, then (re)build in
  the rpmbuild directory -- more complicated but seemingly better suited to
  generate source and debug rpms.

* Fri Jun 20 2014 Joe Lawrence <joe.lawrence@stratus.com>
- Initial rpm spec file.
