%define libname %mklibname guestfs 0
%define glibname %mklibname guestfs-gobject-1.0 0
%define devname %mklibname -d guestfs
%define gdevname %mklibname -d guestfs-gobject-1.0

# FIXME the Provides: generator for matching provides
# seems to be broken
%global __requires_exclude ^ocamlx.*$

%global _disable_ld_no_undefined 1

Summary:	Library and tools for accessing virtual machine disk images
Name:		libguestfs
Version:	1.48.1
Release:	21
Source0:	https://download.libguestfs.org/%(echo %{version}|cut -d. -f1-2)-stable/libguestfs-%{version}.tar.gz
Source1:	libguestfs.rpmlintrc
Group:		System/Libraries
License:	LGPLv2.1/GPLv2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	libtool
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(jansson) >= 2.7
BuildRequires:	pkgconfig(libmagic)
BuildRequires:	pkgconfig(libvirt)
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(hivex)
BuildRequires:	jdk-current
# BuildRequires:	golang
BuildRequires:	pkgconfig(lua)
# BuildRequires:	pkgconfig(ruby)  # disabled for OCaml rebuild
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-hivex
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	pkgconfig(augeas)
BuildRequires:	pkgconfig(libselinux)
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	systemtap-devel
BuildRequires:	xorriso
BuildRequires:	qemu
BuildRequires:	qemu-img
BuildRequires:	qemu-kvm
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-hivex
BuildRequires:	vala-devel
BuildRequires:	gperf
BuildRequires:	mkisofs
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	supermin
# For xmllint
BuildRequires:	libxml2-utils
# For appliance creation
BuildRequires:	dnf
BuildRequires:	dnf-command(download)

%description
libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images.
You can use this for viewing and editing files inside guests, scripting changes
to VMs, monitoring disk used/free statistics, creating guests, P2V, V2V,
performing backups, cloning VMs, building VMs, formatting disks, resizing
disks, and much more.

libguestfs can access almost any disk image imaginable. It can do it
securely — without needing root and with multiple layers of defence against
rogue disk images.
It can access disk images on remote machines or on CDs/USB sticks.
It can access proprietary systems like VMware and Hyper-V.

%files -f libguestfs.lang -f guestfs-main-extra.files
%config %{_sysconfdir}/libguestfs-tools.conf
%{_bindir}/guestfish
%{_bindir}/guestmount
%{_bindir}/guestunmount
%{_bindir}/libguestfs-test-tool
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libguestfs
Group:		Development/C and C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for libguestfs

%files -n %{devname}
%{_includedir}/guestfs.h
%{_libdir}/libguestfs.so
%{_mandir}/man3/*.3*
%{_libdir}/pkgconfig/libguestfs.pc

#---------------------------------------------------------------------------

%package -n %{gdevname}
Summary:	GObject bindings to libguestfs
Group:		Development/C and C++
Requires:	%{glibname} = %{EVRD}

%description -n %{gdevname}
GObject bindings to libguestfs

%files -n %{gdevname}
%{_includedir}/guestfs-gobject.h
%{_includedir}/guestfs-gobject
%{_libdir}/libguestfs-gobject-1.0.so
%{_libdir}/pkgconfig/libguestfs-gobject-1.0.pc
%{_datadir}/gir-1.0/Guestfs-1.0.gir
%{_libdir}/girepository-1.0/Guestfs-1.0.typelib

#---------------------------------------------------------------------------

%if 0
%package -n go-libguestfs
Summary:	Go bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n go-libguestfs
Go bindings for libguestfs

%files -n go-libguestfs
%endif

#---------------------------------------------------------------------------

%package -n java-libguestfs
Summary:	Java bindings for libguestfs
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description -n java-libguestfs
Java bindings for libguestfs

%files -n java-libguestfs
%{_datadir}/java/libguestfs-%{version}.jar
%{_datadir}/javadoc/libguestfs
%{_libdir}/libguestfs_jni.so*

#---------------------------------------------------------------------------

%package -n lua-libguestfs
Summary:	Lua bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n lua-libguestfs
Lua bindings for libguestfs

%files -n lua-libguestfs -f lua-libguestfs.files

#---------------------------------------------------------------------------

%package -n ocaml-libguestfs
Summary:	Objective-CAML bindings for libguestfs
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description -n ocaml-libguestfs
Objective-CAML bindings for libguestfs

%files -n ocaml-libguestfs
%{_libdir}/ocaml/guestfs
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner

#---------------------------------------------------------------------------

%package -n python-libguestfs
Summary:	Python bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n python-libguestfs
Python bindings for libguestfs

%files -n python-libguestfs -f python-libguestfs.files

#---------------------------------------------------------------------------

%if 0
%package -n ruby-libguestfs
Summary:	Ruby bindings for libguestfs
Group:		Development/Ruby
Requires:	%{libname} = %{EVRD}

%description -n ruby-libguestfs
Ruby bindings for libguestfs

%files -n ruby-libguestfs
%endif

#---------------------------------------------------------------------------

%package -n vala-libguestfs
Summary:	Vala bindings for libguestfs
Group:		Development/Vala
Requires:	%{libname} = %{EVRD}

%description -n vala-libguestfs
Vala bindings for libguestfs

%files -n vala-libguestfs
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.deps
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.vapi

#---------------------------------------------------------------------------

%package guestfsd
Summary:	GuestFS daemon
Group:		Development/Tools
Requires:	%{name} = %{EVRD}

%description guestfsd
GuestFS daemon

%files guestfsd
/lib/udev/rules.d/99-guestfs-serial.rules
%{_sbindir}/guestfsd
%{_mandir}/man8/*.8*
%libpackage guestfs 0
%libpackage guestfs-gobject-1.0 0

#---------------------------------------------------------------------------

%prep
%autosetup -p1
# OCaml 5: Pervasives removed
find . \( -name '*.ml' -o -name '*.mli' \) | xargs -r sed -i 's/Pervasives\./Stdlib./g'
. %{_sysconfdir}/profile.d/90java.sh
%configure \
	--enable-install-daemon \
--disable-ruby \
--disable-golang

%build
export AR=%{_bindir}/ar
export RANLIB=%{_bindir}/ranlib
if [ ! -x ./libtool ]; then
	ln -sf %{_bindir}/libtool ./libtool
fi
if [ ! -f build-aux/missing ]; then
	mkdir -p build-aux
	printf '#!/bin/sh\nexec "$@"\n' > build-aux/missing
	chmod +x build-aux/missing
fi
export LIBTOOL=%{_bindir}/libtool
export LIBRARY_PATH=%{_libdir}/ocaml${LIBRARY_PATH:+:$LIBRARY_PATH}
export LDFLAGS="-L%{_libdir}/ocaml $LDFLAGS"

# OCaml 5.5 C library names
find . -type f \( -name 'Makefile' -o -name 'Makefile.in' -o -name 'config.status' \) -print0 | \
	xargs -0 -r perl -i -pe '
		s/(?<![\w])-lcamlstr(?![\w])/-lcamlstrnat/g;
		s/(?<![\w])-lunix(?![\w])/-lunixnat/g;
		s/libcamlstr\.a/libcamlstrnat.a/g;
		s/libunix\.a/libunixnat.a/g;
	'

# Skip appliance: supermin+dnf5 cannot run in mock (absolute dnf path, -v flag)
if [ -f Makefile ]; then
	sed -i -E 's/([ \t])appliance([ \t]|$)/\1\2/g' Makefile || :
fi
%make_build AR=%{_bindir}/ar RANLIB=%{_bindir}/ranlib LIBTOOL=%{_bindir}/libtool
mkdir -p appliance
touch appliance/stamp-supermin

%install
%make_install
%find_lang libguestfs --all-name --with-man

# Python site-packages path varies by version
: > python-libguestfs.files
# After remove_libtool_files, .la is gone — never list it
find %{buildroot}%{_libdir}/python* \( -name 'guestfs.py' -o -name 'libguestfsmod*.so' -o -name 'guestfs*.pyc' -o -path '*/__pycache__/guestfs*' \) 2>/dev/null \
	| sed "s|%{buildroot}||" >> python-libguestfs.files || :
