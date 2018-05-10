#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgsystem
Version  : 2015.2
Release  : 6
URL      : http://pkgs.fedoraproject.org/repo/pkgs/libgsystem/libgsystem-2015.2.tar.xz/e388e3ad3c2b527479cc8512f6ad9a37/libgsystem-2015.2.tar.xz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/libgsystem/libgsystem-2015.2.tar.xz/e388e3ad3c2b527479cc8512f6ad9a37/libgsystem-2015.2.tar.xz
Summary  : https://live.gnome.org/Projects/libgsystem
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libgsystem-lib
BuildRequires : attr-dev
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libcap-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-unix-2.0)

%description
Pending deprecation
-------------------
This library is pending deprecation and no new APIs will be
added.  For more information, see:

%package dev
Summary: dev components for the libgsystem package.
Group: Development
Requires: libgsystem-lib
Provides: libgsystem-devel

%description dev
dev components for the libgsystem package.


%package lib
Summary: lib components for the libgsystem package.
Group: Libraries

%description lib
lib components for the libgsystem package.


%prep
%setup -q -n libgsystem-2015.2

%build
%autogen --disable-static --without-systemd-journal
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
