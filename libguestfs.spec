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
Version:	1.41.8
Release:	1
Source0:	https://download.libguestfs.org/%(echo %{version}|cut -d. -f1-2)-development/libguestfs-%{version}.tar.gz
Group:		System/Libraries
License:	LGPLv2.1/GPLv2
BuildRequires:	pkgconfig(jansson) >= 2.7
BuildRequires:	pkgconfig(libmagic)
BuildRequires:	pkgconfig(libvirt)
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(hivex)
BuildRequires:	jdk-current
BuildRequires:	golang
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ruby)
BuildRequires:	ruby-hivex
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
BuildRequires:	qemu
BuildRequires:	ocaml
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

%package -n %{devname}
Summary:	Development files for libguestfs
Group:		Development/C and C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for libguestfs

%package -n %{gdevname}
Summary:	GObject bindings to libguestfs
Group:		Development/C and C++
Requires:	%{glibname} = %{EVRD}

%description -n %{gdevname}
GObject bindings to libguestfs

%package -n go-libguestfs
Summary:	Go bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n go-libguestfs
Go bindings for libguestfs

%package -n java-libguestfs
Summary:	Java bindings for libguestfs
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description -n java-libguestfs
Java bindings for libguestfs

%package -n lua-libguestfs
Summary:	Lua bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n lua-libguestfs
Lua bindings for libguestfs

%package -n ocaml-libguestfs
Summary:	Objective-CAML bindings for libguestfs
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description -n ocaml-libguestfs
Objective-CAML bindings for libguestfs

%package -n python-libguestfs
Summary:	Python bindings for libguestfs
Group:		Development/Go
Requires:	%{libname} = %{EVRD}

%description -n python-libguestfs
Python bindings for libguestfs

%package -n ruby-libguestfs
Summary:	Ruby bindings for libguestfs
Group:		Development/Ruby
Requires:	%{libname} = %{EVRD}

%description -n ruby-libguestfs
Ruby bindings for libguestfs

%package -n vala-libguestfs
Summary:	Vala bindings for libguestfs
Group:		Development/Vala
Requires:	%{libname} = %{EVRD}

%description -n vala-libguestfs
Vala bindings for libguestfs

%package guestfsd
Summary:	GuestFS daemon
Group:		Development/Tools
Requires:	%{name} = %{EVRD}

%description guestfsd
GuestFS daemon

%prep
%autosetup -p1
. %{_sysconfdir}/profile.d/90java.sh
%configure \
	--enable-install-daemon

%build
%make_build

%install
%make_install
%find_lang libguestfs --all-name --with-man

