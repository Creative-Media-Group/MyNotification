from mynotification import Notification
import sys

platform = sys.platform
print(platform)
x = Notification(title="test", message="test", platform=platform)
x.send_mynotification()
