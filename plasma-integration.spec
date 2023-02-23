#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-integration
Version  : 5.27.1
Release  : 96
URL      : https://download.kde.org/stable/plasma/5.27.1/plasma-integration-5.27.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.1/plasma-integration-5.27.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.1/plasma-integration-5.27.1.tar.xz.sig
Summary  : Plasma's key data used for key-holding behaviour
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: plasma-integration-data = %{version}-%{release}
Requires: plasma-integration-lib = %{version}-%{release}
Requires: plasma-integration-license = %{version}-%{release}
Requires: plasma-integration-locales = %{version}-%{release}
BuildRequires : breeze
BuildRequires : breeze-dev
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtbase-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Framework Integration
Integration of Qt application with KDE workspaces
## Introduction

%package data
Summary: data components for the plasma-integration package.
Group: Data

%description data
data components for the plasma-integration package.


%package dev
Summary: dev components for the plasma-integration package.
Group: Development
Requires: plasma-integration-lib = %{version}-%{release}
Requires: plasma-integration-data = %{version}-%{release}
Provides: plasma-integration-devel = %{version}-%{release}
Requires: plasma-integration = %{version}-%{release}

%description dev
dev components for the plasma-integration package.


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
%setup -q -n plasma-integration-5.27.1
cd %{_builddir}/plasma-integration-5.27.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677185314
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1677185314
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-integration
cp %{_builddir}/plasma-integration-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-integration/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-integration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-integration/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-integration/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-integration/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-integration/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-integration/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-integration/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-integration/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-integration/e458941548e0864907e654fa2e192844ae90fc32 || :
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

%files dev
%defattr(-,root,root,-)
/usr/include/PlasmaKeyData/plasmakeydata.h
/usr/lib64/pkgconfig/plasma-key-data.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/platforminputcontexts/plasmaimplatforminputcontextplugin.so
/usr/lib64/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-integration/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/plasma-integration/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/plasma-integration/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/plasma-integration/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/plasma-integration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma-integration/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-integration/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/plasma-integration/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasmaintegration5.lang
%defattr(-,root,root,-)

