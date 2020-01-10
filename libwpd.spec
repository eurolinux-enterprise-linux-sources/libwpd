%global apiversion 0.9
%global streamname %{name}-stream

Name: libwpd
Summary: Library for reading and converting WordPerfect documents
Version: 0.9.9
Release: 3%{?dist}
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Group: System Environment/Libraries
URL: http://libwpd.sf.net/
License: LGPLv2+ or MPLv2.0

BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: zlib-devel

%description
Library that handles Word Perfect documents.

%package tools
Summary: Tools to transform WordPerfect Documents into other formats
Group: Applications/Publishing
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: HTML, raw, text.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Files for developing with libwpd
Group: Development/Libraries

%description devel
Includes and definitions for developing with libwpd.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %{name}-doc package contains API documentation for %{name}.

%prep
%setup -q

chmod -x docs/%{name}.dia

%build
%configure --disable-static --disable-werror
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
# we install API docs directly from build
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=../lib/.libs make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING.LGPL COPYING.MPL CREDITS README
%{_libdir}/%{name}-%{apiversion}.so.*
%{_libdir}/%{streamname}-%{apiversion}.so.*

%files tools
%{_bindir}/wpd2html
%{_bindir}/wpd2raw
%{_bindir}/wpd2text

%files devel
%doc HACKING TODO
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{streamname}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%{_libdir}/pkgconfig/%{streamname}-%{apiversion}.pc
%{_includedir}/%{name}-%{apiversion}

%files doc
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html
%doc docs/%{name}.dia
%doc docs/%{name}.png

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9.9-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.9-2
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 David Tardon <dtardon@redhat.com> - 0.9.9-1
- new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 David Tardon <dtardon@redhat.com> - 0.9.8-2
- drop build dep on libgsf-devel that has not been needed for years

* Tue May 14 2013 David Tardon <dtardon@redhat.com> - 0.9.8-1
- new release

* Sun Apr 21 2013 David Tardon <dtardon@redhat.com> - 0.9.7-1
- new release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 David Tardon <dtardon@redhat.com> - 0.9.6-1
- new release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.9.4-1
- latest version

* Sun May 22 2011 Caolán McNamara <caolanm@redhat.com> - 0.9.2-1
- latest version
- drop integrated libwpd-gcc4.6.0.patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Caolán McNamara <caolanm@redhat.com> - 0.9.1-1
- latest version

* Sun Dec 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.9.0-1
- latest version

* Sat Feb 13 2010 Caolán McNamara <caolanm@redhat.com> - 0.8.14-5
- Resolves: rhbz#226060 merge review

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8.14-2
- Rebuild for provides

* Wed Feb 13 2008 Caolán McNamara <caolanm@redhat.com> - 0.8.14-1
- next version

* Mon Dec 17 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.13-2
- strangely 0.8.13-1 never appeared in rawhide

* Thu Dec 13 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.13-1
- next version

* Sat Oct 13 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.12-1
- next version

* Fri Aug 24 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.11-1
- next version

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.10-2
- clarify license

* Fri Jun 15 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.10-1
- next version

* Tue Mar 27 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.9-2
- Resolves: rhbz#233876: add unowned directory fix from Michael Schwendt 

* Fri Mar 16 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.9-1
- next version

* Fri Feb 09 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.8-2
- spec cleanups

* Thu Jan 11 2007 Caolán McNamara <caolanm@redhat.com> - 0.8.8-1
- next version

* Mon Oct 09 2006 Caolán McNamara <caolanm@redhat.com> - 0.8.7-1
- next version

* Mon Jul 17 2006 Caolán McNamara <caolanm@redhat.com> - 0.8.6-1
- next version

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.8.5-3.1
- rebuild

* Sun Jun 11 2006  Caolán McNamara <caolanm@redhat.com> 0.8.5-3
- add wp5nofontlistcrash

* Fri Jun 02 2006  Caolán McNamara <caolanm@redhat.com> 0.8.5-2
- build through brew

* Thu Jun 01 2006  Caolán McNamara <caolanm@redhat.com> 0.8.5-1
- next version

* Tue Mar 21 2006  Caolán McNamara <caolanm@redhat.com> 0.8.4-2
- rebuild for libgsf

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.8.4-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.8.4-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 0.8.4-1.1
- rebuilt

* Fri Dec 02 2005 Caolán McNamara <caolanm@redhat.com> 0.8.4-1
- next version

* Fri Dec 02 2005 Caolán McNamara <caolanm@redhat.com> 0.8.3-2
- rebuild because of libgsf

* Tue Jun 28 2005 Caolán McNamara <caolanm@redhat.com> 0.8.3-1
- update to latest libwpd

* Tue Jun 28 2005 Caolán McNamara <caolanm@redhat.com> 0.8.2-2.fc5
- export to other formats twiddle

* Wed Jun 22 2005 Caolán McNamara <caolanm@redhat.com> 0.8.2-1
- bump to latest version

* Fri Apr 29 2005 Caolán McNamara <caolanm@redhat.com> 0.8.1-1
- bump to latest version kudos Fridrich Strba
- drop integrated patch

* Wed Apr  6 2005 Caolán McNamara <caolanm@redhat.com> 0.8.0-4
- add libwpd devel provided patch for endless loops on some wpd documents

* Wed Mar 30 2005 Caolán McNamara <caolanm@redhat.com> 0.8.0-3
- rh#152503# add some Requires for -devel package

* Wed Mar  2 2005 Caolán McNamara <caolanm@redhat.com> 0.8.0-2
- rebuild with gcc4

* Fri Feb 11 2005 Caolán McNamara <caolanm@redhat.com> 0.8.0-1
- new version

* Wed Feb 9 2005 Caolán McNamara <caolanm@redhat.com> 0.7.2-2
- rebuild

* Fri Jul 23 2004 Caolán McNamara <caolanm@redhat.com> 0.7.2-1
- bump to 0.7.2

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Jeremy Katz <katzj@redhat.com> - 0.7.1-1
- update to 0.7.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 16 2003 Jeremy Katz <katzj@redhat.com> 0.6.6-1
- 0.6.6

* Tue Nov  4 2003 Jeremy Katz <katzj@redhat.com> 0.6.5-1
- 0.6.5

* Mon Sep 15 2003 Jeremy Katz <katzj@redhat.com> 0.6.2-1
- 0.6.2

* Sun Jul  6 2003 Jeremy Katz <katzj@redhat.com> 0.5.0-1
- initial build for Red Hat Linux, tweak accordingly

* Sat Apr 26 2003 Rui M. Seabra <rms@1407.org>
- Create rpm spec
