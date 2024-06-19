%global debug_package %{nil}

Name: mergerfs
Version: 2.40.2
Release: 3%{?dist}
Summary: A featureful FUSE based union filesystem

License: ISC
URL: https://github.com/trapexit/mergerfs
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: git
Requires: fuse

%description
mergerfs is a union filesystem geared towards simplifying storage and
management of files across numerous commodity storage devices. It is
similar to mhddfs, unionfs, and aufs.

%prep
%autosetup -n %{name}-%{version} -p1

%build
sed -i 's/chown root//' libfuse/Makefile
%make_build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}
mv %{buildroot}%{prefix}/lib %{buildroot}%{_libdir}

%files
%doc README.md
%license LICENSE
%{_mandir}/mergerfs.1*
%{_bindir}/mergerfs
%{_bindir}/mergerfs-fusermount
%{_libdir}/mergerfs/preload.so
/sbin/mount.mergerfs

%changelog
%autochangelog
