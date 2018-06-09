#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : linecache2
Version  : 1.0.0
Release  : 33
URL      : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz
Source0  : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz
Source99 : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz.asc
Summary  : Backports of the linecache module
Group    : Development/Tools
License  : Python-2.0
Requires: linecache2-python3
Requires: linecache2-python
BuildRequires : fixtures-python
BuildRequires : pbr
BuildRequires : pbr-legacypython
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : six-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
>>> import linecache2 as linecache
        
        Profit.

%package legacypython
Summary: legacypython components for the linecache2 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the linecache2 package.


%package python
Summary: python components for the linecache2 package.
Group: Default
Requires: linecache2-python3

%description python
python components for the linecache2 package.


%package python3
Summary: python3 components for the linecache2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the linecache2 package.


%prep
%setup -q -n linecache2-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528573632
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1528573632
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
