# FastAPI + Vue.js 全栈项目模板

这是一个通用的全栈Web应用开发模板，采用FastAPI作为后端框架，Vue.js作为前端框架，提供了完整的项目结构和基础功能。

## 项目结构

```
full_stack/
├── backend/                    # 后端 FastAPI 服务
│   ├── api/                    # API 路由定义
│   │   ├── __init__.py        # 包初始化文件
│   │   └── index.py           # 默认路由模块（示例）
│   ├── conf/                   # 配置文件目录
│   │   └── application.yaml   # 应用主配置文件（服务器、数据库、Redis 等）
│   ├── middleware/             # 中间件层
│   │   ├── __init__.py        # 包初始化文件
│   │   └── http_log_middleware.py  # HTTP 请求日志记录中间件
│   ├── repository/             # 数据访问层（Repository 模式）
│   │   ├── __init__.py        # 包初始化文件
│   │   ├── base_repository.py # 基础仓储类（CRUD 操作封装）
│   │   ├── data_struct.sql    # 数据库表结构定义 SQL
│   │   └── models.py          # SQLAlchemy ORM 模型定义
│   ├── service/                # 业务逻辑层（可选）
│   │   └── __init__.py        # 包初始化文件
│   ├── utils/                  # 工具类和公共模块
│   │   ├── tests/             # 工具类测试目录
│   │   │   ├── __init__.py
│   │   │   └── test.py        # 测试文件
│   │   ├── __init__.py        # 包初始化文件
│   │   ├── constains.py       # 常量定义（项目路径、应用名称等）
│   │   ├── database.py        # 数据库连接配置和会话管理
│   │   ├── exception.py       # 自定义异常处理
│   │   ├── logger.py          # 日志配置和获取函数
│   │   ├── other.py           # 其他工具函数（YAML 配置读取等）
│   │   ├── response.py        # 统一响应格式处理
│   │   └── system.py          # 系统初始化函数（路由、中间件、OpenAPI 等）
│   ├── __init__.py            # 包初始化文件
│   ├── main.py                # 应用入口文件（Uvicorn 启动配置）
│   └── requirements.txt       # Python 依赖包列表
│
└── frontend/                   # 前端 Vue.js + TypeScript 项目
    ├── public/                 # 公共静态资源目录
    │   ├── favicon.ico        # 网站图标
    │   └── index.html         # HTML 模板
    ├── src/                    # 源代码目录
    │   ├── api/               # API 接口定义
    │   │   └── api.ts         # API 调用封装
    │   ├── assets/            # 静态资源（图片、样式等）
    │   │   └── logo.png
    │   ├── components/        # Vue 组件目录
    │   │   └── HelloWorld.vue # 示例组件
    │   ├── pages/             # 页面组件目录
    │   │   └── .gitkeep       # 占位文件（保持空目录结构）
    │   ├── router/            # 路由配置
    │   │   └── index.ts       # Vue Router 配置
    │   ├── utils/             # 前端工具函数
    │   │   ├── axios.ts       # Axios 封装和拦截器配置
    │   │   └── public.ts      # 公共工具函数
    │   ├── App.vue            # 根组件
    │   ├── main.ts            # 应用入口文件
    │   └── shims-vue.d.ts     # TypeScript 类型声明文件
    ├── .browserslistrc        # 浏览器兼容性配置
    ├── .eslintrc.js           # ESLint 代码检查配置
    ├── __init__.py            # （可删除，非必需）
    ├── babel.config.js        # Babel 转译配置
    ├── openapitools.json      # OpenAPI Generator 配置
    ├── package-lock.json      # 依赖版本锁定文件
    ├── package.json           # 项目配置和依赖管理
    ├── tsconfig.json          # TypeScript 编译配置
    └── vue.config.js          # Vue CLI 项目配置
```

### 目录说明

#### 后端目录结构
- **`api/`**: 存放所有 API 路由模块，按功能模块划分
- **`conf/`**: 存放配置文件，支持多环境配置
- **`middleware/`**: 存放 FastAPI 中间件，如日志、认证等
- **`repository/`**: 数据访问层，封装数据库 CRUD 操作
- **`service/`**: 业务逻辑层（可选），处理复杂业务逻辑
- **`utils/`**: 工具类集合，包括数据库、日志、响应格式化等

#### 前端目录结构
- **`public/`**: 公共资源目录，编译时会直接复制到输出目录
- **`src/api/`**: 统一管理所有后端 API 接口调用
- **`src/assets/`**: 静态资源目录，会被 webpack 处理
- **`src/components/`**: 可复用的 Vue 组件
- **`src/pages/`**: 页面级组件，每个页面对应一个组件
- **`src/router/`**: 路由配置，定义页面导航
- **`src/utils/`**: 前端工具函数和第三方库封装

## 技术栈

### 后端 (FastAPI)
- **FastAPI**: 高性能Web框架，支持异步处理
- **Python**: 3.x 版本
- **数据库**: PostgreSQL (默认配置)
- **缓存**: Redis
- **ORM**: SQLAlchemy
- **日志**: loguru
- **配置管理**: YAML格式配置文件

### 前端 (Vue.js)
- **Vue.js**: 3.x 版本
- **TypeScript**: 类型安全
- **Vue Router**: 路由管理
- **Axios**: HTTP客户端
- **Ant Design Vue**: UI组件库
- **Sass**: CSS预处理器

## 功能特性

### 后端功能
- RESTful API设计
- 中间件支持 (HTTP日志记录)
- 数据库连接池管理
- 统一响应格式
- 异常处理机制
- 配置文件管理 (YAML格式)
- 环境变量支持

### 前端功能
- Vue 3 + TypeScript
- 模块化组件设计
- API接口统一管理
- 路由系统
- HTTP请求拦截器

## 快速开始

### 环境要求
- Python 3.8+
- Node.js 14+
- PostgreSQL
- Redis

### 后端启动

1. 安装Python依赖:
```bash
cd backend
pip install -r requirements.txt
```

2. 配置数据库连接:
修改 [backend/conf/application.yaml](file:///C:/Users/DELL/PycharmProjects/fastapi_framework/backend/conf/application.yaml) 文件中的数据库配置

3. 启动后端服务:
```bash
cd backend
python main.py
```

服务将运行在 `http://localhost:6789`

### 前端启动

1. 安装Node.js依赖:
```bash
cd frontend
npm install
```

2. 启动开发服务器:
```bash
npm run serve
```

前端开发服务器将运行在 `http://localhost:8080`

## 配置说明

项目配置文件位于 [backend/conf/application.yaml](file:///C:/Users/DELL/PycharmProjects/fastapi_framework/backend/conf/application.yaml)，包含以下配置项:

- **server**: 服务器配置 (端口、主机、环境等)
- **database**: 数据库连接配置
- **redis**: Redis连接配置
- **mcp**: 自定义配置项

## API文档

启动后端服务后，可以通过以下URL访问API文档:
- Swagger UI: `http://localhost:6789/docs`
- ReDoc: `http://localhost:6789/redoc`

## 开发规范

1. 遵循RESTful API设计原则
2. 使用TypeScript进行类型检查
3. 遵循代码风格指南
4. 编写单元测试

## 扩展功能

- 数据库迁移支持
- 用户认证和授权
- 日志管理
- 缓存策略
- API版本控制

## 部署

### 后端部署
使用Uvicorn部署生产环境:
```bash
uvicorn main:app --host 0.0.0.0 --port 6789 --workers 4
```

### 前端部署
构建生产版本:
```bash
npm run build
```

## 许可证

此项目为通用模板，可自由使用和修改。