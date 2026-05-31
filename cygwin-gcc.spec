%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

# Set this to one when cygwin and cygwin-w32api-runtime packages aren't built
# yet. Bootstrap mode builds just enough gcc to build those.
%global bootstrap 0

%global gcc_major 16
%global gcc_minor 1
%global gcc_micro 0
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 6

%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%undefine _auto_set_build_flags
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif

%dnl undefine cygwin_build_32bit
%undefine cygwin_build_64bit
%dnl undefine cygwin_build_aarch64

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
%if ! %{bootstrap}
BuildRequires:  cygwin32-w32api-runtime
BuildRequires:  cygwin32 >= 3.0.0
%endif

BuildRequires:  cygwin64-filesystem
BuildRequires:  cygwin64-binutils
BuildRequires:  cygwin64-w32api-headers
%if ! %{bootstrap}
BuildRequires:  cygwin64-w32api-runtime
BuildRequires:  cygwin64 >= 3.0.0
%endif

BuildRequires:  cygwin-aarch64-filesystem
BuildRequires:  cygwin-aarch64-binutils
BuildRequires:  cygwin-aarch64-w32api-headers
%if ! %{bootstrap}
BuildRequires:  cygwin-aarch64-w32api-runtime
BuildRequires:  cygwin-aarch64 >= 3.0.0
%endif

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
Source1:        fake-cygwin-includes.patch

# Cygwin patches
Patch1:		0001-Always-define-WIN32_LEAN_AND_MEAN-before-windows.h.patch
Patch2:		0002-add-m-no-align-vector-insn-option-for-i386.patch
Patch3:		0003-Cygwin-use-SysV-ABI-on-x86_64.patch
Patch4:		0004-Cygwin-add-dummy-pthread-tsaware-and-large-address-a.patch
Patch5:		0005-Cygwin-handle-dllimport-properly-in-medium-model-V2.patch
Patch6:		0006-Cygwin-MinGW-skip-test.patch
Patch7:		0007-Cygwin-define-RTS_CONTROL_ENABLE-and-DTR_CONTROL_ENA.patch
Patch8:		0008-Cygwin-__cxa-atexit.patch
Patch9:		0009-Cygwin-libgomp-soname.patch
Patch10:	0010-Cygwin-g-time.patch
Patch11:	0011-Cygwin-newlib-ftm.patch
Patch12:	0012-Cygwin-define-STD_UNIX.patch

Patch400:	0401-libstdc-Cygwin-fix-a-handle-leak-in-mutex_base.patch
Patch401:	0401-fix-build-gcc-opts.cc.patch
Patch402:	0402-fix-build-libcpp-lex.cc.patch
Patch403:	0403-fix-build-adaint.c.patch

# current patch set of Evgeny Karpov, very approximately rebased onto 16.1.0
Patch501:	0501-aarch64-Bypass-some-warnings-in-MinGW.patch
Patch502:	0502-aarch64-Add-stdcall-and-cdecl-attributes.patch
Patch503:	0503-Rename-SEH-functions-for-reuse-in-AArch64.patch
Patch504:	0504-aarch64-Add-SEH-stack-unwinding-and-C-exceptions.patch
Patch505:	0505-Support-SEH-for-fragmented-functions.patch
Patch506:	0506-Fix-unwiding-code-for-a-floating-point-register-pair.patch
Patch507:	0507-Fix-unwiding-codes-when-stack-probing-is-applied.patch
Patch508:	0508-Rebase-woarm64-aarch64-pe-target-prototype.patch
Patch509:	0509-Fix-build-on-x86_64-pc-linux-gnu-when-host-is-aarch6.patch
Patch510:	0510-Fix-undefined-reference-to-mingw-10.patch
Patch511:	0511-Fix-missing-aarch64-opt.url-files-after-rebase.patch
Patch512:	0512-Fix-undefined-references-to-__gthr_win32_-shared-lib.patch
Patch513:	0513-Build-configuration-fixes-to-enable-native-aarch64-w.patch
Patch514:	0514-Allow-some-warnings-when-building-libgcc-36.patch
Patch515:	0515-Fix-build-of-winnt-d.cc-when-D-language-is-enabled.-.patch

