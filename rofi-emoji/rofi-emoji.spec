Name:           rofi-emoji
Version:        3.3.0
Release:        %autorelease
Summary:        Emoji selector plugin for Rofi

License:        MIT
URL:            https://github.com/Mange/rofi-emoji
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  rofi-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Recommends:     wl-clipboard
Recommends:     xclip

%description
An emoji selector plugin for Rofi that copies the selected emoji to the
clipboard, among other things.

%prep
%autosetup

%build
autoreconf -i
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/rofi-emoji/{LICENSE,README.md}

%check
make check

%files
%license LICENSE
%doc README.md Changelog.md
%{_libdir}/rofi/emoji.so
%{_datadir}/rofi-emoji/all_emojis.txt
%{_datadir}/rofi-emoji/clipboard-adapter.sh

%changelog
%autochangelog