# dirs
find %{buildroot}%{_libdir}/python* -type d -path '*/site-packages/__pycache__' 2>/dev/null | while read d; do
	[ -n "$(ls -A "$d"/guestfs* 2>/dev/null)" ] && echo "%dir ${d#%{buildroot}}"
done >> python-libguestfs.files || :
sort -u -o python-libguestfs.files python-libguestfs.files
if [ ! -s python-libguestfs.files ]; then
	echo "%dir %{_datadir}" > python-libguestfs.files
fi
# Also drop any .la that slipped in
sed -i '/\.la$/d' python-libguestfs.files

# lua path varies by version
: > lua-libguestfs.files
find %{buildroot}%{_libdir}/lua -name 'guestfs.so' 2>/dev/null | sed "s|%{buildroot}||" >> lua-libguestfs.files || :
find %{buildroot}%{_datadir}/lua -name 'guestfs.lua' 2>/dev/null | sed "s|%{buildroot}||" >> lua-libguestfs.files || :
if [ ! -s lua-libguestfs.files ]; then
	# no lua bindings built
	echo "%dir %{_datadir}" > lua-libguestfs.files
fi

# Build dynamic file lists for optional paths that 1.48 may not install
# Dynamic lists: 1.48 layout differs; only package what was installed
: > guestfs-main-extra.files
# virt-* tools (may be absent if builder/tools not built)
if [ -d %{buildroot}%{_bindir} ]; then
	find %{buildroot}%{_bindir} -type f -name 'virt-*' | sed "s|%{buildroot}||" >> guestfs-main-extra.files
fi
# configs
for f in %{_sysconfdir}/virt-builder %{_sysconfdir}/xdg/virt-builder; do
	if [ -e "%{buildroot}$f" ]; then
		find "%{buildroot}$f" | sed "s|%{buildroot}||" | while read pth; do
			if [ -d "%{buildroot}$pth" ]; then echo "%dir $pth"; else echo "$pth"; fi
		done >> guestfs-main-extra.files
	fi
done
# guestfs appliance dir
if [ -d %{buildroot}%{_libdir}/guestfs ]; then
	echo "%dir %{_libdir}/guestfs" >> guestfs-main-extra.files
	find %{buildroot}%{_libdir}/guestfs -type f | sed "s|%{buildroot}||" >> guestfs-main-extra.files
fi
# bash completion + docs
if [ -d %{buildroot}%{_datadir}/bash-completion/completions ]; then
	echo "%dir %{_datadir}/bash-completion/completions" >> guestfs-main-extra.files
	find %{buildroot}%{_datadir}/bash-completion/completions -type f | sed "s|%{buildroot}||" >> guestfs-main-extra.files
fi
if [ -d %{buildroot}%{_datadir}/doc/libguestfs ]; then
	find %{buildroot}%{_datadir}/doc/libguestfs -type f | sed "s|%{buildroot}||" >> guestfs-main-extra.files
fi
if [ ! -s guestfs-main-extra.files ]; then
	echo "%dir %{_datadir}" >> guestfs-main-extra.files
fi
sed -i '/\.la$/d' guestfs-main-extra.files 2>/dev/null || :
sort -u -o guestfs-main-extra.files guestfs-main-extra.files

