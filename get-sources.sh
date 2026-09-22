#!
SPEC=${1:-cygwin-gcc.spec}
SRCDIR=${SRCDIR:-$(pwd)}
REF=$(echo %snapshot_commit | rpmspec -q --shell --srpm ${SPEC} 2>/dev/null | tail -2 | head -1)
mkdir -p tmp
cd tmp
git clone --no-checkout git://sourceware.org/git/gcc.git
cd gcc
git archive --prefix gcc-${REF}/ --output ${SRCDIR}/gcc.${REF}.tar.gz ${REF}
