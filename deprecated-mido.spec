#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-mido
Version  : 1.2.9
Release  : 31
URL      : https://files.pythonhosted.org/packages/47/a8/f05e3e6491568de9e03506a869a6039e2892d8350809203bd9abcf4b17a8/mido-1.2.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/a8/f05e3e6491568de9e03506a869a6039e2892d8350809203bd9abcf4b17a8/mido-1.2.9.tar.gz
Summary  : MIDI Objects for Python
Group    : Development/Tools
License  : MIT
Requires: deprecated-mido-bin = %{version}-%{release}
Requires: deprecated-mido-license = %{version}-%{release}
Requires: deprecated-mido-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Mido - MIDI Objects for Python
==============================
.. image:: https://travis-ci.org/olemb/mido.svg?branch=master
:target: https://travis-ci.org/olemb/mido

%package bin
Summary: bin components for the deprecated-mido package.
Group: Binaries
Requires: deprecated-mido-license = %{version}-%{release}

%description bin
bin components for the deprecated-mido package.


%package legacypython
Summary: legacypython components for the deprecated-mido package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-mido package.


%package license
Summary: license components for the deprecated-mido package.
Group: Default

%description license
license components for the deprecated-mido package.


%package python
Summary: python components for the deprecated-mido package.
Group: Default

%description python
python components for the deprecated-mido package.


%prep
%setup -q -n mido-1.2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554341168
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-mido
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-mido/LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/deprecated-mido/docs_license.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/mido-connect
%exclude /usr/bin/mido-play
%exclude /usr/bin/mido-ports
%exclude /usr/bin/mido-serve

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-mido/LICENSE
/usr/share/package-licenses/deprecated-mido/docs_license.rst

%files python
%defattr(-,root,root,-)
