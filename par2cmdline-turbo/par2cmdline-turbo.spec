Name:           par2cmdline-turbo
Version:        1.3.0
Release:        %autorelease
Summary:        Speed focused par2cmdline fork

License:        GPL-2.0-or-later
URL:            https://github.com/animetosho/par2cmdline-turbo
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  gcc-c++

%description
A *simple* fork of par2cmdline which replaces core computation
routines with ParPar’s processing backend, improving par2cmdline’s
performance on x86/ARM platforms.

%prep
%autosetup -p1

%build
./automake.sh
%configure
%make_build

%install
%make_install

mv %{buildroot}%{_bindir}/par2 %{buildroot}%{_bindir}/par2turbo
rm -f %{buildroot}%{_bindir}/par2create \
      %{buildroot}%{_bindir}/par2repair \
      %{buildroot}%{_bindir}/par2verify \
      %{buildroot}%{_bindir}/par2
ln -s par2turbo %{buildroot}%{_bindir}/par2turbo-create
ln -s par2turbo %{buildroot}%{_bindir}/par2turbo-repair
ln -s par2turbo %{buildroot}%{_bindir}/par2turbo-verify
mv %{buildroot}%{_mandir}/man1/par2.1 %{buildroot}%{_mandir}/man1/par2turbo.1

%check
%make_build check-TESTS

%files
%doc AUTHORS
%doc ChangeLog
%doc README.md
%license COPYING
%{_bindir}/par2turbo
%{_bindir}/par2turbo-create
%{_bindir}/par2turbo-repair
%{_bindir}/par2turbo-verify
%{_mandir}/man1/par2turbo.1*

%changelog
%autochangelog
