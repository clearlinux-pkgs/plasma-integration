#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: f9eab48
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-integration
Version  : 6.1.0
Release  : 116
URL      : https://download.kde.org/stable/plasma/6.1.0/plasma-integration-6.1.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.0/plasma-integration-6.1.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.0/plasma-integration-6.1.0.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : plasma5support-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtbase-staticdev
BuildRequires : qtdeclarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Plasma Integration
Integrates Qt applications with the KDE workspace by providing a QPlatformTheme. Applications do not need to link to this directly.

%package lib
Summary: lib components for the plasma-integration package.
Group: Libraries
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-integration-6.1.0
cd %{_builddir}/plasma-integration-6.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718822017
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBUILD_QT6=ON \
-DBUILD_QT5=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DBUILD_QT6=ON \
-DBUILD_QT5=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718822017
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
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang plasmaintegration5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/platformthemes/KDEPlasmaPlatformTheme6.so
/usr/lib64/qt6/plugins/platformthemes/KDEPlasmaPlatformTheme6.so

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

