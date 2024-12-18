# Generated by go2rpm 1.14.0
%bcond check 0
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/abenz1267/walker
%global goipath         github.com/abenz1267/walker
Version:                0.10.20

%gometa -L -f

%global common_description %{expand:
Walker is a highly extendable application launcher that does not hold
back on features and usability. Fast. Unclutters your brain. Improves
your workflow.}

%global golicenses      LICENSE
%global godocs          README.md cmd/version.txt

Name:           walker
Release:        %autorelease
Summary:        Wayland-native application launcher

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
BuildRequires:  pkgconfig(vips)

Recommends:     wl-clipboard

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
go mod vendor
%endif

%if %{without bootstrap}
%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

chmod -R u+w %{gobuilddir}/pkg
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE vendor/modules.txt
%doc README.md cmd/version.txt
%{_bindir}/*
%endif

%gopkgfiles

%changelog
%autochangelog
