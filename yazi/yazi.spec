# Generated by rust2rpm 26
%bcond_without check

%global crate yazi
%global cargo_install_lib 0

Name:           yazi
Version:        0.2.5
Release:        2%{?dist}
Summary:        Blazing fast terminal file manager
License:        MIT

URL:            https://github.com/sxyazi/yazi
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
BuildRequires:  gcc

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
%autosetup -n %{name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
export YAZI_GEN_COMPLETIONS=1
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
cd yazi-cli
%cargo_install
cd ../yazi-fm
%cargo_install
cd ..

install -Dpm644 assets/yazi.desktop %{buildroot}%{_datadir}/applications/yazi.desktop

install -Dpm644 yazi-boot/completions/yazi.bash %{buildroot}%{bash_completions_dir}/yazi
install -Dpm644 yazi-boot/completions/yazi.fish %{buildroot}%{fish_completions_dir}/yazi.fish
install -Dpm644 yazi-boot/completions/_yazi %{buildroot}%{zsh_completions_dir}/_yazi

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_datadir}/applications/yazi.desktop
%{_bindir}/ya
%{_bindir}/yazi

%files bash-completion
%{bash_completions_dir}/yazi

%files zsh-completion
%{zsh_completions_dir}/_yazi

%files fish-completion
%{fish_completions_dir}/yazi.fish

%changelog
%autochangelog
