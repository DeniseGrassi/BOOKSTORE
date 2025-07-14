FROM python:3.10-slim AS python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# PATH atualizado
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala Poetry via pip em vez do script oficial (mais confiável nesse caso)
RUN pip install "poetry>=1.7.1" && mkdir -p $POETRY_HOME/bin && ln -s "$(which poetry)" $POETRY_HOME/bin/poetry

# Confirma a versão instalada (opcional)
RUN poetry --version



# Define diretório de trabalho
WORKDIR $PYSETUP_PATH

# Copia os arquivos de dependência
COPY poetry.lock pyproject.toml README.md ./

# Instala dependências de runtime
RUN poetry install --only main --no-root

# Define diretório principal da aplicação
WORKDIR /app

# Copia o restante da aplicação
COPY . /app/

# Expõe a porta da aplicação
EXPOSE 8000

# Comando padrão para rodar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

