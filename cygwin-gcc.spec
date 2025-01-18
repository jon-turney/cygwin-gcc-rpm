%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%global gcc_major 12
%global gcc_minor 4
%global gcc_micro 0
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 1

%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%undefine _auto_set_build_flags
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif

Name:           cygwin-gcc
Version:        %{gcc_major}.%{gcc_minor}.%{gcc_micro}
Release:        %{gcc_release}%{?dist}
Summary:        Cygwin GCC cross-compiler

License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions
Group:          Development/Languages
URL:            http://gcc.gnu.org

BuildRequires:  gcc gcc-c++
BuildRequires:  texinfo
BuildRequires:  cygwin32-filesystem
BuildRequires:  cygwin32-binutils
BuildRequires:  cygwin32-w32api-headers
BuildRequires:  cygwin32-w32api-runtime
BuildRequires:  cygwin32 >= 3.0.0
BuildRequires:  cygwin64-filesystem
BuildRequires:  cygwin64-binutils
BuildRequires:  cygwin64-w32api-headers
BuildRequires:  cygwin64-w32api-runtime
BuildRequires:  cygwin64 >= 3.0.0
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  libmpc-devel
BuildRequires:  libstdc++-static
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  isl-devel >= 0.15
%endif
BuildRequires:  zlib-devel
BuildRequires:  flex
BuildRequires:  gettext

Source0:        https://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.xz

# Cygwin patches
Patch1:		0001-Cygwin-use-SysV-ABI-on-x86_64.patch
Patch2:         0002-Cygwin-add-dummy-pthread-tsaware-and-large-address-a.patch
Patch3:         0003-Cygwin-handle-dllimport-properly-in-medium-model-V2.patch
Patch4:         0004-Cygwin-MinGW-skip-test.patch
Patch5:		0005-Cygwin-define-RTS_CONTROL_ENABLE-and-DTR_CONTROL_ENA.patch
Patch6:         0006-Cygwin-__cxa-atexit.patch
Patch7:         0007-Cygwin-libgomp-soname.patch
Patch8:         0008-Cygwin-g-time.patch
Patch9:         0009-Cygwin-newlib-ftm.patch
Patch10:        0010-Cygwin-define-STD_UNIX.patch
Patch11:	0011-gcc-honour-ffile-prefix-map-in-ASM_MAP-PR93371.patch
Patch12:	0012-Always-define-WIN32_LEAN_AND_MEAN-before-windows.h.patch

# Fedora-specific patches
Patch1001:      1001-textdomain.patch
Patch1002:      1002-cygwin-ld-flags.patch
Patch1003:	1003-no-format-security.patch

# Upstream patches
#Patch2001:      pr47030.patch

%description
Cygwin cross-compiler (GCC) suite.


%package common
Summary: Common data for Cygwin cross-compilers
Group:   Development/Languages

%description common
%{summary}.

%package -n cygwin32-gcc
Summary: Cygwin cross-compiler for C
Group:   Development/Languages
# NB: Explicit cygwin32-filesystem dependency is REQUIRED here.
Requires:       cygwin32-filesystem
Requires:       cygwin32-binutils
Requires:       cygwin32-default-manifest
Requires:       cygwin32-w32api-runtime
Requires:       cygwin32 >= 3.0.0
Requires:       cygwin32-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:       cygwin32(cygatomic-1.dll)
Provides:       cygwin32(cyggcc_s-1.dll)
Provides:       cygwin32(cyggomp-1.dll)
Provides:       cygwin32(cygquadmath-0.dll)
# prevent update errors
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      cygwin32-gcc-java < %{version}-%{release}
Obsoletes:      cygwin32-gcc-gnat < %{version}-%{release}
Obsoletes:      cygwin32-gcc-objc < %{version}-%{release}
Obsoletes:      cygwin32-gcc-objc++ < %{version}-%{release}


%description -n cygwin32-gcc
Cygwin i686 cross-compiler (GCC) for C.


%package -n cygwin32-cpp
Summary:   Cygwin cross-C Preprocessor
Group:     Development/Languages
Requires:  %{name}-common = %{version}-%{release}

