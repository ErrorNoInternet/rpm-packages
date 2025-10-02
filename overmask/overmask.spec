%bcond_without check

%global commit 28b951d1ad14db38375c63882cc021294ec1a2e2
%global snapdate 20251002

%global cargo_install_lib 0

Name:           overmask
Version:        0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:        %autorelease
Summary:        Add a writeable overlay on top of read-only files

SourceLicense:  LGPL-3.0-only
License:        LGPL-3.0-only AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

URL:            https://github.com/ErrorNoInternet/overmask
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  systemd-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{name}-fish-completion = %{version}-%{release}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{name}-zsh-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%prep
%autosetup -n %{name}-%{commit} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm644 completions/overmask.bash %{buildroot}%{bash_completions_dir}/overmask
install -Dpm644 completions/overmask.fish %{buildroot}%{fish_completions_dir}/overmask.fish
install -Dpm644 completions/_overmask %{buildroot}%{zsh_completions_dir}/_overmask

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/overmask

%files bash-completion
%{bash_completions_dir}/overmask

%files fish-completion
%{fish_completions_dir}/overmask.fish

%files zsh-completion
%{zsh_completions_dir}/_overmask

%changelog
%autochangelog
