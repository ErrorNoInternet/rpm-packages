%global debug_package %{nil}

Name:		    vesktop
Version:	    1.5.2
Release:        %autorelease
Summary:	    Vesktop is a custom Discord desktop app

License:	    GPL-3.0-only
URL:		    https://github.com/Vencord/Vesktop

Source0:	    %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:	    vesktop.sh
Source2:	    vesktop.desktop

Patch0:         remove-splash.diff
Patch1:         tray-notifications.diff

BuildRequires:	pnpm

%description
Vesktop is a custom Discord desktop app aiming to give
you better performance and improve Linux support.

%prep
%autosetup -n Vesktop-%{version} -p1

%build
export COREPACK_ENABLE_STRICT=0
pnpm i
pnpm package:dir

%install
mkdir -p %{buildroot}%{_prefix}/lib
cp -pr dist/linux*-unpacked %{buildroot}%{_prefix}/lib/vesktop
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/vesktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datarootdir}/applications/vesktop.desktop
install -Dm644 static/icon.png %{buildroot}%{_datarootdir}/pixmaps/vesktop.png

%files
%doc README.md
%license LICENSE
%{_bindir}/vesktop
%{_prefix}/lib/vesktop
%{_datarootdir}/applications/vesktop.desktop
%{_datarootdir}/pixmaps/vesktop.png

%changelog
%autochangelog
