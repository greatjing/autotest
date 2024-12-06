# 自动化测试项目

这是一个用于自动化测试的项目，旨在通过使用 `pytest` 框架来提高测试效率和准确性。该项目支持生成 HTML 报告，并能够分类显示冒烟测试和其他测试用例的结果。

## 目录

- [安装](#安装)
- [使用](#使用)
- [测试](#测试)
- [贡献](#贡献)
- [许可证](#许可证)

## 安装

1. 克隆这个仓库：
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```
2. 进入项目目录：
   ```bash
   cd your-repo-name
   ```
3. 创建并激活虚拟环境（可选）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
   ```
4. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用

在项目中，您可以使用以下命令运行测试并生成 HTML 报告：

```bash
pytest --html=reports/html/report.html --self-contained-html -v
```

### 运行冒烟测试

要仅运行冒烟测试并生成报告：

```bash
pytest -m smoke --html=reports/html/smoke_report.html --self-contained-html -v
```

### 运行其他测试

要运行其他测试并生成报告：

```bash
pytest -m "not smoke" --html=reports/html/other_report.html --self-contained-html -v
```

## 测试

在项目中，您可以使用以下命令运行所有测试：

```bash
pytest --html=reports/html/summary_report.html --self-contained-html -v
```

## 贡献

欢迎贡献！请遵循以下步骤：

1. Fork 这个仓库。
2. 创建您的特性分支：
   ```bash
   git checkout -b feature/YourFeature
   ```
3. 提交您的更改：
   ```bash
   git commit -m "添加了一个新特性"
   ```
4. 推送到分支：
   ```bash
   git push origin feature/YourFeature
   ```
5. 创建一个 Pull Request。

## 许可证

此项目使用 [MIT 许可证](LICENSE)。