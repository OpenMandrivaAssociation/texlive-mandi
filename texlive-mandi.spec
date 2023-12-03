Name:		texlive-mandi
Version:	68950
Release:	1
Summary:	Macros for introductory physics and astronomy
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mandi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
