%global tl_name vaucanson-g
%global tl_revision 79288

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	PSTricks macros for drawing automata
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/vaucanson-g
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
VauCanSon-G is a package that enables the user to draw automata within
texts written using LaTeX. The package macros make use of commands of
PStricks.

