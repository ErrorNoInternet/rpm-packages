%global commit      f3397776dbe2ed6be90197ea57fbd39c564566dc
%global snapdate    20250424

Name:               asmfetch
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            %autorelease
Summary:            A fetch tool written in x86-64 assembly for Linux

License:            LGPL-3.0-or-later
URL:                https://github.com/ErrorNoInternet/asmfetch
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

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
