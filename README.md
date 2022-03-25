# AIRFLOW TEMPLATE

Template para subir projetos Airflow com a arquitetura Celery do zero.

&nbsp;
## Tecnologia

Aqui estão as tecnologias utilizadas neste projeto

* Airflow  - v2.1.0
* Postgres - v13
* Redis    - vLatest

&nbsp;
## Configuração

Ubuntu 20.04

* Criar repositório:
```
    mkdir /workspace
    cd /workspace
```

### Instalar Docker

* Atualize o aptíndice de pacotes e instale pacotes para permitir apto uso de um repositório por HTTPS
```
    sudo apt-get update
```
* Adicione a chave GPG oficial do Docker
```
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
* Use o comando a seguir para configurar o repositório estável
```
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
* Atualize o aptíndice de pacotes e instale a versão mais recente do Docker Engine
```
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
```


### Instalar Docker-compose

* Baixar versão estável do Docker compose
```
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

* Aplicar permissões executáveis ​​ao binário
```
    chmod +x /usr/local/bin/docker-compose
```

* Clonar repositório
```
    git clone https://github.com/Aasta97/airflow-template.git
    cd airflow-template/
```


&nbsp;
## Como utilizar

Subir containers:
```
    docker-compose up
```

Acessar URL:
```
    http://[IP do Servidor]:8080/
```

&nbsp;
## Não encontrou o que procurava? Acesse [Airflow Template](https://github.com/Aasta97/airflow-template.git)!