%description -n cygwin32-cpp
Cygwin cross-C Preprocessor


%package -n cygwin32-gcc-c++
Summary: Cygwin cross-compiler for C++
Group: Development/Languages
Requires: cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin32(cygstdc++-6.dll)

%description -n cygwin32-gcc-c++
Cygwin cross-compiler for C++.


%package -n cygwin32-gcc-gfortran
Summary: Cygwin cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin32(cyggfortran-5.dll)

%description -n cygwin32-gcc-gfortran
Cygwin cross-compiler for FORTRAN.


%package -n cygwin64-gcc
Summary: Cygwin64 cross-compiler for C
Group:   Development/Languages
# NB: Explicit cygwin-filesystem dependency is REQUIRED here.
Requires:       cygwin64-filesystem
Requires:       cygwin64-binutils
Requires:       cygwin64-default-manifest
Requires:       cygwin64-w32api-runtime
Requires:       cygwin64 >= 3.0.0
Requires:       cygwin64-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLLs:
Provides:       cygwin64(cygatomic-1.dll)
Provides:       cygwin64(cyggcc_s-seh-1.dll)
Provides:       cygwin64(cyggomp-1.dll)
Provides:       cygwin64(cygquadmath-0.dll)
# prevent update errors
Obsoletes:      cygwin64-gcc-gnat < %{version}-%{release}
Obsoletes:      cygwin64-gcc-objc < %{version}-%{release}
Obsoletes:      cygwin64-gcc-objc++ < %{version}-%{release}


%description -n cygwin64-gcc
Cygwin x86_64 cross-compiler (GCC) for C.

%package -n cygwin64-cpp
Summary:   Cygwin64 cross-C Preprocessor
Group:     Development/Languages
Requires:  %{name}-common = %{version}-%{release}

%description -n cygwin64-cpp
Cygwin x86_64 cross-C Preprocessor


%package -n cygwin64-gcc-c++
Summary: Cygwin64 cross-compiler for C++
Group: Development/Languages
Requires: cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin64(cygstdc++-6.dll)

%description -n cygwin64-gcc-c++
Cygwin x86_64 cross-compiler for C++.


%package -n cygwin64-gcc-gfortran
Summary: Cygwin64 cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin64(cyggfortran-5.dll)

%description -n cygwin64-gcc-gfortran
Cygwin x86_64 cross-compiler for FORTRAN.


%prep
%autosetup -n gcc-%{version} -p1

echo 'Fedora Cygwin %{version}-%{gcc_release}' > gcc/DEV-PHASE


%build
# use built-in SSP with Cygwin 2.10
# FIXME: --disable-libssp should suffice in GCC 8
export gcc_cv_libc_provides_ssp=yes
# configure tries to test SUSv4-compliant behaviour of
# realpath(..., NULL) via _XOPEN_VERSION
export glibcxx_cv_realpath=yes

mkdir -p build_32bit
pushd build_32bit

CC="%{__cc} ${RPM_OPT_FLAGS}" \
../configure \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --build=%_build --host=%_host \
  --target=%{cygwin32_target} \
  --with-arch=i686 --with-tune=generic \
  --with-gnu-as --with-gnu-ld --verbose \
  --enable-linker-build-id \
  --disable-multilib \
  --with-system-zlib \
  --enable-shared --enable-shared-libgcc --enable-static \
  --without-included-gettext \
  --disable-win32-registry \
  --enable-threads=posix \
  --enable-version-specific-runtime-libs \
  --with-gcc-major-version-only \
  --with-sysroot=%{cygwin32_sysroot} \
  --enable-shared --enable-shared-libgcc --enable-__cxa_atexit \
  --with-dwarf2 --disable-sjlj-exceptions \
%if 0%{?fedora} || 0%{?rhel} >= 8
  --enable-graphite \
