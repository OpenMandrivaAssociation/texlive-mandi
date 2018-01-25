Name:		texlive-mandi
Version:	2.7.1
Release:	1
Summary:	Macros for introductory physics and astronomy
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mandi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains commands for students and teachers of
introductory physics. Commands for physical quantities
intelligently handle SI units so the user need not do so. There
are other features that should make LaTeX easy for introductory
physics students.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mandi
%doc %{_texmfdistdir}/doc/latex/mandi
#- source
%doc %{_texmfdistdir}/source/latex/mandi

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
