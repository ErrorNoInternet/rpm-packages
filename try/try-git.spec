%global commit          f938e2a57e6abae2c8fecf686d1e7538305d0d8d
%global snapdate        20241213
%global latest          0.2.0

%global debug_package   %{nil}

Name:           try-git
Version:        %{latest}^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:        %autorelease
Summary:        Inspect a command's effects before modifying your live system

License:        MIT
URL:            https://github.com/binpash/try
Source:         %{url}/archive/%{commit}/try-%{commit}.tar.gz
Patch:          ignore-vfat-mounts.diff

Obsoletes:      try <= %{latest}

BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  expect
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
%make_build

%check
sed -i 's/ $//' Makefile
# make test
# make lint

%install
%make_install bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}
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
