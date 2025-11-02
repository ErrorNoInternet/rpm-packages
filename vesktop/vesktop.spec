%global _default_patch_fuzz 2
%global debug_package       %{nil}

Name:           vesktop
Version:        1.6.1
Release:        1%{?dist}
Summary:        Vesktop is a custom Discord desktop app

License:        GPL-3.0-only
URL:            https://github.com/Vencord/Vesktop

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        vesktop.sh
Source2:        vesktop.desktop

BuildRequires:  nodejs-npm
BuildRequires:  pnpm

%description
Vesktop is a custom Discord desktop app aiming to give
you better performance and improve Linux support.

%prep
%autosetup -n Vesktop-%{version} -p1

%build
export COREPACK_ENABLE_STRICT=0
pnpm i electron-builder@next
pnpm i
pnpm package:dir

%install
mkdir -p %{buildroot}%{_libdir}
cp -pr dist/linux*-unpacked %{buildroot}%{_libdir}/vesktop
install -Dpm755 %{SOURCE1} %{buildroot}%{_bindir}/vesktop
install -Dpm644 %{SOURCE2} %{buildroot}%{_datarootdir}/applications/vesktop.desktop
install -Dpm644 static/icon.png %{buildroot}%{_datarootdir}/pixmaps/vesktop.png

%files
%doc README.md
%license LICENSE
%{_bindir}/vesktop
%{_libdir}/vesktop
%{_datarootdir}/applications/vesktop.desktop
%{_datarootdir}/pixmaps/vesktop.png

%changelog
%autochangelog
