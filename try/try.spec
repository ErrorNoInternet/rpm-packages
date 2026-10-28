%global _default_patch_fuzz 2
%global debug_package %{nil}

Name:           try
Version:        0.2.1
Release:        1%{?dist}
Summary:        Inspect a command's effects before modifying your live system

License:        MIT
URL:            https://github.com/binpash/try
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc
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
%autosetup -n %{name}-%{version} -p1

%build
autoconf
%configure
%make_build

%install
%make_install bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}
install -Dpm644 completions/try.bash %{buildroot}%{bash_completions_dir}/try

%files
%license LICENSE
%doc README.md STYLE.md
%{_bindir}/try
%{_bindir}/try-commit
%{_bindir}/try-parse-trace
%{_bindir}/try-summary
%{_mandir}/man1/try.1*

%files bash-completion
%{bash_completions_dir}/try

%changelog
%autochangelog
