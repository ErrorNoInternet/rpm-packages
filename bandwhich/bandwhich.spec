# Generated by rust2rpm 26
%bcond_without check

%global cargo_install_lib 0

Name:           bandwhich
Version:        0.22.2
Release:        1%{?dist}
Summary:        Terminal bandwidth utilization tool 

SourceLicense:  MIT
License:        MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (LGPL-3.0-only) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

URL:            https://github.com/imsnif/bandwhich
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         bandwhich-fix-metadata-auto.diff
Patch1:         bandwhich-replace-git-deps.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
Display current network utilization by process, connection and remote
IP/hostname.}

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
%autosetup -n %{name}-%{version} -N
%autopatch 0
cargo vendor
%autopatch -m1 -p1
ln -s vendor/packet-builder packet-builder
%cargo_prep -v vendor

%build
mkdir gen
export BANDWHICH_GEN_DIR=gen

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm644 gen/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# install -Dpm644 res/%%{name}.svg %%{buildroot}%%{_datadir}/icons/hicolor/scalable/apps/%%{name}.svg

install -Dpm644 gen/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm644 gen/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm644 gen/_%{name} %{buildroot}%{zsh_completions_dir}/_%{name}

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
# %%doc INSTALL.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
# %%{_datadir}/icons/hicolor/scalable/apps/%%{name}.svg

%files bash-completion
%{bash_completions_dir}/%{name}

%files fish-completion
%{fish_completions_dir}/%{name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
