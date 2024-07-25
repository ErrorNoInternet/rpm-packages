%global commit          4acc903a20f8eb2fccb5fd0cd9d1d11e64741c24
%global snapdate        20240724

%global debug_package   %{nil}

Name:           try-git
Version:        0.2.0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:        %autorelease
Summary:        Inspect a command's effects before modifying your live system

License:        MIT
URL:            https://github.com/binpash/try
Source:         %{url}/archive/%{commit}/try-%{commit}.tar.gz

Obsoletes:      try <= 0.2.0

BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  kmod
BuildRequires:  make
BuildRequires:  pandoc

Requires:       mergerfs
Requires:       util-linux

%description
`try` lets you run a command and inspect its effects before changing
your live system. `try` uses Linux's namespaces (via `unshare`) and
the overlayfs union filesystem.

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%prep
%autosetup -n try-%{commit} -p1

%build
autoconf
%configure
%make_build man/try.1 utils/try-commit utils/try-summary

%check
./scripts/check_version.sh
# make lint

%install
install -Dpm755 try %{buildroot}%{_bindir}/try
install -Dpm755 utils/try-commit %{buildroot}%{_bindir}/try-commit
install -Dpm755 utils/try-summary %{buildroot}%{_bindir}/try-summary
install -Dpm644 man/try.1 %{buildroot}%{_mandir}/man1/try.1
install -Dpm644 completions/try.bash %{buildroot}%{bash_completions_dir}/try

%files
%license LICENSE
%doc README.md STYLE.md
%{_bindir}/try
%{_bindir}/try-commit
%{_bindir}/try-summary
%{_mandir}/man1/try.1*

%files bash-completion
%{bash_completions_dir}/try

%changelog
%autochangelog
