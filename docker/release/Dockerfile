FROM debian:12.1

RUN groupadd varvarvpn \
&& useradd varvarvpn -g varvarvpn -M -s /bin/bash \
&& echo 'varvarvpn:Docker!' | chpasswd

COPY src /home/varvarvpn
COPY script /home/varvarvpn
COPY Makefile /home/varvarvpn

RUN chown varvarvpn:varvarvpn -R src

COPY docker-entrypoint.sh .
RUN chmod 755 /docker-entrypoint.sh

WORKDIR /home/varvarvpn
USER varvarvpn

ENTRYPOINT [ "/docker-entrypoint.sh" ]