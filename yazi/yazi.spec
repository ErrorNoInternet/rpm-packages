%bcond_without check

%global __brp_mangle_shebangs /usr/bin/true
%global _default_patch_fuzz 2
%global cargo_install_lib   0

Name:           yazi
Version:        25.3.2
Release:        1%{?dist}
Summary:        Blazing fast terminal file manager

License:        BSD-2-Clause AND (0BSD OR MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (MIT OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND MIT AND (MIT OR Apache-2.0 OR NCSA) AND (Apache-2.0 OR BSL-1.0) AND (Unlicense OR MIT) AND Apache-2.0 AND (CC0-1.0 OR Apache-2.0) AND BSD-3-Clause AND MPL-2.0 AND ISC AND Zlib AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 OR MIT) AND CC0-1.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND BSL-1.0
SourceLicense:  MIT

URL:            https://github.com/sxyazi/yazi
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  make

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

install -Dpm644 yazi-boot/completions/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm644 yazi-boot/completions/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm644 yazi-boot/completions/_%{name} %{buildroot}%{zsh_completions_dir}/_%{name}

install -Dpm644 assets/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

for size in {1024,512,256,128,64,32,16}; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$size"x"$size"/apps
    magick assets/logo.png -resize "$size"x"$size"\! %{buildroot}%{_datadir}/icons/hicolor/"$size"x"$size"/apps/%{name}.png
done

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE LICENSE-ICONS
%license LICENSE.dependencies cargo-vendor.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/ya
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files bash-completion
%{bash_completions_dir}/%{name}

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%files fish-completion
%{fish_completions_dir}/%{name}.fish

%changelog
%autochangelog
