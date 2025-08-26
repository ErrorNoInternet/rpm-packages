Name:           mergerfs
Version:        2.41.0~rc0
Release:        1%{?dist}
Summary:        A featureful union filesystem

License:        ISC
URL:            https://github.com/trapexit/mergerfs
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  git
Requires:       fuse

%description
mergerfs is a union filesystem geared towards simplifying storage and
management of files across numerous commodity storage devices. It is
similar to mhddfs, unionfs, and aufs.

%prep
%autosetup -p1

%build
sed -i 's/chown root/# chown root/' libfuse/Makefile
%make_build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir} || true
mv %{buildroot}/sbin/mount.mergerfs %{buildroot}%{_bindir}
chmod +s %{buildroot}%{_bindir}/mergerfs

%files
%doc README.md
%license LICENSE
%{_bindir}/mergerfs
%{_bindir}/mergerfs-fusermount
%{_bindir}/mount.mergerfs
%{_libdir}/mergerfs/preload.so
%{_mandir}/*

%changelog
%autochangelog