%files -f libguestfs.lang
%config %{_sysconfdir}/libguestfs-tools.conf
%config %{_sysconfdir}/virt-builder
%dir %{_sysconfdir}/xdg/virt-builder
%dir %{_sysconfdir}/xdg/virt-builder/repos.d
%config %{_sysconfdir}/xdg/virt-builder/repos.d/libguestfs.conf
%config %{_sysconfdir}/xdg/virt-builder/repos.d/libguestfs.gpg
%config %{_sysconfdir}/xdg/virt-builder/repos.d/opensuse.conf
%config %{_sysconfdir}/xdg/virt-builder/repos.d/opensuse.gpg
%{_bindir}/guestfish
%{_bindir}/guestmount
%{_bindir}/guestunmount
%{_bindir}/libguestfs-test-tool
%{_bindir}/virt-alignment-scan
%{_bindir}/virt-builder
%{_bindir}/virt-builder-repository
%{_bindir}/virt-cat
%{_bindir}/virt-copy-in
%{_bindir}/virt-copy-out
%{_bindir}/virt-customize
%{_bindir}/virt-df
%{_bindir}/virt-dib
%{_bindir}/virt-diff
%{_bindir}/virt-edit
%{_bindir}/virt-filesystems
%{_bindir}/virt-format
%{_bindir}/virt-get-kernel
%{_bindir}/virt-index-validate
%{_bindir}/virt-inspector
%{_bindir}/virt-log
%{_bindir}/virt-ls
%{_bindir}/virt-make-fs
%{_bindir}/virt-rescue
%{_bindir}/virt-resize
%{_bindir}/virt-sparsify
%{_bindir}/virt-sysprep
%{_bindir}/virt-tail
%{_bindir}/virt-tar-in
%{_bindir}/virt-tar-out
%dir %{_libdir}/guestfs
%dir %{_libdir}/guestfs/supermin.d
%{_libdir}/guestfs/supermin.d/base.tar.gz
%{_libdir}/guestfs/supermin.d/daemon.tar.gz
%{_libdir}/guestfs/supermin.d/excludefiles
%{_libdir}/guestfs/supermin.d/hostfiles
%{_libdir}/guestfs/supermin.d/init.tar.gz
%{_libdir}/guestfs/supermin.d/packages
%{_libdir}/guestfs/supermin.d/udev-rules.tar.gz
%{_sbindir}/libguestfs-make-fixed-appliance
%{_datadir}/bash-completion/completions/guestfish
%{_datadir}/bash-completion/completions/guestmount
%{_datadir}/bash-completion/completions/guestunmount
%{_datadir}/bash-completion/completions/libguestfs-test-tool
%{_datadir}/bash-completion/completions/virt-alignment-scan
%{_datadir}/bash-completion/completions/virt-builder
%{_datadir}/bash-completion/completions/virt-cat
%{_datadir}/bash-completion/completions/virt-copy-in
%{_datadir}/bash-completion/completions/virt-copy-out
%{_datadir}/bash-completion/completions/virt-customize
%{_datadir}/bash-completion/completions/virt-df
%{_datadir}/bash-completion/completions/virt-dib
%{_datadir}/bash-completion/completions/virt-diff
%{_datadir}/bash-completion/completions/virt-edit
%{_datadir}/bash-completion/completions/virt-filesystems
%{_datadir}/bash-completion/completions/virt-format
%{_datadir}/bash-completion/completions/virt-get-kernel
%{_datadir}/bash-completion/completions/virt-inspector
%{_datadir}/bash-completion/completions/virt-log
%{_datadir}/bash-completion/completions/virt-ls
%{_datadir}/bash-completion/completions/virt-rescue
%{_datadir}/bash-completion/completions/virt-resize
%{_datadir}/bash-completion/completions/virt-sparsify
%{_datadir}/bash-completion/completions/virt-sysprep
%{_datadir}/bash-completion/completions/virt-tail
%{_datadir}/bash-completion/completions/virt-tar-in
%{_datadir}/bash-completion/completions/virt-tar-out
%{_datadir}/bash-completion/completions/virt-win-reg
%{_datadir}/doc/libguestfs/example-debian.xml
%{_datadir}/doc/libguestfs/example-fedora.xml
%{_datadir}/doc/libguestfs/example-rhel-6.xml
%{_datadir}/doc/libguestfs/example-ubuntu.xml
%{_datadir}/doc/libguestfs/example-windows.xml
%{_datadir}/doc/libguestfs/virt-inspector.rng
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files guestfsd
/lib/udev/rules.d/99-guestfs-serial.rules
%{_sbindir}/guestfsd
%{_mandir}/man8/*.8*

%libpackage guestfs 0

%libpackage guestfs-gobject-1.0 0

%files -n %{devname}
%{_includedir}/guestfs.h
%{_libdir}/libguestfs.so
%{_mandir}/man3/*.3*
%{_libdir}/pkgconfig/libguestfs.pc

%files -n %{gdevname}
%{_includedir}/guestfs-gobject.h
%{_includedir}/guestfs-gobject
%{_libdir}/libguestfs-gobject-1.0.so
%{_libdir}/pkgconfig/libguestfs-gobject-1.0.pc
%{_datadir}/gir-1.0/Guestfs-1.0.gir
%{_libdir}/girepository-1.0/Guestfs-1.0.typelib

%files -n go-libguestfs
%{_prefix}/lib/golang/pkg/*/libguestfs.org/guestfs
%{_prefix}/lib/golang/src/pkg/libguestfs.org/guestfs

%files -n java-libguestfs
%{_datadir}/java/libguestfs-%{version}.jar
%{_datadir}/javadoc/libguestfs
%{_libdir}/libguestfs_jni.so*

%files -n lua-libguestfs
%{_libdir}/lua/5.3/guestfs.so

%files -n ocaml-libguestfs
%{_libdir}/ocaml/guestfs
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner

%files -n python-libguestfs
%{_libdir}/python3.8/site-packages/__pycache__/guestfs.*.pyc
%{_libdir}/python3.8/site-packages/guestfs.py
%{_libdir}/python3.8/site-packages/libguestfsmod.*.so

%files -n ruby-libguestfs
%{_datadir}/ruby/site_ruby/*/guestfs.rb
%{_libdir}/ruby/site_ruby/_guestfs.so

%files -n vala-libguestfs
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.deps
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.vapi
