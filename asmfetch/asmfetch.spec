%global commit      affd46a9227dd6009fad0f486923c22337796c48
%global snapdate    20250428

Name:               asmfetch
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            %autorelease
Summary:            A fetch tool written in x86-64 assembly for Linux

License:            LGPL-3.0-or-later
URL:                https://github.com/ErrorNoInternet/asmfetch
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

ExclusiveArch:      x86_64

BuildRequires:      gcc

%description
A fetch tool written in x86-64 assembly for Linux.
Runs in under 150 microseconds and has zero dependencies.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
gcc -nostdlib %{optflags} asmfetch.S -o asmfetch

%install
mkdir -p %{buildroot}%{_bindir}
mv asmfetch %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/asmfetch

%changelog
%autochangelog
