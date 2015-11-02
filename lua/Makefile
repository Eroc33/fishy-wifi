# Makefile - toplevel build for Whiffy Fishy

# store the SDK etc. either in ~/esp8266-stuff, or use ./esp8266-local-sdk
STUFFDIR=${HOME}/esp8266-stuff
ESPDIR=$(shell [ -d $(STUFFDIR) ] && \
  echo $(STUFFDIR) || echo `pwd`/esp8266-local-sdk)

# SDK and dev tool paths
ESPLORERDIR=${ESPDIR}/ESPlorer
ESPSDKDIR=$(ESPDIR)/esp-open-sdk-compiler
ESPTOOLDIR=$(ESPDIR)/esptool
NODEMCUDIR=$(ESPDIR)/nodemcu-firmware
XTENSABIN=$(ESPSDKDIR)/xtensa-lx106-elf/bin
MQTTSPYDIR=$(ESPDIR)/mqtt-spy
FIXPATH=PATH=${PATH}:$(XTENSABIN)

# which serial port?
# for the Pi: ESPPORT=/dev/ttyAMA0
ESPPORT=/dev/ttyUSB0

# an innocuous default target
help:
	@echo using SDK in $(ESPDIR)
	@echo make targets: nodemcu, nodemcu-with-dns, flashnodemcu, \
          flasholimex, esplorer, mqtt-spy...

# rebuild nodemcu
nodemcu:
	cd $(NODEMCUDIR); $(FIXPATH) $(MAKE)
nodemcu-with-dns:
	cd $(NODEMCUDIR); $(FIXPATH) $(MAKE) UNIVERSAL_TARGET_DEFINES=-DUSE_DNS

# copy a binary build of the firmware to our local tree
copy-nodemcu-bin:
	[ -d  $(ESPDIR)/nodemcu-bin ] || mkdir $(ESPDIR)/nodemcu-bin
	cp -r $(NODEMCUDIR)/bin/* $(ESPDIR)/nodemcu-bin

# flash the firmware to the ESP8266
flashnodemcu:
	cd $(NODEMCUDIR); $(FIXPATH) $(MAKE) flash ESPPORT=$(ESPPORT)
flasholimex:
	cd $(NODEMCUDIR); $(ESPTOOLDIR)/esptool.py --port $(ESPPORT) \
          write_flash -fs 16m 0 $(ESPTDIR)/0x00000.bin 0x10000 $(ESPDIR)/0x10000.bin
flasholimexcustom:
	cd $(NODEMCUDIR); $(ESPTOOLDIR)/esptool.py --port $(ESPPORT) \
          write_flash -fs 16m 0 $(ESPDIR)/nodemcu-bin/0x00000.bin 0x10000 $(ESPDIR)/nodemcu-bin/0x10000.bin
flasholimexlatest: 
	cd $(NODEMCUDIR); $(ESPTOOLDIR)/esptool.py --port $(ESPPORT) \
	  write_flash -fs 16m 0 pre_build/latest/nodemcu_latest.bin
# TODO         0x7E000 bin/blank.bin
flash0127:
	$(ESPTOOLDIR)/esptool.py --port $(ESPPORT) write_flash \
          -fs 16m 0 $(NODEMCUDIR)/pre_build/0.9.5/nodemcu_20150127.bin
flash0212:
	$(ESPTOOLDIR)/esptool.py --port $(ESPPORT) write_flash \
          -fs 16m 0 $(NODEMCUDIR)/pre_build/0.9.5/nodemcu_20150212.bin 
flash0123:
	$(ESPTOOLDIR)/esptool.py --port $(ESPPORT) write_flash \
          -fs 16m 0 $(NODEMCUDIR)/pre_build/0.9.5/nodemcu_20150123.bin 

# run ESPlorer
esplorer:
	cd $(ESPLORERDIR) && java -jar ./ESPlorer.jar &
seed-esplorer-prefs:
	PREFSDIR=${HOME}/.java/.userPrefs/com/; \
	[ -d $$PREFSDIR ] || mkdir -p $$PREFSDIR; cd $$PREFSDIR; \
        tar xvzf $(ESPDIR)/esplorer-snippets.tgz

# run mqtt-spy (note: install mosquitto broker first!)
mqtt-spy:
	cd $(MQTTSPYDIR) && java -jar mqtt-spy-0.1.7-jar-with-dependencies.jar
