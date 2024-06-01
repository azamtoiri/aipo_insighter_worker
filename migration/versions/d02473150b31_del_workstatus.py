"""del workstatus

Revision ID: d02473150b31
Revises: ee395199f4d7
Create Date: 2024-05-21 11:44:46.341735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd02473150b31'
down_revision: Union[str, None] = 'ee395199f4d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###


    op.execute('DROP TABLE IF EXISTS statuses CASCADE')
    op.execute('DROP TABLE IF EXISTS stages CASCADE')
    op.execute('DROP TABLE IF EXISTS worker_statuses CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stages',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('stages_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('stage_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='stages_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('statuses',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('statuses_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('status_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='statuses_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('worker_statuses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('stage_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('assistant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('process_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('file_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('end_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('error_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('error_message', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['assistant_id'], ['ai_assistants.assistant_id'], name='worker_statuses_assistant_id_fkey'),
    sa.ForeignKeyConstraint(['file_id'], ['files.id'], name='worker_statuses_file_id_fkey'),
    sa.ForeignKeyConstraint(['stage_id'], ['stages.id'], name='worker_statuses_stage_id_fkey'),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], name='worker_statuses_status_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='worker_statuses_pkey')
    )
    # ### end Alembic commands ###