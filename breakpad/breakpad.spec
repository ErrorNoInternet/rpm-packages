Name:               breakpad
Version:            2023.06.01
Release:            %autorelease
Summary:            A crash-reporting system

License:            BSD-3-Clause
URL:                https://chromium.googlesource.com/breakpad/breakpad
Source0:            %{url}/+archive/v%{version}.tar.gz
Source1:            https://chromium.googlesource.com/linux-syscall-support/+archive/v2024.02.01.tar.gz
Patch0:             breakpad-fix-missing-include.patch

BuildRequires:      gcc-c++
BuildRequires:      pkgconfig(gmock)
BuildRequires:      pkgconfig(gtest)
BuildRequires:      pkgconfig(zlib)

%description
A set of client and server components which implement a crash-reporting system.

%prep
tar xf %{SOURCE0}
mkdir -p src/third_party/lss
tar xf %{SOURCE1} -C src/third_party/lss

%autopatch -p1

%build
export CFLAGS="$CFLAGS -Wno-error"
export CXXFLAGS="$CXXFLAGS -Wno-error"

%configure
%make_build

%install
%make_install

rm -rf %{buildroot}%{_docdir}/breakpad-0.1

%files
%license LICENSE
%doc README.md AUTHORS ChangeLog INSTALL NEWS
%{_bindir}/core2md
%{_bindir}/dump_syms
%ifarch x86_64 %{ix86}
%{_bindir}/dump_syms_mac
%endif
%{_bindir}/microdump_stackwalk
%{_bindir}/minidump-2-core
%{_bindir}/minidump_dump
%{_bindir}/minidump_stackwalk
%{_bindir}/minidump_upload
%{_bindir}/pid2md
%{_bindir}/sym_upload
%{_includedir}/breakpad
%{_libdir}/libbreakpad.a
%{_libdir}/libbreakpad_client.a
%{_libdir}/pkgconfig/breakpad-client.pc
%{_libdir}/pkgconfig/breakpad.pc
%{_libexecdir}/core_handler

%changelog
%autochangelog
