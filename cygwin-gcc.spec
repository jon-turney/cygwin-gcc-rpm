%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%global gcc_version 7.4.0
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 1

%global build_ada 0
%global build_objc 0
%global build_vtv 0

Name:           cygwin-gcc
Version:        %{gcc_version}
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
BuildRequires:  cygwin32 >= 2.10.0
BuildRequires:  cygwin64-filesystem
BuildRequires:  cygwin64-binutils
BuildRequires:  cygwin64-w32api-headers
BuildRequires:  cygwin64-w32api-runtime
BuildRequires:  cygwin64 >= 2.10.0
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  libmpc-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  libstdc++-static
%endif
%if 0%{?fedora}
BuildRequires:  isl-devel >= 0.14
%endif
BuildRequires:  zlib-devel
BuildRequires:  flex
BuildRequires:  gettext
%if %{build_ada}
BuildRequires:  gcc-gnat
%endif

Source0:        ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.xz

# Cygwin patches
Patch1:         0001-share-mingw-fset-stack-executable-with-cygwin.patch
#Patch2:         0002-boehm-gc-for-cygwin.patch
Patch7:         0007-Avoid-installing-libffi-V2.patch
#Patch8:         0008-libitm-libtool-fixes-for-Cygwin.patch
Patch9:         0009-Cygwin-uses-sysv-ABI-on-x86_64-V2.patch
Patch10:        0010-Do-not-version-lto-plugin-on-cygwin-mingw.patch
Patch11:        0011-add-dummy-pthread-tsaware-and-large-address-aware-fo.patch
Patch12:        0012-handle-dllimport-properly-in-medium-model-V2.patch
Patch13:        0013-skip-test-for-cygwin-mingw.patch
Patch14:        0014-64bit-Cygwin-uses-SEH.patch
Patch15:        0015-define-RTS_CONTROL_ENABLE-and-DTR_CONTROL_ENABLE-for.patch
Patch16:        0016-fix-some-implicit-declaration-warnings.patch
Patch17:        0017-__cxa-atexit-for-Cygwin.patch
Patch18:        0018-prevent-modules-from-being-unloaded-before-their-dto.patch
Patch20:        0020-cygwin-uses-cyg-lib-prefix-v3.patch
Patch22:        0022-libgomp-soname-cygwin-mingw.patch
#Patch23:        0023-glibcxx-use-c99.patch
Patch24:        0024-libitm-weak-symbols.patch
#Patch26:        0026-g++-gnu-source.patch
Patch28:        0028-g++-time.patch
Patch30:        0030-newlib-ftm.patch
Patch31:        0031-define_std-unix.patch

# Fedora-specific patches
Patch1000:      1000-cross-exe-suffix.patch
Patch1001:      1001-textdomain.patch

# Upstream patches
Patch2001:      pr47030.patch

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
Requires:       cygwin32 >= 2.10.0
Requires:       cygwin32-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:       cygwin32(cygatomic-1.dll)
Provides:       cygwin32(cyggcc_s-1.dll)
Provides:       cygwin32(cyggomp-1.dll)
Provides:       cygwin32(cygquadmath-0.dll)
%if %{build_vtv}
Provides:       cygwin32(cygvtv-0.dll)
Provides:       cygwin32(cygvtv_stubs-0.dll)
%endif
# prevent update errors
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      cygwin32-gcc-java < %{version}-%{release}
%if ! %{build_ada}
Obsoletes:      cygwin32-gcc-gnat < %{version}-%{release}
%endif
%if ! %{build_objc}
Obsoletes:      cygwin32-gcc-objc < %{version}-%{release}
Obsoletes:      cygwin32-gcc-objc++ < %{version}-%{release}
%endif


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


%package -n cygwin32-gcc-objc
Summary: Cygwin cross-compiler support for Objective C
Group: Development/Languages
Requires: cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin32(cygobjc-4.dll)

%description -n cygwin32-gcc-objc
Cygwin cross-compiler support for Objective C.


%package -n cygwin32-gcc-objc++
Summary: Cygwin cross-compiler support for Objective C++
Group: Development/Languages
Requires:  cygwin32-gcc-c++ = %{version}-%{release}
Requires:  cygwin32-gcc-objc = %{version}-%{release}

%description -n cygwin32-gcc-objc++
Cygwin cross-compiler support for Objective C++.


%package -n cygwin32-gcc-gfortran
Summary: Cygwin cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin32(cyggfortran-4.dll)

%description -n cygwin32-gcc-gfortran
Cygwin cross-compiler for FORTRAN.


