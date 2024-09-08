FROM debian:buster
ARG USER_ID=1000
ARG QCAD_DIR=/usr/local/share/qcad

WORKDIR /tmp
RUN groupadd --gid "$USER_ID" qcad \
    && useradd -ms /bin/bash --gid "$USER_ID" --uid "$USER_ID" qcad

# update & install X11 libs needed by qcad
#   wget needed to download
RUN apt update \
    && apt --yes upgrade \
    && apt install --yes \
        libgl1 \
        libglib2.0-0 \
        libx11-6 \
        qt5-default \
        wget \
    && apt clean \
    && apt remove \
    && apt --yes autoremove

# install qcad in /usr/local
RUN wget -O /tmp/qcad.run \
    https://www.qcad.org/archives/qcad/qcad-3.30.1-trial-linux-x86_64.run \
    && chmod +x /tmp/qcad.run \
    && /tmp/qcad.run --target $QCAD_DIR \
    && ln -s $QCAD_DIR/qcad /usr/local/bin/qcad \
    && rm /tmp/qcad.run

# remove plugins for commercial version
#   reverting to community version
RUN rm \
    $QCAD_DIR/plugins/libqcadpdf.so \
    $QCAD_DIR/plugins/libqcadpolygon.so \
    $QCAD_DIR/plugins/libqcadproj.so \
    $QCAD_DIR/plugins/libqcadproscripts.so \
    $QCAD_DIR/plugins/libqcadproxies.so \
    $QCAD_DIR/plugins/libqcadshp.so \
    $QCAD_DIR/plugins/libqcadspatialindexpro.so \
    $QCAD_DIR/plugins/libqcadtrace.so \
    $QCAD_DIR/plugins/libqcadtriangulation.so \
    $QCAD_DIR/plugins/libqcaddwg.so

USER qcad
CMD ["/usr/local/bin/qcad"]


