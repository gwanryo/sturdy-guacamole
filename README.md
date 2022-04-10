# sturdy-guacamole

![StarWars](https://salt-pro.com/wp-content/uploads/2017/01/may_the_force_be_with_you___yoda_flag_by_osflag-d9xe904.jpg)
May the Force Be With You

## Getting Started

This project is based on Python Flask.

### Prerequisites

* docker, docker-compose

### How to run

1. Clone the repo

    ```bash
    git clone https://github.com/gwanryo/sturdy-guacamole
    ```

2. Write .env based on .env.sample, all values are essential

    ```bash
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASS=
    DB_CONN_MIN=
    DB_CONN_MAX=
    ```

3. Build image, and run

    ```bash
    cd sturdy-guacamole
    docker-compose build
    docker-compose up -d
    ```
