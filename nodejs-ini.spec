%{?scl:%scl_package nodejs-ini}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-ini
Version:    1.2.0
Release:    1%{?dist}
Summary:    An INI parser/serializer for node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/proto-list
Source0:    http://registry.npmjs.org/ini/-/ini-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  nodejs-tap

%description
An INI file parser and serializer for node.js.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/ini
cp -p ini.js package.json %{buildroot}%{nodejs_sitelib}/ini

%nodejs_symlink_deps

# We currently don't run tests because I'd have to file another ten or
# so review reuqests for the node.js TAP testing framework and methinks there
# are enough of those for now.  ;-)
##%%check
##tap test/*.js

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/ini
%doc README.md LICENSE

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.0-1
- New upstream release 1.2.0

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-3
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.0-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- new upstream release 1.1.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-1
- new upstream release 1.0.5
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2
- guard Requires for F17 automatic depedency generation

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1
- new upstream release 1.0.2

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-2
- add Group to make EL5 happy

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
