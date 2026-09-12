MiiX Python 用例运行说明

1. 用 PyCharm 打开这个 Git 仓库目录。
2. 选择本机 Python 3 解释器。
3. 在 Terminal 执行：pip install -r requirements.txt。
4. 手机打开 USB 调试，确认 adb devices 里只有一台在线设备，或在 PyCharm Run Configuration 的 Environment variables 里设置 MIIX_SERIAL=设备ID。
5. 直接运行 cases/TC-xxx/TC-xxx.py，或添加参数：--serial 设备ID --params '{"account":"test"}'。

每个用例的最新日志在 run/latest.log，截图默认在 screenshots。运行时依赖在 vendor/miix_workflow_runtime.py。