%package -n cygwin32-gcc-gnat
Summary: Cygwin cross-compiler for Ada
Group: Development/Languages
Requires:  cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
# (shared libgnat doesn't work quite right, nor does it cross-build
#Provides: cygwin32(cyggnat-7.dll)
#Provides: cygwin32(cyggnarl-7.dll)

%description -n cygwin32-gcc-gnat
Cygwin cross-compiler for Ada.

%package -n cygwin64-gcc
Summary: Cygwin64 cross-compiler for C
Group:   Development/Languages
# NB: Explicit cygwin-filesystem dependency is REQUIRED here.
Requires:       cygwin64-filesystem
Requires:       cygwin64-binutils
Requires:       cygwin64-default-manifest
Requires:       cygwin64-w32api-runtime
Requires:       cygwin64 >= 2.10.0
Requires:       cygwin64-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLLs:
Provides:       cygwin64(cygatomic-1.dll)
Provides:       cygwin64(cyggcc_s-seh-1.dll)
Provides:       cygwin64(cyggomp-1.dll)
Provides:       cygwin64(cygquadmath-0.dll)
%if %{build_vtv}
Provides:       cygwin64(cygvtv-0.dll)
Provides:       cygwin64(cygvtv_stubs-0.dll)
%endif
# prevent update errors
%if ! %{build_ada}
Obsoletes:      cygwin64-gcc-gnat < %{version}-%{release}
%endif
%if ! %{build_objc}
Obsoletes:      cygwin64-gcc-objc < %{version}-%{release}
Obsoletes:      cygwin64-gcc-objc++ < %{version}-%{release}
%endif


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


%package -n cygwin64-gcc-objc
Summary: Cygwin64 cross-compiler support for Objective C
Group: Development/Languages
Requires: cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin64(cygobjc-4.dll)

%description -n cygwin64-gcc-objc
Cygwin x86_64 cross-compiler support for Objective C.


%package -n cygwin64-gcc-objc++
Summary: Cygwin64 cross-compiler support for Objective C++
Group: Development/Languages
Requires:  cygwin64-gcc-c++ = %{version}-%{release}
Requires:  cygwin64-gcc-objc = %{version}-%{release}

%description -n cygwin64-gcc-objc++
Cygwin x86_64 cross-compiler support for Objective C++.


%package -n cygwin64-gcc-gfortran
Summary: Cygwin64 cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides:  cygwin64(cyggfortran-4.dll)

%description -n cygwin64-gcc-gfortran
Cygwin x86_64 cross-compiler for FORTRAN.


%package -n cygwin64-gcc-gnat
Summary: Cygwin64 cross-compiler for Ada
Group: Development/Languages
Requires:  cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
# (shared libgnat doesn't work quite right, nor does it cross-build
#Provides: cygwin64(cyggnat-7.dll)
#Provides: cygwin64(cyggnarl-7.dll)

%description -n cygwin64-gcc-gnat
Cygwin x86_64 cross-compiler for Ada.


%prep
%setup -q -n gcc-%{gcc_version}
%patch1 -p1
#patch2 -p1
%patch7 -p1
#patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch20 -p1
%patch22 -p1
#patch23 -p2
%patch24 -p1
#patch26 -p2
%patch28 -p2
%patch30 -p2
%patch31 -p2

%patch1000 -p1
%patch1001 -p1

%patch2001 -p2

echo %{gcc_version} > gcc/BASE-VER
echo 'Fedora Cygwin %{gcc_version}-%{gcc_release}' > gcc/DEV-PHASE


%build
# use built-in SSP with Cygwin 2.10
# FIXME: --disable-libssp should suffice in GCC 8
export gcc_cv_libc_provides_ssp=yes
# configure tries to test SUSv4-compliant behaviour of
# realpath(..., NULL) via _XOPEN_VERSION
export glibcxx_cv_realpath=yes

mkdir -p build_32bit
pushd build_32bit

%if %{build_ada}
enablelada=,ada
%endif
%if %{build_objc}
enablelobjc=,objc,obj-c++
%endif

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
  --with-sysroot=%{cygwin32_sysroot} \
  --enable-shared --enable-shared-libgcc --enable-__cxa_atexit \
  --with-dwarf2 --disable-sjlj-exceptions \
%if 0%{?fedora}
  --enable-graphite \
%endif
  --enable-languages="c,c++,fortran,lto${enablelada}${enablelobjc}" \
  --disable-libcc1 \
  --enable-lto \
  --disable-symvers \
  --enable-libatomic \
  --enable-libgomp \
  --enable-libitm \
  --disable-libssp \
  --enable-libquadmath --enable-libquadmath-support \
  --enable-libstdcxx-filesystem-ts \
%if %{build_vtv}
  --enable-vtable-verify \
