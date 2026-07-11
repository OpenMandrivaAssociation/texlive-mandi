%global tl_name mandi
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2.2
Release:	%{tl_revision}.1
Summary:	Macros for introductory physics and astronomy
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mandi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mandi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains commands for students and teachers of introductory
physics. Commands for physical quantities intelligently handle SI units
so the user need not do so. There are other features that should make
LaTeX easy for introductory physics students. The name of the package
can be pronounced as "M&I" and refers to the physics textbook Matter &
Interactions.

