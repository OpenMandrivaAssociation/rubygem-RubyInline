%define oname RubyInline

Name:       rubygem-%{oname}
Version:    3.8.6
Release:    2
Summary:    Inline allows you to write foreign code within your ruby code
Group:      Development/Ruby
License:    MIT
URL:        https://rubyforge.org/projects/rubyinline/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(ZenTest) >= 4.3
Requires:   rubygem(rubyforge) >= 2.0.4
Requires:   rubygem(minitest) >= 1.7.1
Requires:   rubygem(hoe) >= 2.6.2
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Inline allows you to write foreign code within your ruby code. It
automatically determines if the code in question has changed and
builds it only when necessary. The extensions are then automatically
loaded into the class/module that defines it.
You can even write extra builders that will allow you to write inlined
code in any language. Use Inline::C as a template and look at
Module#inline for the required API.


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/demo -type f | xargs chmod 755
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test -type f | xargs chmod 755
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/tutorial -type f | xargs chmod 755
chmod 755 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/example*.rb
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby\w*/,"/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{example.rb,example2.rb,demo/hello.rb,lib/inline.rb}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/demo/
%{ruby_gemdir}/gems/%{oname}-%{version}/example*.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/tutorial/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 3.8.6-1mdv2011.0
+ Revision: 585882
- import rubygem-RubyInline

