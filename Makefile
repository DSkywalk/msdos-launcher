prefix = /usr/local

# These variables are used to generate compatibilitytool.vdf:
#
tool_name             = msdos-launcher
tool_name_display     = DOSBox Launcher (native MSDOS)


files = run-dosbox \
	config.py \
	log.py \
	helpers.py \
	version.py \
	toolmanifest.vdf \
	LICENSE \
	README.md

msdos-launcher.vdf: compatibilitytool.template
	sed 's/%name%/$(tool_name)/; s/%display_name%/$(tool_name_display)/; s|%path%|$(tool_vdf_path)|;' \
	    $< > $@

install: tool_vdf_path = $(prefix)/share/msdos-launcher
install: msdos-launcher.vdf $(files)
	install -m 644 -Dt "$(DESTDIR)$(prefix)/share/steam/compatibilitytools.d/"        msdos-launcher.vdf
	install        -Dt "$(DESTDIR)$(prefix)/share/msdos-launcher/"                    run-dosbox
	install -m 644 -Dt "$(DESTDIR)$(prefix)/share/msdos-launcher/"                    *.py
	install -m 644 -Dt "$(DESTDIR)$(prefix)/share/msdos-launcher/"                    toolmanifest.vdf
	install -m 644 -Dt "$(DESTDIR)$(prefix)/share/doc/msdos-launcher/"                README.md
	install -m 644 -Dt "$(DESTDIR)$(prefix)/share/licenses/msdos-launcher/"           LICENSE
	@echo
	@echo 'Restart Steam, so it can pick up new compatibility tool.'
	@echo 'You can type "make uninstall" to remove the launcher.'


uninstall:
	rm    "$(DESTDIR)$(prefix)/share/msdos-launcher"/*
	rmdir "$(DESTDIR)$(prefix)/share/msdos-launcher"
	rm    "$(DESTDIR)$(prefix)/share/doc/msdos-launcher"/*
	rmdir "$(DESTDIR)$(prefix)/share/doc/msdos-launcher"
	rm    "$(DESTDIR)$(prefix)/share/licenses/msdos-launcher"/*
	rmdir "$(DESTDIR)$(prefix)/share/licenses/msdos-launcher"
	rm    "$(DESTDIR)$(prefix)/share/steam/compatibilitytools.d/msdos-launcher.vdf"
	rmdir --ignore-fail-on-non-empty "$(DESTDIR)$(prefix)/share/steam/compatibilitytools.d"
	rmdir --ignore-fail-on-non-empty "$(DESTDIR)$(prefix)/share"/{doc,licenses,steam}