%endif
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_version}/%{cygwin32_target}/python \
%if %{build_ada}
  --enable-libada \
%endif
  --with-bugurl=http://cygwinports.org
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
  --with-sysroot=%{cygwin64_sysroot} \
  --enable-shared --enable-shared-libgcc --enable-__cxa_atexit \
  --with-dwarf2 \
%if 0%{?fedora}
  --enable-graphite \
%endif
  --enable-languages="c,c++,fortran,lto${enablelada}${enablelobjc}" \
  --disable-libcc1 \
  --enable-lto \
  --disable-symvers \
  --enable-libatomic \
  --enable-libgomp \
  --enable-libitm \
  --disable-libssp \
  --enable-libquadmath --enable-libquadmath-support \
  --enable-libstdcxx-filesystem-ts \
%if %{build_vtv}
  --enable-vtable-verify \
%endif
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_version}/%{cygwin64_target}/python \
%if %{build_ada}
  --enable-libada \
%endif
  --with-bugurl=http://cygwinports.org

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
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_version}/

# clean-up include-fixed
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_version}/include-fixed/*limits.h \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_version}/include/
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_version}/include-fixed/*limits.h \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_version}/include/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_version}/include-fixed/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_version}/include-fixed/

# This is a runtime plugin of libgomp, not a link library
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/gcc/*/%{version}/libgomp-plugin-host_nonshm.dll.a

