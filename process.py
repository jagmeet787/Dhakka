import time

from permissions import PermissionsResource
from database import database

from androwarn.warn.report.report import generate_report
from androwarn.warn.analysis.analysis import perform_analysis
from androwarn.warn.search.search import grab_application_package_name

from androguard.misc import AnalyzeAPK


class process(object):
    permissions_service = PermissionsResource()
    database_service = database()
    upload_directory_base = "./Files"

    def process_apk(self):
        taks_list = self.database_service.get_processing()
        for records in taks_list:
            apk_id = records[0]
            apk_name = records[3]
            file_dir = self.upload_directory_base + "/" + str(apk_id) + "/"
            file_path = file_dir + apk_name
            a, d, dx = AnalyzeAPK(file_path)
            permissions = self.permissions_service.getPermissions(a)
            # print permissions
            package_name = grab_application_package_name(a)
            data = perform_analysis(file_path, a, d, dx, False)
            # 'Verbosity level (ESSENTIAL 1, ADVANCED 2, EXPERT 3) (default 1)'
            generate_report(package_name, data, 1, 'html', file_dir + 'index.html')
            # maldrolyzer report and send back in the body

            self.database_service.update_record(apk_id,"Finished")

process_ins = process()
while (True):
    process_ins.process_apk()
    # time.sleep(100)