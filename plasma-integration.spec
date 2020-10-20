#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-integration
Version  : 5.20.1
Release  : 58
URL      : https://download.kde.org/stable/plasma/5.20.1/plasma-integration-5.20.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.20.1/plasma-integration-5.20.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.20.1/plasma-integration-5.20.1.tar.xz.sig
Summary  : No detailed summary available
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
BuildRequires : extra-cmake-modules-data
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtbase-staticdev
BuildRequires : qtdeclarative-dev

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
%setup -q -n plasma-integration-5.20.1
cd %{_builddir}/plasma-integration-5.20.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603217138
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1603217138
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-integration
cp %{_builddir}/plasma-integration-5.20.1/COPYING.LGPL-3 %{buildroot}/usr/share/package-licenses/plasma-integration/f45ee1c765646813b442ca58de72e20a64a7ddba
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
/usr/share/package-licenses/plasma-integration/f45ee1c765646813b442ca58de72e20a64a7ddba

%files locales -f plasmaintegration5.lang
%defattr(-,root,root,-)