# libtool installs DLL files of runtime libraries into $(libdir)/../bin,
# but we need them in cygwin*_bindir.
mkdir -p $RPM_BUILD_ROOT%{cygwin32_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_version}/*.dll \
  $RPM_BUILD_ROOT%{cygwin32_bindir}
mkdir -p $RPM_BUILD_ROOT%{cygwin64_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_version}/*.dll \
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
%{_bindir}/%{cygwin32_target}-gcc-%{version}
%{_bindir}/%{cygwin32_target}-gcc-ar
%{_bindir}/%{cygwin32_target}-gcc-nm
%{_bindir}/%{cygwin32_target}-gcc-ranlib
%{_bindir}/%{cygwin32_target}-gcov
%{_bindir}/%{cygwin32_target}-gcov-dump
%{_bindir}/%{cygwin32_target}-gcov-tool
%{_mandir}/man1/%{cygwin32_target}-gcc.1*
%{_mandir}/man1/%{cygwin32_target}-gcov.1*
%{_mandir}/man1/%{cygwin32_target}-gcov-dump.1*
%{_mandir}/man1/%{cygwin32_target}-gcov-tool.1*
%dir %{_prefix}/lib/gcc/%{cygwin32_target}
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{version}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/crtbegin.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/crtbeginS.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/crtend.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/crtfastmath.o
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libatomic.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgcc.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libitm.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libitm.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libquadmath.dll.a
%if %{build_vtv}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libvtv.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libvtv.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libvtv_stubs.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libvtv_stubs.dll.a
%endif
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/include
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/include/*.h
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/install-tools/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/plugin/
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/install-tools/
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/liblto_plugin.so
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/lto1
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/plugin/
%dir %{_datadir}/gcc-%{gcc_version}
%dir %{_datadir}/gcc-%{gcc_version}/%{cygwin32_target}
%{cygwin32_bindir}/cygatomic-1.dll
%{cygwin32_bindir}/cyggcc_s-1.dll
%{cygwin32_bindir}/cyggomp-1.dll
%{cygwin32_bindir}/cygquadmath-0.dll
%if %{build_vtv}
%{cygwin32_bindir}/cygvtv-0.dll
%{cygwin32_bindir}/cygvtv_stubs-0.dll
%endif


%files -n cygwin32-cpp
/lib/%{cygwin32_target}-cpp
%{_bindir}/%{cygwin32_target}-cpp
%{_mandir}/man1/%{cygwin32_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{cygwin32_target}
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{version}
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/cc1


%files -n cygwin32-gcc-c++
%{_bindir}/%{cygwin32_target}-g++
%{_bindir}/%{cygwin32_target}-c++
%{_mandir}/man1/%{cygwin32_target}-g++.1*
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/cc1plus
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/collect2
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/include/c++/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_version}/%{cygwin32_target}/python
%{_datadir}/gcc-%{gcc_version}/%{cygwin32_target}/python/libstdcxx/
%{cygwin32_bindir}/cygstdc++-6.dll


%if %{build_objc}
%files -n cygwin32-gcc-objc
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/cc1obj
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/include/objc/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libobjc.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libobjc.dll.a
%{cygwin32_bindir}/cygobjc-4.dll


%files -n cygwin32-gcc-objc++
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/cc1objplus
%endif


%files -n cygwin32-gcc-gfortran
%{_bindir}/%{cygwin32_target}-gfortran
%{_mandir}/man1/%{cygwin32_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/f951
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/libgfortran.spec
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/finclude
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/finclude/ieee_*
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/finclude/omp_lib*
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/finclude/openacc*
%{cygwin32_bindir}/cyggfortran-4.dll


%if %{build_ada}
%files -n cygwin32-gcc-gnat
%{_bindir}/%{cygwin32_target}-gnat*
#%%{_mandir}/man1/%%{cygwin32_target}-gnat*.1*
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/adainclude/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{version}/adalib/
%{_libexecdir}/gcc/%{cygwin32_target}/%{version}/gnat1
#%%{cygwin32_bindir}/cyggnarl-7.dll
#%%{cygwin32_bindir}/cyggnat-7.dll
%endif

%files -n cygwin64-gcc
%{_bindir}/%{cygwin64_target}-gcc
%{_bindir}/%{cygwin64_target}-gcc-%{version}
%{_bindir}/%{cygwin64_target}-gcc-ar
%{_bindir}/%{cygwin64_target}-gcc-nm
%{_bindir}/%{cygwin64_target}-gcc-ranlib
%{_bindir}/%{cygwin64_target}-gcov
%{_bindir}/%{cygwin64_target}-gcov-dump
%{_bindir}/%{cygwin64_target}-gcov-tool
%{_mandir}/man1/%{cygwin64_target}-gcc.1*
%{_mandir}/man1/%{cygwin64_target}-gcov.1*
%{_mandir}/man1/%{cygwin64_target}-gcov-dump.1*
%{_mandir}/man1/%{cygwin64_target}-gcov-tool.1*
%dir %{_prefix}/lib/gcc/%{cygwin64_target}
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{version}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/crtbegin.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/crtbeginS.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/crtend.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/crtfastmath.o
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libatomic.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgcc.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libitm.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libitm.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libquadmath.dll.a
%if %{build_vtv}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libvtv.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libvtv.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libvtv_stubs.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libvtv_stubs.dll.a
%endif
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/include
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/include/*.h
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/install-tools/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/plugin/
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/install-tools/
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/liblto_plugin.so
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/lto1
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/plugin/
%dir %{_datadir}/gcc-%{gcc_version}
%dir %{_datadir}/gcc-%{gcc_version}/%{cygwin64_target}
%{cygwin64_bindir}/cygatomic-1.dll
%{cygwin64_bindir}/cyggcc_s-seh-1.dll
%{cygwin64_bindir}/cyggomp-1.dll
%{cygwin64_bindir}/cygquadmath-0.dll
%if %{build_vtv}
%{cygwin64_bindir}/cygvtv-0.dll
%{cygwin64_bindir}/cygvtv_stubs-0.dll
%endif


%files -n cygwin64-cpp
/lib/%{cygwin64_target}-cpp
%{_bindir}/%{cygwin64_target}-cpp
%{_mandir}/man1/%{cygwin64_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{cygwin64_target}
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{version}
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/cc1


%files -n cygwin64-gcc-c++
%{_bindir}/%{cygwin64_target}-g++
%{_bindir}/%{cygwin64_target}-c++
%{_mandir}/man1/%{cygwin64_target}-g++.1*
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/cc1plus
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/collect2
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/include/c++/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_version}/%{cygwin64_target}/python
%{_datadir}/gcc-%{gcc_version}/%{cygwin64_target}/python/libstdcxx/
%{cygwin64_bindir}/cygstdc++-6.dll


%if %{build_objc}
%files -n cygwin64-gcc-objc
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/cc1obj
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/include/objc/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libobjc.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libobjc.dll.a
%{cygwin64_bindir}/cygobjc-4.dll


%files -n cygwin64-gcc-objc++
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/cc1objplus
%endif


%files -n cygwin64-gcc-gfortran
%{_bindir}/%{cygwin64_target}-gfortran
%{_mandir}/man1/%{cygwin64_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/f951
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/libgfortran.spec
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/finclude
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/finclude/ieee_*
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/finclude/omp_lib*
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/finclude/openacc*
%{cygwin64_bindir}/cyggfortran-4.dll


%if %{build_ada}
%files -n cygwin64-gcc-gnat
%{_bindir}/%{cygwin64_target}-gnat*
#%%{_mandir}/man1/%%{cygwin64_target}-gnat*.1*
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/adainclude/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{version}/adalib/
%{_libexecdir}/gcc/%{cygwin64_target}/%{version}/gnat1
#%%{cygwin64_bindir}/cyggnarl-7.dll
#%%{cygwin64_bindir}/cyggnat-7.dll
%endif


%changelog
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
