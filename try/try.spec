%global debug_package %{nil}

Name:           try
Version:        0.2.0
Release:        4%{?dist}
Summary:        Inspect a command's effects before modifying your live system

License:        MIT
URL:            https://github.com/binpash/try
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
%autosetup

%build
%make_build -C man

%check
./scripts/lint.sh

%install
install -Dpm755 try %{buildroot}%{_bindir}/try
install -Dpm644 man/try.1 %{buildroot}%{_mandir}/man1/try.1
install -Dpm644 completions/try.bash %{buildroot}%{bash_completions_dir}/try

%files
%license LICENSE
%doc README.md STYLE.md
%{_bindir}/try
%{_mandir}/man1/try.1*

%files bash-completion
%{bash_completions_dir}/try

%changelog
%autochangelog
