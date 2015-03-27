#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xauth
Version  : 1.0.9
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/app/xauth-1.0.9.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/xauth-1.0.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT MIT-Opengroup
Requires: xauth-bin
Requires: xauth-doc
BuildRequires : cmdtest
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xmuu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xtrans)
BuildRequires : python-cliapp
BuildRequires : python-ttystatus

%description
I. OVERVIEW
The xauth program is used to edit and display the authorization
information used in connecting to the X server.
The underlying "Authorization Protocol for X" is described in the

%package bin
Summary: bin components for the xauth package.
Group: Binaries

%description bin
bin components for the xauth package.


%package doc
Summary: doc components for the xauth package.
Group: Documentation

%description doc
doc components for the xauth package.


%prep
%setup -q -n xauth-1.0.9

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xauth

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
