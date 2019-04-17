import json

class PermissionsResource(object):
    def getPermissions(self, a):
      permission_set = {"android.permission.INTERNET", "android.permission.CHANGE_CONFIGURATION",
                        "android.permission.HARDWARE_TEST", "com.android.launcher.permission.INSTALL_SHORTCUT",
                        "android.permission.BIND_VPN_SERVICE", "android.permission.BLUETOOTH_PRIVILEGED",
                        "android.permission.WRITE_CALL_LOG", "android.permission.WRITE_SYNC_SETTINGS",
                        "android.permission.SYSTEM_ALERT_WINDOW", "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS",
                        "android.permission.CHANGE_WIFI_STATE", "android.permission.RECORD_AUDIO",
                        "android.permission.READ_PROFILE", "android.permission.ACCOUNT_MANAGER",
                        "android.permission.STOP_APP_SWITCHES", "android.permission.ACCESS_WIFI_STATE",
                        "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE",
                        "android.permission.CONTROL_LOCATION_UPDATES", "android.permission.REBOOT",
                        "android.permission.ACCESS_NETWORK_STATE", "android.permission.WRITE_USER_DICTIONARY",
                        "com.android.browser.permission.READ_HISTORY_BOOKMARKS", "android.permission.RECEIVE_SMS,",
                        "android.permission.WRITE_CONTACTS", "android.permission.READ_CONTACTS",
                        "android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED", "android.permission.WRITE_SETTINGS",
                        "android.permission.READ_INPUT_STATE", "android.permission.MANAGE_APP_TOKENS",
                        "com.android.email.permission.ACCESS_PROVIDER",
                        "com.android.launcher.permission.WRITE_SETTINGS",
                        "android.permission.MODIFY_AUDIO_SETTINGS", "android.permission.WRITE_APN_SETTINGS",
                        "android.permission.ACCESS_SURFACE_FLINGER", "android.permission.READ_LOGS",
                        "android.permission.UPDATE_DEVICE_STATS", "android.permission.MANAGE_ACCOUNTS",
                        "android.permission.SEND_SMS", "android.permission.INTERACT_ACROSS_USERS_FULL",
                        "android.permission.DELETE_PACKAGES", "android.permission.DOWNLOAD_WITHOUT_NOTIFICATION",
                        "android.permission.RECEIVE_BOOT_COMPLETED", "android.permission.VIBRATE",
                        "android.permission.CALL_PHONE", "android.permission.READ_PHONE_STATE",
                        "android.permission.CLEAR_APP_USER_DATA", "android.permission.KILL_BACKGROUND_PROCESSES",
                        "android.permission.CAMERA", "android.permission.WAKE_LOCK",
                        "android.permission.ACCESS_DOWNLOAD_MANAGER", "android.permission.RESTART_PACKAGES",
                        "android.permission.GET_ACCOUNTS", "android.permission.SUBSCRIBED_FEEDS_READ",
                        "android.permission.READ_SYNC_SETTINGS", "com.android.launcher.permission.UNINSTALL_SHORTCUT",
                        "android.permission.USE_CREDENTIALS", "android.permission.ACCESS_COARSE_LOCATION",
                        "com.android.email.permission.READ_ATTACHMENT", "android.permission.ACCESS_FINE_LOCATION",
                        "android.permission.WRITE_EXTERNAL_STORAGE", "android.permission.INSTALL_PACKAGES",
                        "android.permission.AUTHENTICATE_ACCOUNTS", "com.android.launcher.permission.READ_SETTINGS"}
      data = a.get_permissions()
      ans = ""
      for val in permission_set:
          if val in data:
              ans = ans + "2,"
          else:
              ans = ans + "1,"
      return ans[:-1]