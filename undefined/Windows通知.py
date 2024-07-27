import winotify

# 创建通知对象
notify = winotify.Notification(
    app_id='QQ',
    title='Hello',
    # icon='path/to/icon.ico',
    duration='short',
    msg='This is a test notification.'
)


if __name__ == '__main__':
    # 显示通知
    notify.show()