Patch528:	0528-Add-aarch64-pc-cygwin-target.patch
Patch529:	0529-Change-long-double-to-64bit-3.patch
Patch530:	0530-Fix.patch
Patch531:	0531-Add-support-for-shared-attribute-41.patch
Patch532:	0532-Fix-some-configuration-checks-ignored-for-aarch64-by.patch
Patch533:	0533-Resolve-compilation-issue-on-aarch64-pc-cygwin.patch
Patch534:	0534-Fix-unwinding-for-nonconsecutive-registers-2.patch
Patch535:	0535-Add-SEH-unwinding-support-for-UNSPEC_STP-4.patch
Patch536:	0536-Fix-aarch64-unwinding-with-debugger-attached-3.patch
Patch537:	0537-Add-MS-variadic-ABI-support-to-aarch64-pc-cygwin-tar.patch
Patch538:	0538-Disable-float80.patch

# additional patches
Patch600:       0001-libgcc-select-Win32-enable-execute-stack-on-Win32-aa.patch
Patch601:       0002-libgcc-Hacks-for-compiler-bootstrapping.patch
Patch602:       0003-Workaound-unable-to-emulate-TF-error.patch

# Fedora-specific patches
Patch1001:      1001-textdomain.patch
Patch1002:      1002-cygwin-ld-flags.patch
Patch1003:	1003-no-format-security.patch

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
%if ! %{bootstrap}
Requires:       cygwin32-default-manifest
Requires:       cygwin32-w32api-runtime
Requires:       cygwin32 >= 3.0.0
%endif
Requires:       cygwin32-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
%if ! %{bootstrap}
Provides:       cygwin32(cygatomic-1.dll)
Provides:       cygwin32(cyggcc_s-1.dll)
Provides:       cygwin32(cyggomp-1.dll)
Provides:       cygwin32(cygquadmath-0.dll)
%endif
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
%if ! %{bootstrap}
Provides:  cygwin32(cygstdc++-6.dll)
%endif

%description -n cygwin32-gcc-c++
Cygwin cross-compiler for C++.


%package -n cygwin32-gcc-gfortran
Summary: Cygwin cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin32-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
%if ! %{bootstrap}
Provides:  cygwin32(cyggfortran-5.dll)
%endif

%description -n cygwin32-gcc-gfortran
Cygwin cross-compiler for FORTRAN.


%package -n cygwin64-gcc
Summary: Cygwin64 cross-compiler for C
Group:   Development/Languages
# NB: Explicit cygwin-filesystem dependency is REQUIRED here.
Requires:       cygwin64-filesystem
Requires:       cygwin64-binutils
%if ! %{bootstrap}
Requires:       cygwin64-default-manifest
Requires:       cygwin64-w32api-runtime
Requires:       cygwin64 >= 3.0.0
%endif
Requires:       cygwin64-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLLs:
%if ! %{bootstrap}
Provides:       cygwin64(cygatomic-1.dll)
Provides:       cygwin64(cyggcc_s-seh-1.dll)
Provides:       cygwin64(cyggomp-1.dll)
Provides:       cygwin64(cygquadmath-0.dll)
%endif
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
%if ! %{bootstrap}
Provides:  cygwin64(cygstdc++-6.dll)
%endif

%description -n cygwin64-gcc-c++
Cygwin x86_64 cross-compiler for C++.


%package -n cygwin64-gcc-gfortran
Summary: Cygwin64 cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
%if ! %{bootstrap}
Provides:  cygwin64(cyggfortran-5.dll)
%endif

%description -n cygwin64-gcc-gfortran
Cygwin x86_64 cross-compiler for FORTRAN.


