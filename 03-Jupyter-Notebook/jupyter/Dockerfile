FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update --fix-missing \
    && apt-get -y install --no-install-recommends \
        build-essential \
        python3-yaml \
        python3-six \
        python3-setuptools \
        python3-dev \
        cmake \
        curl \
        python3-pip \
        supervisor \
        git \
    && python3 -m pip install \
        jupyter \
        jupyterlab \
        jupyterlab-git \
        ipympl

# keep this (mostly) separate to quickly alter packages
# you would like to have in the notebook environment
RUN python3 -m pip install \
        matplotlib \
        scikit-learn==0.22.1 \
        scipy==1.4.1 \
        pandas
        
COPY files/entrypoint.sh /bin/entrypoint.sh
COPY files/supervisor_jupyter /etc/supervisor/conf.d/jupyter.conf
RUN chmod +x /bin/entrypoint.sh \
    && mkdir -p /service /etc/supervisor/conf.d /var/run/supervisor 

ARG HOST_UID=${HOST_UID:-0}
ARG HOST_USER=${HOST_USER:-root}
ARG USER_HOME=${USER_HOME:-/root}

RUN sh -c "[ \"${HOST_USER}\" = root ]" || \
    (groupadd -r ${HOST_USER} -g ${HOST_UID} \
    && useradd -d "${USER_HOME}" -M -r -l -N -s /usr/sbin/nologin \
       -u ${HOST_UID} -g ${HOST_UID} ${HOST_USER} \
    && mkdir -p "${USER_HOME}" \
    && chown -R "${HOST_UID}:${HOST_UID}" "${USER_HOME}") \
    && sed -i "s:{{ *HOST_USER *}}:${HOST_USER}:g;s:{{ *USER_HOME *}}:${USER_HOME}:g" \
        /etc/supervisor/conf.d/jupyter.conf \
    && chown -R "${HOST_UID}:${HOST_UID}" /var/run/supervisor/.

RUN if [ -e /usr/bin/sudo ];then \
        chmod u+s /usr/bin/sudo; \
        (umask 0227 && echo "${HOST_USER}  ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers.d/users); \
    fi

USER ${HOST_USER}
WORKDIR ${USER_HOME}
EXPOSE 8888
CMD sh /bin/entrypoint.sh
