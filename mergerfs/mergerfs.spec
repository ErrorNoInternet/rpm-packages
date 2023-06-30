%global debug_package %{nil}

Name: mergerfs
Version: 2.35.1
Release: 2%{?dist}
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

%prep
%autosetup -n %{name}-%{version}

%build
# chown root causes permission issues
mv libfuse/Makefile tmp-Makefile
sed 's/chown root/echo IGNORING: chown root/g' tmp-Makefile > libfuse/Makefile

make %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%doc %{_mandir}/*
%{_bindir}/mergerfs
%{_bindir}/mergerfs-fusermount
/sbin/mount.mergerfs

%changelog
* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 2.35.1-2
- Add LICENSE and README.md

* Mon Jun 26 2023 ErrorNoInternet <errornointernet@envs.net> - 2.35.1-1
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
