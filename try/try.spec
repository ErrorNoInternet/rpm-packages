%global debug_package %{nil}

Name: try
Version: 0.2.0
Release: 2%{?dist}
Summary: Inspect a command's effects before modifying your live system

License: MIT
URL: https://github.com/binpash/try
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: make pandoc
Requires: util-linux mergerfs

%description
`try` lets you run a command and inspect its effects before changing
your live system. `try` uses Linux's namespaces (via `unshare`) and
the overlayfs union filesystem.

%prep
%autosetup -n %{name}-%{version}

%build
%make -C man

%install
install -Dpm644 try %{buildroot}%{_bindir}/try
install -Dpm644 man/try.1 %{buildroot}%{_mandir}/man1/try.1
install -Dpm644 completions/try.bash %{bash_completions_dir}/try

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/try.1.gz
%{_bindir}/try
%{bash_completions_dir}/try

%changelog
%autochangelog
