"""empty message

Revision ID: 11b247298da4
Revises: 44fe26926437
Create Date: 2016-04-25 15:02:37.899716

"""

# revision identifiers, used by Alembic.
revision = '11b247298da4'
down_revision = '44fe26926437'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_stats():
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("activity_stream_stats_daily", "addon_version",
                    type_=sa.String(length=64))
    op.alter_column("activity_stream_stats_daily", "page",
                    type_=sa.String(length=64))
    op.alter_column("activity_stream_events_daily", "addon_version",
                    type_=sa.String(length=64))
    op.alter_column("activity_stream_events_daily", "page",
                    type_=sa.String(length=64))
    ### end Alembic commands ###


def downgrade_stats():
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("activity_stream_stats_daily", "addon_version",
                    type_=sa.String(length=16))
    op.alter_column("activity_stream_stats_daily", "page",
                    type_=sa.String(length=16))
    op.alter_column("activity_stream_events_daily", "addon_version",
                    type_=sa.String(length=16))
    op.alter_column("activity_stream_events_daily", "page",
                    type_=sa.String(length=16))
    ### end Alembic commands ###
