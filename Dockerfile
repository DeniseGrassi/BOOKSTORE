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
    PYSETUP_PATH="/app" \
    VENV_PATH="/app/.venv"

# Atualiza o PATH para usar o ambiente virtual
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install "poetry>=1.7.1"

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependência
COPY poetry.lock pyproject.toml README.md ./

# Instala todas as dependências (inclusive Django)
RUN poetry install --no-root

# Copia o restante do código
COPY . .

# Define o diretório onde está o manage.py
WORKDIR /app/backend/backend/bookstore

# Coleta arquivos estáticos
RUN poetry run python manage.py collectstatic --noinput

# Comando padrão para subir o backend
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]


