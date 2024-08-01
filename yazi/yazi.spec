%bcond_without check

%global _default_patch_fuzz 2

%global crate               yazi
%global cargo_install_lib   0

Name:           yazi
Version:        0.3.0
Release:        1%{?dist}
Summary:        Blazing fast terminal file manager

# BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSL-1.0
# CC0-1.0
# CC0-1.0 OR Apache-2.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR NCSA
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License: Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  MIT

URL:            https://github.com/sxyazi/yazi
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          yazi-replace-git-deps.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
BuildRequires:  gcc

Recommends:     7zip
Recommends:     chafa
Recommends:     ImageMagick

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
%autosetup -n %{name}-%{version} -N
cargo vendor
%autopatch 0 -p1
cargo vendor # vendor `notify`'s dependencies
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
%license LICENSE LICENSE-ICONS
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/ya
%{_bindir}/yazi
%{_datadir}/applications/yazi.desktop

%files bash-completion
%{bash_completions_dir}/yazi

%files zsh-completion
%{zsh_completions_dir}/_yazi

%files fish-completion
%{fish_completions_dir}/yazi.fish

%changelog
%autochangelog
