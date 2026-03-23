import time

from sqlalchemy import Column, BIGINT, inspect, String, JSON, ARRAY

from utils.database import Base


class BaseModel(Base):
    """基础模型"""

    __table_args__ = {"schema": "decision_engine"}

    __abstract__ = True
    id = Column(BIGINT(), primary_key=True, autoincrement=True)
    create_time = Column(BIGINT(), default=int(time.time()), comment="创建时间")
    update_time = Column(BIGINT(), default=int(time.time()), onupdate=int(time.time()),
                         comment="更新时间")

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class CombatTask(BaseModel):
    """作战任务"""

    __tablename__ = "combat_task"

    name = Column(String(64), comment="名称")
    description = Column(String(512), comment="描述")
    status = Column(String(16), comment="状态")
    init_situation = Column(JSON, comment="初始态势")
    flow_json = Column(JSON, comment="攻击流程图")
    limit_att_ck = Column(ARRAY(String), comment="限制技战术")
    tendency = Column(String(64), comment="作战倾向")