%endif
  --enable-languages="c,c++,fortran,lto" \
  --disable-libcc1 \
  --enable-lto \
  --disable-symvers \
  --enable-libatomic \
  --enable-libgomp \
  --disable-libssp \
  --enable-libquadmath --enable-libquadmath-support \
  --enable-libstdcxx-filesystem-ts \
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_major}/%{cygwin32_target}/python \
  --with-bugurl=https://copr.fedorainfracloud.org/coprs/yselkowitz/cygwin/
popd

mkdir -p build_64bit
pushd build_64bit

CC="%{__cc} ${RPM_OPT_FLAGS}" \
../configure \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --build=%_build --host=%_host \
  --target=%{cygwin64_target} \
  --with-tune=generic \
  --with-gnu-as --with-gnu-ld --verbose \
  --enable-linker-build-id \
  --disable-multilib \
  --with-system-zlib \
  --enable-shared --enable-shared-libgcc --enable-static \
  --without-included-gettext \
  --disable-win32-registry \
  --enable-threads=posix \
  --enable-version-specific-runtime-libs \
  --with-gcc-major-version-only \
  --with-sysroot=%{cygwin64_sysroot} \
  --enable-shared --enable-shared-libgcc --enable-__cxa_atexit \
  --with-dwarf2 \
%if 0%{?fedora} || 0%{?rhel} >= 8
  --enable-graphite \
%endif
  --enable-languages="c,c++,fortran,lto" \
  --disable-libcc1 \
  --enable-lto \
  --disable-symvers \
  --enable-libatomic \
  --enable-libgomp \
  --disable-libssp \
  --enable-libquadmath --enable-libquadmath-support \
  --enable-libstdcxx-filesystem-ts \
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_major}/%{cygwin64_target}/python \
  --with-bugurl=https://copr.fedorainfracloud.org/coprs/yselkowitz/cygwin/

popd

%cygwin_make %{?_smp_mflags} all


%install
%cygwin_make_install DESTDIR=$RPM_BUILD_ROOT

# These files conflict with existing installed files.
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty*
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/*

# This file is provided by cygwin*-libbfd
rm -f $RPM_BUILD_ROOT%{_prefix}/%{cygwin32_target}/lib/libiberty.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{cygwin64_target}/lib/libiberty.a

mkdir -p $RPM_BUILD_ROOT/lib
ln -sf ..%{_prefix}/bin/%{cygwin32_target}-cpp \
  $RPM_BUILD_ROOT/lib/%{cygwin32_target}-cpp
ln -sf ..%{_prefix}/bin/%{cygwin64_target}-cpp \
  $RPM_BUILD_ROOT/lib/%{cygwin64_target}-cpp

# installation bug on multilib platforms
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/lib/libgcc_s.dll.a \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/

# clean-up include-fixed
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include-fixed/*limits.h \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include/
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include-fixed/*limits.h \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include-fixed/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include-fixed/

# This is a runtime plugin of libgomp, not a link library
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/gcc/*/%{gcc_major}/libgomp-plugin-host_nonshm.dll.a

