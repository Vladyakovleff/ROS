FROM ubuntu:20.04

# Задание тайм-зоны и метода установки
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Обновление списка пакетов и установка зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    lsb-release \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Установка ROS Noetic
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros-latest.list' \
    && curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y \
    ros-noetic-ros-base \
    && rm -rf /var/lib/apt/lists/*

# Установка прочих зависимостей
RUN apt-get update && apt-get install -y \
    python3-pip \
    && pip3 install Flask \
    && rm -rf /var/lib/apt/lists/*

# Все файлы пакета должны быть скопированы в /app
COPY . /app

# Перемещаемся в каталог
WORKDIR /app

# Обновление путей
ENV PYTHONPATH="${PYTHONPATH}:/opt/ros/noetic/lib/python3/dist-packages"
ENV PATH="${PATH}:/opt/ros/noetic/bin"

# Установка переменных окружения ROS
RUN mkdir -p /home/user/catkin_ws/src
COPY . /home/user/catkin_ws/src/webserver_package
WORKDIR /home/user/catkin_ws

RUN . /opt/ros/noetic/setup.sh && \
    catkin_make && \
    . devel/setup.bash && \
    echo "source /home/user/catkin_ws/devel/setup.bash" >> ~/.bashrc

ENV ROS_PACKAGE_PATH="/opt/ros/noetic/share:/home/user/catkin_ws/src"
ENV LD_LIBRARY_PATH="/opt/ros/noetic/lib"

# Запуск ноды веб-сервера
CMD ["rosrun", "webserver_package", "webserver_node.py"]
