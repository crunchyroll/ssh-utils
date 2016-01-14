# cpennello 2015-02-05

.PHONY: help install uninstall rpm

utils=$(wildcard ssh-*)
prefix=/usr/local
bin=$(prefix)/bin
rpmspec=rpm.spec

help:
	@echo targets:
	@sed -nr 's/^(\w+):.*/  \1/p' Makefile

install: $(utils)
	cp $^ $(bin)

uninstall:
	cd $(bin); rm $(utils)

rpm: $(rpmspec)
	rpmbuild -bb $<