# libtool installs DLL files of runtime libraries into $(libdir)/../bin,
# but we need them in cygwin*_bindir.
mkdir -p $RPM_BUILD_ROOT%{cygwin32_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/*.dll \
  $RPM_BUILD_ROOT%{cygwin32_bindir}
mkdir -p $RPM_BUILD_ROOT%{cygwin64_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/*.dll \
  $RPM_BUILD_ROOT%{cygwin64_bindir}

# Don't want the *.la files.
find $RPM_BUILD_ROOT -name '*.la' -delete



%find_lang cygwin-gcc
%find_lang cygwin-cpplib
cat cygwin-cpplib.lang >> cygwin-gcc.lang


%files common -f cygwin-gcc.lang
%doc gcc/README* gcc/COPYING*


%files -n cygwin32-gcc
%{_bindir}/%{cygwin32_target}-gcc
%{_bindir}/%{cygwin32_target}-gcc-%{gcc_major}
%{_bindir}/%{cygwin32_target}-gcc-ar
%{_bindir}/%{cygwin32_target}-gcc-nm
%{_bindir}/%{cygwin32_target}-gcc-ranlib
%{_bindir}/%{cygwin32_target}-gcov
%{_bindir}/%{cygwin32_target}-gcov-dump
%{_bindir}/%{cygwin32_target}-gcov-tool
%{_bindir}/%{cygwin32_target}-lto-dump
%{_mandir}/man1/%{cygwin32_target}-gcc.1*
%{_mandir}/man1/%{cygwin32_target}-gcov.1*
%{_mandir}/man1/%{cygwin32_target}-gcov-dump.1*
%{_mandir}/man1/%{cygwin32_target}-gcov-tool.1*
%{_mandir}/man1/%{cygwin32_target}-lto-dump.1*
%dir %{_prefix}/lib/gcc/%{cygwin32_target}
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/crtbegin.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/crtbeginS.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/crtend.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/crtfastmath.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libatomic.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libquadmath.dll.a
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include/*.h
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/install-tools/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/plugin/
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/install-tools/
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/liblto_plugin.so
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/lto1
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/plugin/
%dir %{_datadir}/gcc-%{gcc_major}
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}
%{cygwin32_bindir}/cygatomic-1.dll
%{cygwin32_bindir}/cyggcc_s-1.dll
%{cygwin32_bindir}/cyggomp-1.dll
%{cygwin32_bindir}/cygquadmath-0.dll


%files -n cygwin32-cpp
/lib/%{cygwin32_target}-cpp
%{_bindir}/%{cygwin32_target}-cpp
%{_mandir}/man1/%{cygwin32_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{cygwin32_target}
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/cc1


%files -n cygwin32-gcc-c++
%{_bindir}/%{cygwin32_target}-g++
%{_bindir}/%{cygwin32_target}-c++
%{_mandir}/man1/%{cygwin32_target}-g++.1*
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/cc1plus
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/collect2
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include/c++/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}/python
%{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}/python/libstdcxx/
%{cygwin32_bindir}/cygstdc++-6.dll


%files -n cygwin32-gcc-gfortran
%{_bindir}/%{cygwin32_target}-gfortran
%{_mandir}/man1/%{cygwin32_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/f951
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/finclude/
%{cygwin32_bindir}/cyggfortran-5.dll


%files -n cygwin64-gcc
%{_bindir}/%{cygwin64_target}-gcc
%{_bindir}/%{cygwin64_target}-gcc-%{gcc_major}
%{_bindir}/%{cygwin64_target}-gcc-ar
%{_bindir}/%{cygwin64_target}-gcc-nm
%{_bindir}/%{cygwin64_target}-gcc-ranlib
%{_bindir}/%{cygwin64_target}-gcov
%{_bindir}/%{cygwin64_target}-gcov-dump
%{_bindir}/%{cygwin64_target}-gcov-tool
%{_bindir}/%{cygwin64_target}-lto-dump
%{_mandir}/man1/%{cygwin64_target}-gcc.1*
%{_mandir}/man1/%{cygwin64_target}-gcov.1*
%{_mandir}/man1/%{cygwin64_target}-gcov-dump.1*
%{_mandir}/man1/%{cygwin64_target}-gcov-tool.1*
%{_mandir}/man1/%{cygwin64_target}-lto-dump.1*
%dir %{_prefix}/lib/gcc/%{cygwin64_target}
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/crtbegin.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/crtbeginS.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/crtend.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/crtfastmath.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libatomic.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libquadmath.dll.a
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include/*.h
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/install-tools/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/plugin/
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/install-tools/
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/liblto_plugin.so
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/lto1
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/plugin/
%dir %{_datadir}/gcc-%{gcc_major}
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}
%{cygwin64_bindir}/cygatomic-1.dll
%{cygwin64_bindir}/cyggcc_s-seh-1.dll
%{cygwin64_bindir}/cyggomp-1.dll
%{cygwin64_bindir}/cygquadmath-0.dll


%files -n cygwin64-cpp
/lib/%{cygwin64_target}-cpp
%{_bindir}/%{cygwin64_target}-cpp
%{_mandir}/man1/%{cygwin64_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{cygwin64_target}
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/cc1


%files -n cygwin64-gcc-c++
%{_bindir}/%{cygwin64_target}-g++
%{_bindir}/%{cygwin64_target}-c++
%{_mandir}/man1/%{cygwin64_target}-g++.1*
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/cc1plus
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/collect2
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include/c++/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}/python
%{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}/python/libstdcxx/
%{cygwin64_bindir}/cygstdc++-6.dll


%files -n cygwin64-gcc-gfortran
%{_bindir}/%{cygwin64_target}-gfortran
%{_mandir}/man1/%{cygwin64_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/f951
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/finclude/
%{cygwin64_bindir}/cyggfortran-5.dll


%changelog
* Tue Oct 19 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 11.2.0-2
- Disable dynamicbase by default in DLLs

* Thu Sep 02 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 11.2.0-1
- new version

* Wed Apr 01 2020 Yaakov Selkowitz <yselkowi@redhat.com> - 9.3.0-1
- new version

* Sun Dec 30 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 7.4.0-1
- new version
- Add patch for PR fortran/47030

* Thu Jul 12 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 7.3.0-2
- Add patch for PR libstdc++/86138

* Tue Jun 05 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 7.3.0-1
- new version
- Enable libstdc++ Filesystem TS

* Tue Dec 05 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4.0-2
- Use built-in SSP in Cygwin 2.10
- Fix definition of unix macro

* Thu Nov 16 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4.0-1
- new version
- Disable cilk, libvtv.

* Thu Aug 25 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 5.4.0-2
- Disable _GNU_SOURCE patch to match native compilers

* Fri Jun 24 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 5.4.0-1
- new version

* Wed Mar 30 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.0-3
- Fix build with GCC 6 (PR69959)

* Thu Feb 25 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.0-2
- Fix link order of w32api

* Sun Feb 21 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.0-1
- new version
- Enable libcilkrts, libitm, libvtv

* Fri Aug 14 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 4.9.3-1
- Update to 4.9.3

* Fri Jun 19 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 4.9.2-1
- Update to 4.9.2
- Build cygwin32-gcc and cygwin64-gcc from single SRPM

* Sun Nov 02 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.8.3-6
- Fix optimization issue in crtbeginS.o.

* Mon Aug 11 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.8.3-5
- Separate Win32 patch for __cxa_thread_atexit.

* Thu Aug 07 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.8.3-4
- Build with --enable-__cxa_atexit

* Wed Jul 30 2014 Yaakov Selkowitz <yselkowitz@cygwin.com> - 4.8.3-3
- Use %%{_prefix}/lib/gcc instead of %%{_libdir}/gcc
- Cleanup spec

* Fri Jul 25 2014 Yaakov Selkowitz <yselkowitz@cygwin.com> - 4.8.3-2
- Add patch to fix libgcc deregistration on x86

* Tue Jun 10 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.8.3-1
- Version bump.
- Remove java support (dropped from F21/EL7).
- Added patch to support default manifest.

* Tue Jan 21 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.8.2-2
- Fix 64-bit builtin types for i686-cygwin target.

* Sun Jan 19 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.8.2-1
- Version bump.
- Enable Ada on systems with native gcc-gnat-4.8.x.
- Enable NLS without colliding with native gcc.

* Thu Jun 27 2013 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.7.3-1
- Version bump.
- Update for new Cygwin packaging scheme.

* Sun Aug 14 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.3-4
- Add .exe to unsuffixed output executables, as with the native compiler.

* Wed Aug 10 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.3-3
- Enable --large-address-aware for executables by default.
- Re-enable java subpackage.

* Mon Jul 04 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.3-2
- Rebuilt for http://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 26 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.3-1
- Version bump.

* Sun Mar 13 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.1-2
- Ship libiberty.a from cygwin-binutils-devel instead of cygwin-gcc.

* Thu Feb 17 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.1-1
- Match native gcc version to resolve ecj1 dependency on libgcj.

* Wed Feb 16 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 4.5.2-1
- Initial RPM release, largely based on mingw32-gcc.
