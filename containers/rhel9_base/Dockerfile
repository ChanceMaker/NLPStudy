FROM redhat/ubi9-minimal
RUN dnf update -y && \
    dnf install -y nginx && \
    dnf clean all

EXPOSE 80

CMD ["nginx","-g","daemon off;"]