%package -n cygwin-aarch64-gcc
Summary: Cygwin aarch64 cross-compiler for C
Group:   Development/Languages
# NB: Explicit cygwin-filesystem dependency is REQUIRED here.
Requires:       cygwin-aarch64-filesystem
Requires:       cygwin-aarch64-binutils
%if ! %{bootstrap}
Requires:       cygwin-aarch64-default-manifest
Requires:       cygwin-aarch64-w32api-runtime
Requires:       cygwin-aarch64 >= 3.0.0
%endif
Requires:       cygwin-aarch64-cpp = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLLs:
%if ! %{bootstrap}
Provides:       cygwin-aarch64(cygatomic-1.dll)
Provides:       cygwin-aarch64(cyggcc_s-seh-1.dll)
Provides:       cygwin-aarch64(cyggomp-1.dll)
Provides:       cygwin-aarch64(cygquadmath-0.dll)
%endif
# prevent update errors
Obsoletes:      cygwin-aarch64-gcc-gnat < %{version}-%{release}
Obsoletes:      cygwin-aarch64-gcc-objc < %{version}-%{release}
Obsoletes:      cygwin-aarch64-gcc-objc++ < %{version}-%{release}


%description -n cygwin-aarch64-gcc
Cygwin aarch64 cross-compiler (GCC) for C.

%package -n cygwin-aarch64-cpp
Summary:   Cygwin aarch64 cross-C Preprocessor
Group:     Development/Languages
Requires:  %{name}-common = %{version}-%{release}

%description -n cygwin-aarch64-cpp
Cygwin aarch64 cross-C Preprocessor


%package -n cygwin-aarch64-gcc-c++
Summary: Cygwin aarch64 cross-compiler for C++
Group: Development/Languages
Requires: cygwin-aarch64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
%if ! %{bootstrap}
Provides:  cygwin-aarch64(cygstdc++-6.dll)
%endif

%description -n cygwin-aarch64-gcc-c++
Cygwin aarch64 cross-compiler for C++.


%package -n cygwin-aarch64-gcc-gfortran
Summary: Cygwin aarch64 cross-compiler for FORTRAN
Group: Development/Languages
Requires:  cygwin-aarch64-gcc = %{version}-%{release}
# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
%if ! %{bootstrap}
Provides:  cygwin-aarch64(cyggfortran-5.dll)
%endif

%description -n cygwin-aarch64-gcc-gfortran
Cygwin aarch64 cross-compiler for FORTRAN.


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

CONFIGURE_OPTS="\
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --build=%_build --host=%_host \
  --with-gnu-as --with-gnu-ld --verbose \
  --enable-linker-build-id \
  --disable-multilib \
  --with-system-zlib \
%if !%{bootstrap}
  --enable-shared \
  --enable-shared-libgcc \
%else
  --disable-shared \
  --disable-shared-libgcc \
%endif
  --enable-static \
  --without-included-gettext \
  --disable-win32-registry \
%if !%{bootstrap}
  --enable-threads=posix \
%else
  --disable-threads \
%endif
  --enable-version-specific-runtime-libs \
  --with-gcc-major-version-only \
  --enable-__cxa_atexit \
%if !%{bootstrap}
  --with-dwarf2 \
%else
  --without-dwarf2 \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
  --enable-graphite \
%endif
  --enable-languages="c,c++,fortran,lto" \
  --disable-libcc1 \
%if %{bootstrap}
  --disable-lto \
  --disable-gcov \
%else
  --enable-lto \
%endif
  --disable-symvers \
  --enable-libatomic \
  --enable-libgomp \
  --disable-libssp \
  --enable-libstdcxx-filesystem-ts \
  --with-bugurl=https://copr.fedorainfracloud.org/coprs/yselkowitz/cygwin/
"

%if 0%{?cygwin_build_32bit} == 1
mkdir -p build_32bit
pushd build_32bit

CC="%{__cc} ${RPM_OPT_FLAGS}" \
../configure \
  $CONFIGURE_OPTS \
  --target=%{cygwin32_target} \
  --with-arch=i686 --with-tune=generic \
  --with-sysroot=%{cygwin32_sysroot} \
  --disable-sjlj-exceptions \
  --enable-libquadmath \
  --enable-libquadmath-support \
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_major}/%{cygwin32_target}/python

popd
%endif

