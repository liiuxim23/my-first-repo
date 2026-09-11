# MiiX 工作流原型 · 动作代码示例
def test_case(device, params):

    # [s125] 点击控件
    device(resource_id="app:id/login_account").click(timeout=10)

    # [s118] 点击免费电子书
    device(description="免费电子书").click(timeout=10)

    # [s123] 等待时长
    device.sleep(10)

    # [s121] 点击mine_button
    device(description="mine_button").click(timeout=10)

    # [s122] 点击bookshelf_button
    device(description="bookshelf_button").click(timeout=10)

    # [s124] 截图留证
    device.screenshot()

if __name__ == "__main__":
    import argparse
    import json
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "vendor")))
    from miix_workflow_runtime import Device
    parser = argparse.ArgumentParser(description="Run this MiiX Python case directly from PyCharm or terminal.")
    parser.add_argument("--serial", default=os.environ.get("MIIX_SERIAL"), help="Android device serial. If omitted, MiiX uses MIIX_SERIAL or the only online adb device.")
    parser.add_argument("--params", default="{}", help="JSON params, for example: {"account":"test"}")
    args = parser.parse_args()
    device = Device(args.serial)
    test_case(device, json.loads(args.params))
    print(json.dumps({"status": "passed", "serial": device.serial, "steps": device.results}, ensure_ascii=False, indent=2))
