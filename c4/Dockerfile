FROM python:3.8-alpine

RUN apk update && \
    apk add --no-cache --virtual .for-build build-base curl fontconfig && \
    apk add --no-cache freetype-dev && \
    curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip &&  \
    mkdir -p /usr/share/fonts/NotoSansCJKjp && \
    unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/NotoSansCJKjp/ && \
    rm NotoSansCJKjp-hinted.zip && \
    fc-cache -fv && \
    pip install numpy matplotlib && \
    echo "font.serif      : Noto Serif CJK JP, DejaVu Serif, DejaVu Serif, Bitstream Vera Serif, Computer Modern Roman, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino" >> /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc && \
    echo "font.sans-serif : Noto Sans CJK JP, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif" >> /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc && \
    rm -rf ~/.cache/matplotlib && \
    apk del --purge .for-build && \
    apk add --no-cache libstdc++
