"""Provide info to system health for duckdb."""

from __future__ import annotations

from sqlalchemy import text
from sqlalchemy.orm.session import Session


def db_size_bytes(session: Session, database_name: str) -> float | None:
    """Get the duckdb database size."""
    session.execute(text("SET database_size;"))    
    size = session.execute(
        text(
            "SELECT database_size "
            "FROM pragma_database_size();"
        )
    ).scalar()

    if not size:
        return None

    return float(size)
