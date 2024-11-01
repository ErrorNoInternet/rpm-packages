# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate random-fast-rng

Name:           rust-random-fast-rng
Version:        0.1.1
Release:        %autorelease
Summary:        Rust library for Blazing fast non cryptographic random number generator

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/random-fast-rng
Source:         %{crates_source}
# * https://github.com/elichai/random-rs/issues/2
Source1:        https://github.com/elichai/random-rs/raw/bd98b95/LICENSE-APACHE
Source2:        https://github.com/elichai/random-rs/raw/bd98b95/LICENSE-MIT
# Manually created patch for downstream crate metadata changes
# * remove reference to readme file that is not included in published crates
Patch:          random-fast-rng-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust library for Blazing fast non cryptographic random number generator.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+doc-comment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-comment-devel %{_description}

This package contains library source intended for building other packages which
use the "doc-comment" feature of the "%{crate}" crate.

%files       -n %{name}+doc-comment-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE1} %{SOURCE2} .

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