%if 0%{?cygwin_build_64bit} == 1
mkdir -p build_64bit
pushd build_64bit

CC="%{__cc} ${RPM_OPT_FLAGS}" \
../configure \
  $CONFIGURE_OPTS \
  --target=%{cygwin64_target} \
  --with-tune=generic \
  --with-sysroot=%{cygwin64_sysroot} \
  --enable-libquadmath \
  --enable-libquadmath-support \
  --with-default-libstdcxx-abi=gcc4-compatible \
  --with-python-dir=/share/gcc-%{gcc_major}/%{cygwin64_target}/python

popd
%endif

%if 0%{?cygwin_build_aarch64} == 1
mkdir -p build_aarch64
pushd build_aarch64

CC="%{__cc} ${RPM_OPT_FLAGS}" \
../configure \
  $CONFIGURE_OPTS \
  --target=%{cygwin_aarch64_target} \
  --with-arch=armv8.1-a -with-tune=cortex-x1 \
  --with-sysroot=%{cygwin_aarch64_sysroot} \
  --disable-libquadmath \
  --disable-libquadmath-support \
  --with-python-dir=/share/gcc-%{gcc_major}/%{cygwin_aarch64_target}/python

popd
%endif


# if bootstrapping, only build gcc core and libgcc
%if %{bootstrap}
%cygwin_make %{?_smp_mflags} all-gcc
%cygwin_make all-target-libgcc CFLAGS_FOR_TARGET="-Dinhibit_libc"
%else
%cygwin_make %{?_smp_mflags} all
%endif


%install
%if %{bootstrap}
%cygwin_make DESTDIR=$RPM_BUILD_ROOT install-gcc install-target-libgcc
%else
%cygwin_make_install DESTDIR=$RPM_BUILD_ROOT
%endif

