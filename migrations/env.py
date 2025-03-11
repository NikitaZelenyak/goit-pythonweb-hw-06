from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context

from conf.db import URI
from entity.models import Base

# Ініціалізація Alembic Config
config = context.config

# Логування (якщо є .ini файл)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Передаємо URI напряму, не використовуємо engine_from_config
config.set_main_option("sqlalchemy.url", URI)

# Вказуємо моделі для autogenerate
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запуск міграцій в офлайн режимі (без з'єднання з базою)."""
    context.configure(
        url=URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Запуск міграцій в онлайн режимі (з підключенням до бази)."""
    engine = create_engine(URI, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Визначаємо, який режим запускати
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
