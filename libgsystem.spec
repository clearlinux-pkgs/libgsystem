#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgsystem
Version  : 2015.2
Release  : 12
URL      : http://pkgs.fedoraproject.org/repo/pkgs/libgsystem/libgsystem-2015.2.tar.xz/e388e3ad3c2b527479cc8512f6ad9a37/libgsystem-2015.2.tar.xz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/libgsystem/libgsystem-2015.2.tar.xz/e388e3ad3c2b527479cc8512f6ad9a37/libgsystem-2015.2.tar.xz
Summary  : https://live.gnome.org/Projects/libgsystem
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libgsystem-lib = %{version}-%{release}
Requires: libgsystem-license = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libcap-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gio-unix-2.0)
Patch1: remove_xaatr_header_check.patch

%description
Pending deprecation
-------------------
This library is pending deprecation and no new APIs will be
added.  For more information, see:

%package dev
Summary: dev components for the libgsystem package.
Group: Development
Requires: libgsystem-lib = %{version}-%{release}
Provides: libgsystem-devel = %{version}-%{release}
Requires: libgsystem = %{version}-%{release}

%description dev
dev components for the libgsystem package.


%package lib
Summary: lib components for the libgsystem package.
Group: Libraries
Requires: libgsystem-license = %{version}-%{release}

%description lib
lib components for the libgsystem package.


%package license
Summary: license components for the libgsystem package.
Group: Default

%description license
license components for the libgsystem package.


%prep
%setup -q -n libgsystem-2015.2
cd %{_builddir}/libgsystem-2015.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592683016
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --without-systemd-journal
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592683016
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgsystem
cp %{_builddir}/libgsystem-2015.2/COPYING %{buildroot}/usr/share/package-licenses/libgsystem/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/libgsystem-2015.2/libglnx/COPYING %{buildroot}/usr/share/package-licenses/libgsystem/ba8966e2473a9969bdcab3dc82274c817cfd98a1
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libgsystem/gsystem-console.h
/usr/include/libgsystem/gsystem-errors.h
/usr/include/libgsystem/gsystem-file-utils.h
/usr/include/libgsystem/gsystem-glib-compat.h
/usr/include/libgsystem/gsystem-local-alloc.h
/usr/include/libgsystem/gsystem-log.h
/usr/include/libgsystem/gsystem-shutil.h
/usr/include/libgsystem/gsystem-subprocess-context.h
/usr/include/libgsystem/gsystem-subprocess.h
/usr/include/libgsystem/libgsystem.h
/usr/lib64/libgsystem.so
/usr/lib64/pkgconfig/libgsystem.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgsystem.so.0
/usr/lib64/libgsystem.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgsystem/ba8966e2473a9969bdcab3dc82274c817cfd98a1