# These files conflict with existing installed files.
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty*
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/*

mkdir -p $RPM_BUILD_ROOT/lib
ln -sf ..%{_prefix}/bin/%{cygwin32_target}-cpp \
  $RPM_BUILD_ROOT/lib/%{cygwin32_target}-cpp
%if 0%{?cygwin_build_64bit} == 1
ln -sf ..%{_prefix}/bin/%{cygwin64_target}-cpp \
  $RPM_BUILD_ROOT/lib/%{cygwin64_target}-cpp
%endif
ln -sf ..%{_prefix}/bin/%{cygwin_aarch64_target}-cpp \
  $RPM_BUILD_ROOT/lib/%{cygwin_aarch64_target}-cpp


# clean-up include-fixed
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include-fixed/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include-fixed/
rm -fr $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/include-fixed/

# libtool installs DLL files of runtime libraries into $(libdir)/../bin,
# but we need them in cygwin*_bindir.
%if ! %{bootstrap}
%if 0%{?cygwin_build_32bit} == 1
mkdir -p $RPM_BUILD_ROOT%{cygwin32_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/*.dll \
  $RPM_BUILD_ROOT%{cygwin32_bindir}
%endif
%if 0%{?cygwin_build_64bit} == 1
mkdir -p $RPM_BUILD_ROOT%{cygwin64_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/*.dll \
  $RPM_BUILD_ROOT%{cygwin64_bindir}
%endif
mkdir -p $RPM_BUILD_ROOT%{cygwin_aarch64_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/*.dll \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/*.dll \
  $RPM_BUILD_ROOT%{cygwin_aarch64_bindir}
%endif

# Don't want the *.la files.
find $RPM_BUILD_ROOT -name '*.la' -delete

%if %{bootstrap}
# Fakery necessary to compile w32api-runtime with a bootstrap cygwin-gcc. It
# doesn't pull in the cygwin package, which has the real includes, so just fake
# the minimum we need. (It might be better just to use a copy of them here?).
for d in \
%if 0%{?cygwin_build_32bit} == 1
  %{cygwin32_includedir} \
%endif
%if 0%{?cygwin_build_64bit} == 1
  %{cygwin64_includedir} \
%endif
  %{cygwin_aarch64_includedir}
do
    mkdir -p $RPM_BUILD_ROOT${d}
    patch -d $RPM_BUILD_ROOT${d} -p1 <%{SOURCE1}
done
%endif


%find_lang cygwin-gcc
%if ! %{bootstrap}
%find_lang cygwin-cpplib
cat cygwin-cpplib.lang >> cygwin-gcc.lang
%endif


%files common -f cygwin-gcc.lang
%doc gcc/README* gcc/COPYING*


%if 0%{?cygwin_build_32bit} == 1
%files -n cygwin32-gcc
%{_bindir}/%{cygwin32_target}-gcc
%{_bindir}/%{cygwin32_target}-gcc-%{gcc_major}
%{_bindir}/%{cygwin32_target}-gcc-ar
%{_bindir}/%{cygwin32_target}-gcc-nm
%{_bindir}/%{cygwin32_target}-gcc-ranlib
%if ! %{bootstrap}
%{_bindir}/%{cygwin32_target}-gcov
%{_bindir}/%{cygwin32_target}-gcov-dump
%{_bindir}/%{cygwin32_target}-gcov-tool
%endif
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
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libatomic.dll.a
%endif
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc.a
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libquadmath.dll.a
%else
%{cygwin32_includedir}/*
%endif
%dir %{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include/*.h
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/install-tools/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/plugin/
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/install-tools/
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/liblto_plugin.so
%endif
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/lto1
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/plugin/
%if ! %{bootstrap}
%dir %{_datadir}/gcc-%{gcc_major}
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}
%{cygwin32_bindir}/cygatomic-1.dll
%{cygwin32_bindir}/cyggcc_s-1.dll
%{cygwin32_bindir}/cyggomp-1.dll
%{cygwin32_bindir}/cygquadmath-0.dll
%endif


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
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/include/c++/
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++exp.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}/python
%{_datadir}/gcc-%{gcc_major}/%{cygwin32_target}/python/libstdcxx/
%{cygwin32_bindir}/cygstdc++-6.dll
%endif


%files -n cygwin32-gcc-gfortran
%{_bindir}/%{cygwin32_target}-gfortran
%{_mandir}/man1/%{cygwin32_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin32_target}/%{gcc_major}/f951
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{cygwin32_target}/%{gcc_major}/finclude/
%{cygwin32_bindir}/cyggfortran-5.dll
%endif
%endif


%if 0%{?cygwin_build_64bit} == 1
%files -n cygwin64-gcc
%{_bindir}/%{cygwin64_target}-gcc
%{_bindir}/%{cygwin64_target}-gcc-%{gcc_major}
%{_bindir}/%{cygwin64_target}-gcc-ar
%{_bindir}/%{cygwin64_target}-gcc-nm
%{_bindir}/%{cygwin64_target}-gcc-ranlib
%if ! %{bootstrap}
%{_bindir}/%{cygwin64_target}-gcov
%{_bindir}/%{cygwin64_target}-gcov-dump
%{_bindir}/%{cygwin64_target}-gcov-tool
%endif
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
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libatomic.dll.a
%endif
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc.a
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgomp.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libquadmath.dll.a
%else
%{cygwin64_includedir}/*
%endif
%dir %{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include/*.h
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/install-tools/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/plugin/
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/install-tools/
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/liblto_plugin.so
%endif
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/lto1
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/plugin/
%if ! %{bootstrap}
%dir %{_datadir}/gcc-%{gcc_major}
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}
%{cygwin64_bindir}/cygatomic-1.dll
%{cygwin64_bindir}/cyggcc_s-seh-1.dll
%{cygwin64_bindir}/cyggomp-1.dll
%{cygwin64_bindir}/cygquadmath-0.dll
%endif


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
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/include/c++/
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++exp.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}/python
%{_datadir}/gcc-%{gcc_major}/%{cygwin64_target}/python/libstdcxx/
%{cygwin64_bindir}/cygstdc++-6.dll
%endif


%files -n cygwin64-gcc-gfortran
%{_bindir}/%{cygwin64_target}-gfortran
%{_mandir}/man1/%{cygwin64_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin64_target}/%{gcc_major}/f951
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{cygwin64_target}/%{gcc_major}/finclude/
%{cygwin64_bindir}/cyggfortran-5.dll
%endif
%endif



%files -n cygwin-aarch64-gcc
%{_bindir}/%{cygwin_aarch64_target}-gcc
%{_bindir}/%{cygwin_aarch64_target}-gcc-%{gcc_major}
%{_bindir}/%{cygwin_aarch64_target}-gcc-ar
%{_bindir}/%{cygwin_aarch64_target}-gcc-nm
%{_bindir}/%{cygwin_aarch64_target}-gcc-ranlib
%if ! %{bootstrap}
%{_bindir}/%{cygwin_aarch64_target}-gcov
%{_bindir}/%{cygwin_aarch64_target}-gcov-dump
%{_bindir}/%{cygwin_aarch64_target}-gcov-tool
%endif
%{_bindir}/%{cygwin_aarch64_target}-lto-dump
%{_mandir}/man1/%{cygwin_aarch64_target}-gcc.1*
%{_mandir}/man1/%{cygwin_aarch64_target}-gcov.1*
%{_mandir}/man1/%{cygwin_aarch64_target}-gcov-dump.1*
%{_mandir}/man1/%{cygwin_aarch64_target}-gcov-tool.1*
%{_mandir}/man1/%{cygwin_aarch64_target}-lto-dump.1*
%dir %{_prefix}/lib/gcc/%{cygwin_aarch64_target}
%dir %{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/crtbegin.o
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/crtbeginS.o
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/crtend.o
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/crtfastmath.o
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libatomic.dll.a
%endif
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgcc.a
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgcc_s.dll.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgomp.a
%if 0
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgomp.dll.a
%endif
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgomp.spec
%if 0
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libquadmath.dll.a
%endif
%else
%{cygwin_aarch64_includedir}/*
%endif
%dir %{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/include
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/include/*.h
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/install-tools/
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/plugin/
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/install-tools/
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/liblto_plugin.so
%endif
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/lto1
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/lto-wrapper
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/plugin/
%if ! %{bootstrap}
%dir %{_datadir}/gcc-%{gcc_major}
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin_aarch64_target}
%{cygwin_aarch64_bindir}/cygatomic-1.dll
%{cygwin_aarch64_bindir}/cyggcc_s-seh-1.dll
%if 0
%{cygwin_aarch64_bindir}/cyggomp-1.dll
%endif
%if 0
%{cygwin_aarch64_bindir}/cygquadmath-0.dll
%endif
%endif


%files -n cygwin-aarch64-cpp
/lib/%{cygwin_aarch64_target}-cpp
%{_bindir}/%{cygwin_aarch64_target}-cpp
%{_mandir}/man1/%{cygwin_aarch64_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{cygwin_aarch64_target}
%dir %{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/cc1


%files -n cygwin-aarch64-gcc-c++
%{_bindir}/%{cygwin_aarch64_target}-g++
%{_bindir}/%{cygwin_aarch64_target}-c++
%{_mandir}/man1/%{cygwin_aarch64_target}-g++.1*
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/cc1plus
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/collect2
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/include/c++/
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libstdc++.dll.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libstdc++.dll.a-gdb.py
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libstdc++exp.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libsupc++.a
%dir %{_datadir}/gcc-%{gcc_major}/%{cygwin_aarch64_target}/python
%{_datadir}/gcc-%{gcc_major}/%{cygwin_aarch64_target}/python/libstdcxx/
%{cygwin_aarch64_bindir}/cygstdc++-6.dll
%endif


%files -n cygwin-aarch64-gcc-gfortran
%{_bindir}/%{cygwin_aarch64_target}-gfortran
%{_mandir}/man1/%{cygwin_aarch64_target}-gfortran.1*
%{_libexecdir}/gcc/%{cygwin_aarch64_target}/%{gcc_major}/f951
%if ! %{bootstrap}
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgfortran.dll.a
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{cygwin_aarch64_target}/%{gcc_major}/finclude/
%{cygwin_aarch64_bindir}/cyggfortran-5.dll
%endif


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
