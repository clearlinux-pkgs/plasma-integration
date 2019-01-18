#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-integration
Version  : 5.14.5
Release  : 13
URL      : https://download.kde.org/stable/plasma/5.14.5/plasma-integration-5.14.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.5/plasma-integration-5.14.5.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.5/plasma-integration-5.14.5.tar.xz.sig
Summary  : Qt Platform Theme integration plugins for the Plasma workspaces
Group    : Development/Tools
License  : LGPL-3.0
Requires: plasma-integration-data = %{version}-%{release}
Requires: plasma-integration-lib = %{version}-%{release}
Requires: plasma-integration-license = %{version}-%{release}
Requires: plasma-integration-locales = %{version}-%{release}
BuildRequires : breeze
BuildRequires : breeze-dev
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : qtbase-dev mesa-dev

%description
# Framework Integration
Integration of Qt application with KDE workspaces
## Introduction

%package data
Summary: data components for the plasma-integration package.
Group: Data

%description data
data components for the plasma-integration package.


%package lib
Summary: lib components for the plasma-integration package.
Group: Libraries
Requires: plasma-integration-data = %{version}-%{release}
Requires: plasma-integration-license = %{version}-%{release}

%description lib
lib components for the plasma-integration package.


%package license
Summary: license components for the plasma-integration package.
Group: Default

%description license
license components for the plasma-integration package.


%package locales
Summary: locales components for the plasma-integration package.
Group: Default

%description locales
locales components for the plasma-integration package.


%prep
%setup -q -n plasma-integration-5.14.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546968478
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1546968478
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-integration
cp COPYING.LGPL-3 %{buildroot}/usr/share/package-licenses/plasma-integration/COPYING.LGPL-3
pushd clr-build
%make_install
popd
%find_lang plasmaintegration5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kconf_update/fonts_akregator.pl
/usr/share/kconf_update/fonts_akregator.upd
/usr/share/kconf_update/fonts_global.pl
/usr/share/kconf_update/fonts_global.upd
/usr/share/kconf_update/fonts_global_toolbar.upd
/usr/share/kconf_update/fonts_kate.pl
/usr/share/kconf_update/fonts_kate.upd

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-integration/COPYING.LGPL-3

%files locales -f plasmaintegration5.lang
%defattr(-,root,root,-)

