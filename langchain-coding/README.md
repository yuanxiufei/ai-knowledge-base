# langchain-coding

当前项目使用 `uv` 管理 Python 版本和依赖，定位是轻量实验脚本工程。

## 安装依赖

```bash
uv sync
```

如果还没有虚拟环境，`uv sync` 会自动在项目内创建并同步 `.venv`。

如果你想更新锁文件或追加依赖，可以使用：

```bash
uv lock
uv add langchain
uv add langchain-openai
uv add openai
```

## 环境变量

先复制模板文件：

```bash
copy .env.example .env
```

`.env` 只用于本地运行，不提交仓库；仓库中保留 `.env.example` 作为模板。

可配置项：

- `OPENAI_API_KEY`
- `OPENAI_API_BASE_URL`

其余参数使用脚本内默认值；如果后续有需要，也可以在 `.env` 中额外添加：

- `OPENAI_MODEL`
- `ALI_API_KEY`
- `ALI_API_BASE_URL`
- `DEEPSEEK_API_KEY`
- `DEEPSEEK_API_BASE_URL`

## 运行脚本

```bash
uv run python 01-openai.py
```

## 当前文件

- `01-openai.py`
- `.env.example`
- `pyproject.toml`
- `uv.lock`
