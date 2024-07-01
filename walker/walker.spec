%global goipath         github.com/abenz1267/walker
Version:                0.0.74

%gometa -L -f

%global common_description %{expand:
Wayland-native application runner.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           walker
Release:        %autorelease
Summary:        Wayland-native application runner

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  git
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(pango)

Recommends:     wl-clipboard

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1
go mod vendor

%build
%gobuild -o %{gobuilddir}/bin/walker %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

chmod -R u+w %{gobuilddir}/pkg

%files
%license LICENSE
%license vendor/modules.txt
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
