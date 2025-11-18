ARG BUILD_FROM=ghcr.io/hassio-addons/base:16.2.2
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip py3-pyusb

COPY minidsp_2x4hd_usb/ /usr/local/share/minidsp_2x4hd_usb/

RUN chmod +x /usr/local/share/minidsp_2x4hd_usb/services.d/minidsp/run && \
    chmod +x /usr/local/share/minidsp_2x4hd_usb/services.d/minidsp/finish && \
    chmod +x /usr/local/share/minidsp_2x4hd_usb/minidsp-usb.py

CMD [ "/usr/bin/s6-svscan", "/usr/local/share/minidsp_2x4hd_usb/services.d" ]
